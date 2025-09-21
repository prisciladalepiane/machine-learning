# Módulo de Consumo da API do Modelo

import requests # Importa a biblioteca requests para fazer requisições HTTP
import pandas as pd
import json

def previsao(data):
    
    # Define a URL da API de deploy do modelo
    url = "http://localhost:5100/predict"
    
    # Define os cabeçalhos da requisição HTTP
    headers = {"Content-Type": "application/json"}
    
    # Converte os dados do DataFrame para o formato JSON
    data_json = data.to_json(orient = "records")
    
    # Faz uma requisição POST para o serviço da API
    response = requests.post(url, headers = headers, data = data_json)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        
        # Se sim, obtém as previsões 
        predictions = response.json()
        
        # Retorna as previsões
        return predictions
    else:
        
        # Se não, imprime o código de erro e a mensagem de erro
        print(f"Error: {response.status_code}, {response.text}")
        
        # Retorna None em caso de erro
        return None

# Executa o código se o script for executado diretamente
if __name__ == "__main__":
    
    # Dados de exemplo para previsão
    data = pd.DataFrame({
        "X1": [0.5],
        "X2": [4.8],
        "X3": [1]
    })
    
    # Faz a previsão usando os dados de exemplo
    predictions = previsao(data)
    
    # Imprime a previsão
    print(f"\nPrevisão do Modelo: {predictions}\n")