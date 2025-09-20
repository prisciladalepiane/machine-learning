# Módulo de Deploy do Modelo

# Imports
import os
import joblib
from flask import Flask, request, jsonify
import pandas as pd

# Cria app Flask
app = Flask(__name__)

# Carregar o modelo mais recente
def carrega_modelo():
    
    model_path = 'modelos/modelo_mais_recente.pkl'
    modelo = joblib.load(model_path)

    return modelo

# Carrega o modelo mais recente
modelo = carrega_modelo()

@app.route('/predict', methods = ['POST'])
def predict():
    
    # Obtém os dados do corpo da requisição
    data = request.get_json()
    
    # Converte os dados para um DataFrame do pandas
    data_df = pd.DataFrame(data)
    
    # Faz previsões com o modelo
    predictions = modelo.predict(data_df)
    
    # Retorna as previsões como uma resposta JSON
    return jsonify(predictions.tolist())

# Executa a aplicação Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5100)