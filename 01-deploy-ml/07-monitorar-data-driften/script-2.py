# Projeto 7 - Monitoramento, Identificação e Mitigação de Model e Data Drift
# Script 2: Simulação de Data Drift e Avaliação do Modelo

# Imports
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

# Carrega o dataset
arquivo = 'dataset.csv'
wine_data = pd.read_csv(arquivo, delimiter = ';')

# Separa as features e o target
X = wine_data.drop('quality', axis = 1)
y = wine_data['quality']

# Divide o dataset em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.3, random_state = 42)

# Carrega o modelo treinado e o padronizador
modelo_arquivo = 'modelo_v1.pkl'
scaler_arquivo = 'scaler_v1.pkl'
modelo_dsa_v1 = joblib.load(modelo_arquivo)
scaler = joblib.load(scaler_arquivo)

# Padroniza os dados de teste
X_teste_scaled = scaler.transform(X_teste)

# Define a seed para reprodução dos resultados
np.random.seed(41)

# Função para simular Data Drift
def simula_data_drift(X, drift_factor):
    drifted_X = X + np.random.normal(0, drift_factor, X.shape)
    return drifted_X

# Simula Data Drift
X_test_drifted = simula_data_drift(X_teste_scaled, drift_factor = 0.7)

# Avaliar o modelo no conjunto de teste com Data Drift
drifted_predictions = modelo_dsa_v1.predict(X_test_drifted)
drifted_accuracy = accuracy_score(y_teste, drifted_predictions)

# Função para monitorar o desempenho do modelo
def monitora_performance_modelo(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Monitorar o desempenho do modelo antes e depois do drift
pre_drift_accuracy = round(monitora_performance_modelo(modelo_dsa_v1, X_teste_scaled, y_teste), 2)
post_drift_accuracy = round(monitora_performance_modelo(modelo_dsa_v1, X_test_drifted, y_teste), 2)

print("\nScript 2 - Simulação de Data Drift e Avaliação do Modelo")

print("\nAcurácia Antes do Data Drift:", pre_drift_accuracy)

print("\nAcurácia Depois do Data Drift:", post_drift_accuracy)

print("\nScript 2 Executado com Sucesso!\n")