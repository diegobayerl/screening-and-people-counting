# Detecção e Contagem de Pessoas

Este projeto consiste em um sistema de detecção e contagem de pessoas em tempo real usando OpenCV e modelos pré-treinados.

## Descrição

O objetivo deste projeto é utilizar técnicas de visão computacional para detectar e contar pessoas em um ambiente de vídeo em tempo real. O sistema utiliza o modelo pré-treinado "res10_300x300_ssd_iter_140000.caffemodel" em conjunto com o arquivo de configuração "deploy.prototxt" para realizar a detecção de pessoas. Além disso, implementamos a funcionalidade de rastreamento de pessoas usando o algoritmo CSRT.

O sistema exibe um retângulo delimitador ao redor de cada pessoa detectada, bem como a contagem atual de pessoas na tela. Também foi adicionada uma linha vertical para contar o número de pessoas que passam de um ponto A para um ponto B.

## Requisitos

- Python 3.x
- OpenCV
- Arquivos de modelo "deploy.prototxt" e "res10_300x300_ssd_iter_140000.caffemodel"

## Instalação

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

## Requisitos

- Python 3.x

## Verificando a versão do Python

Certifique-se de ter o Python 3.x instalado em seu sistema. Você pode verificar a versão do Python digitando o seguinte comando no terminal:

```bash
python --version
```
