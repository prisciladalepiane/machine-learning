# Projeto 7 - Monitoramento, Identificação e Mitigação de Model e Data Drift
# Script 1: Treinamento Inicial do Modelo

# Imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import joblib

# Carrega o dataset 
arquivo = 'dataset.csv'
wine_data = pd.read_csv(arquivo, delimiter = ';')

# Separa as features e o target
X = wine_data.drop('quality', axis = 1)
y = wine_data['quality']

# Divide o dataset em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.3, random_state = 42)

# Padroniza os dados
scaler = StandardScaler()
X_treino_scaled = scaler.fit_transform(X_treino)
X_teste_scaled = scaler.transform(X_teste)

# Treina o modelo inicial
modelo_v1 = RandomForestClassifier(random_state = 42)
modelo_v1.fit(X_treino_scaled, y_treino)

# Avalia o modelo no conjunto de teste inicial
previsoes = modelo_v1.predict(X_teste_scaled)
acuracia = round(accuracy_score(y_teste, previsoes), 2) * 100
report = classification_report(y_teste, previsoes)

print("\nScript 1 - Treinamento Inicial do Modelo")
print("\nAcurácia Inicial do Modelo (%):", acuracia)
print("\nRelatório de classificação:\n", report)

# Salva o modelo treinado e o padronizador
modelo_arquivo = 'modelo_v1.pkl'
scaler_arquivo = 'scaler_v1.pkl'
joblib.dump(modelo_v1, modelo_arquivo)
joblib.dump(scaler, scaler_arquivo)

print(f"\nModelo salvo: {modelo_arquivo}")
print(f"\nPadronizador salvo: {scaler_arquivo}")

print("\nScript 1 Executado com Sucesso!\n")