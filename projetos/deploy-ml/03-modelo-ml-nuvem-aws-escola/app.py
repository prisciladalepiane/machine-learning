# Deploy do modelo de Machine Learning na Nuvem AWS 
import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

def carregar_arquivo(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

modelo = carregar_arquivo('modelo_final.pkl')
scaler = carregar_arquivo('scaler_final.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def previsao():

    try:
        exame_ingles = float(request.form.get('exame_ingles', 0))
        nota_qi = int(request.form.get('nota_qi', 0))
        exame_psico = int(request.form.get('exame_psico', 0))

        if not (0 <= exame_ingles <= 10 and 0 <= nota_qi <= 200 and 0 <= exame_psico <= 100):
            raise ValueError("Valores de entrada inválidos.")
        
        dados_entrada = np.array([exame_ingles, nota_qi, exame_psico]).reshape(1,3)

        dados_entrada = pd.DataFrame(dados_entrada, columns=['nota_exame_ingles', 'valor_qi', 'nota_exame_psicotecnico'])

        dados_scaled = scaler.transform(dados_entrada)

        pred = modelo.predict(dados_scaled)

        resultado = pred[0]
        resultado = "O Aluno é aprovado" if pred[0] == 1 else "O Aluno não é aprovado"

    except Exception as e:
        resultado = f'Erro: {e}'

    return render_template('index.html', result=resultado)

if __name__ == "__main__":
    app.run()