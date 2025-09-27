# Projeto 7 - Monitoramento, Identificação e Mitigação de Model e Data Drift
# Script 3: Estratégia 1 de Mitigação de Data Drift -
# Retreinar o Modelo com os novos dados e otimizar Hiperparâmetros

# Imports
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
import joblib

# Carrega o dataset
arquivo = 'dataset.csv'
wine_data = pd.read_csv(arquivo, delimiter = ';')

# Separar as features e o target
X = wine_data.drop('quality', axis = 1)
y = wine_data['quality']

# Divide o dataset em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.3, random_state = 42)

# Padroniza os dados
scaler = StandardScaler()
X_treino_scaled = scaler.fit_transform(X_treino)
X_teste_scaled = scaler.transform(X_teste)

# Define a seed para reprodução dos resultados
np.random.seed(123)

# Função para simular Data Drift
def simula_data_drift(X, drift_factor):
    drifted_X = X + np.random.normal(0, drift_factor, X.shape)
    return drifted_X

# Simula Data Drift
X_test_drifted = simula_data_drift(X_teste_scaled, drift_factor = 0.7)

# Estratégia de Mitigação: Re-treinar o modelo com dados atualizados e otimização de hiperparâmetros
def retreina_modelo(X_train, y_train, X_new, y_new):

    X_combined = np.vstack((X_train, X_new))
    y_combined = np.hstack((y_train, y_new))

    # Define os hiperparâmetros para a otimização
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Cria um novo modelo
    modelo = RandomForestClassifier(random_state = 42)

    # Aplica GridSearchCV para encontrar os melhores hiperparâmetros
    # cv = 3 significa validação cruzada com 3 folds
    # n_jobs = -1 utiliza todos os núcleos do processador
    # verbose = 2 exibe o progresso
    grid_search = GridSearchCV(estimator = modelo, param_grid = param_grid, cv = 3, n_jobs = -1, verbose = 2)
    grid_search.fit(X_combined, y_combined)

    # Treina o modelo com os melhores hiperparâmetros
    best_model = grid_search.best_estimator_
    best_model.fit(X_combined, y_combined)
    
    return best_model

# Simula novos dados de treinamento (por simplicidade, reutilizamos X_test_drifted)
X_new_train, X_new_test, y_new_train, y_new_test = train_test_split(X_test_drifted, y_teste, test_size = 0.3, random_state = 42)


print("\nOtimização de Hiperparâmetros...\n")

# Re-treinar o modelo com os novos dados e otimização de hiperparâmetros
modelo_v2 = retreina_modelo(X_treino_scaled, y_treino, X_new_train, y_new_train)

# Função para monitorar o desempenho do modelo
def monitora_performance_modelo(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Avaliar o modelo re-treinado
acuracia_pos_retreino = round(monitora_performance_modelo(modelo_v2, X_new_test, y_new_test), 2)

print("\nProjeto 7 - Script 3 - Estratégia de Mitigação de Data Drift")

print("\nAcurácia após retreinamento do modelo com novos dados e otimização de hiperparâmetros:", acuracia_pos_retreino)

# Salva o modelo treinado e o padronizador
modelo_arquivo = 'modelo_v2.pkl'
scaler_arquivo = 'scaler_v2.pkl'
joblib.dump(modelo_v2, modelo_arquivo)
joblib.dump(scaler, scaler_arquivo)

print(f"\nModelo salvo: {modelo_arquivo}")
print(f"\nPadronizador salvo: {scaler_arquivo}")

print("\nScript 3 Executado com Sucesso!\n")





