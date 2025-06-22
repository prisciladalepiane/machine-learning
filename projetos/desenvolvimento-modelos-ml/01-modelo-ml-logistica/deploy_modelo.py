from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)

# Carregar o modelo treinado
modelo = joblib.load('modelos/modelo_logistica.pkl')
le_tipo_embalagem = joblib.load('modelos/transformador_tipo_embalagem.pkl')
le_tipo_produto = joblib.load('modelos/transformador_tipo_produto.pkl')

# DEfinir a rota principal para a pagina
@app.route('/', methods=['GET'])
def index():
    return render_template('template.html')

# Definir a rota para receber os dados do formulário
@app.route('/predict', methods=['POST'])
def predict():

    peso = int(request.form['peso'])

    tipo_embalagem = le_tipo_embalagem.transform([request.form['tipo_embalagem']])[0]

    prediction = modelo.predict([[peso, tipo_embalagem]])[0]

    tipo_produto = le_tipo_produto.inverse_transform([prediction])[0]

    return render_template('template.html', prediction=tipo_produto)

if __name__ == '__main__':
    app.run()