import cv2
import os

#pegar diretorio atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Carrega o modelo pré-treinado para detecção de pessoas
pedestrian_net = cv2.dnn.readNetFromCaffe(
    os.path.join(diretorio_atual, 'model/deploy.prototxt'),
    os.path.join(diretorio_atual, 'model/res10_300x300_ssd_iter_140000.caffemodel')
)

# Inicializa a câmera
camera = cv2.VideoCapture(0)  # 0 representa a câmera padrão, mas você pode modificar se necessário

# Inicializa a contagem de pessoas
count_people = 0
total_people = 0
is_counted = False

# Define as coordenadas da linha vertical
line_position = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2

while True:
    # Lê o frame da câmera
    ret, frame = camera.read()

    # Redimensiona o frame para um tamanho específico para a detecção de pessoas
    resized_frame = cv2.resize(frame, (300, 300))

    # Prepara o frame para ser usado pelo modelo de detecção
    blob = cv2.dnn.blobFromImage(resized_frame, 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=True, crop=False)

    # Passa o blob pela rede neural para detecção de pessoas
    pedestrian_net.setInput(blob)
    detections = pedestrian_net.forward()

    # Loop pelas detecções e contagem de pessoas
    count_people = 0
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            # Obtém as coordenadas do retângulo delimitador da detecção
            box = detections[0, 0, i, 3:7] * [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]
            (startX, startY, endX, endY) = box.astype("int")

            # Desenha o retângulo delimitador da detecção no frame
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

            # Verifica se o quadrado encostou na linha vertical
            if startX <= line_position <= endX:
                if not is_counted:
                    count_people += 1
                    total_people += 1
                    is_counted = True
            else:
                is_counted = False

    # Exibe a contagem atual e total de pessoas
    cv2.putText(frame, f'Contagem Total: {total_people}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Desenha a linha vertical no frame
    cv2.line(frame, (line_position, 0), (line_position, frame.shape[0]), (0, 0, 255), 2)

    # Mostra o frame resultante
    cv2.imshow('Deteccao de Pessoas', frame)

    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Salva a última contagem em um arquivo de texto
with open('total_contado.txt', 'w') as arquivo:
    arquivo.write(f'Veiculos: {total_people}\n')

# Libera os recursos utilizados
camera.release()
cv2.destroyAllWindows()