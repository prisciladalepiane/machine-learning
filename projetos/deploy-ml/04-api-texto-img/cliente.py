# Projeto 4 - Deploy de API Para Geração de Texto a Partir de Imagens com LLM
# Módulo Cliente

# Import
import requests

# URL da API
url = "http://localhost:3000/api"

# Payload (texto de entrada para o LLM)
#payload = {'text': (None, 'Which color is the car in the image?')}
#payload = {'text': (None, 'Which color is the elephant in the image?')}
payload = {'text': (None, 'What is the dog doing in the image?')}

# Imagem enviada para o modelo
#file = [('image', open('img/imagem1.png','rb'))]
#file = [('image', open('img/imagem2.png','rb'))]
file = [('image', open('img/imagem3.jpg','rb'))]

# Cabeçalho
headers = {'accept': 'application/json'}

# Faz a requisição à API e armazena a resposta
resposta = requests.request("POST", 
                            url, 
                            headers = headers, 
                            data = payload, 
                            files = file)

print(resposta.text)
