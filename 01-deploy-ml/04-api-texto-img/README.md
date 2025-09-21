# Deploy de API para geração de texto a partir de imagens com LLM

O Projeto visa desenvolver e implantar uma API  que utiliza Modelo de  Linguagem de Grande  Escala  (LLM)  para  gerar  texto  a  partir  de  imagens. 

Objetivo: Construir  a  API  e  então implantá-la em um container Docker que poderá ser executando independente de plataforma, local ou na nuvem. 

Modelo usado disponível no link: https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

Plataforma de busca por LLMs: huggingface.co

FastAPI: [fastapi](https://fastapi.tiangolo.com)

## Instruções Para Execução do Projeto 

Abra o terminal ou prompt de comando e navegue até a pasta onde está os arquivos

Execute o comando abaixo para criar a imagem Docker

`docker build -t pri-deploy:p4 .`

Execute o comando abaixo para criar o container Docker

`docker run -dit --name pri-p4 -p 3000:3000 pri-deploy:p4`

Visualize os logs para verificar se a API já foi inicializada

`docker logs pri-p4`

Então execute a chamada cliente

`python cliente.py`
