# Projeto 7 - Monitoramento, Identificação e Mitigação de Model e Data Drift
# Script 5: Estratégia 3 de Mitigação de Data Drift
# Retreinar o Modelo com os Novos Dados, Otimizar Hiperparâmetros, Combinar Diferentes Algoritmos

# Imports
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
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

# Define a seed para reprodução dos resultados
np.random.seed(29)

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
    param_grid_gbc = {
        'n_estimators': [400, 500, 600],
        'learning_rate': [0.0001, 0.001, 0.01],
        'max_depth': [3, 5, 7],
        'subsample': [0.8, 0.9, 1.0]
    }
    
    param_grid_svc = {
        'C': [0.1, 1, 10],
        'kernel': ['linear', 'rbf'],
        'gamma': ['scale', 'auto']
    }

    # Cria novos modelos
    gbc = GradientBoostingClassifier(random_state = 42)
    svc = SVC(probability = True, random_state = 42)
    
    # Aplica GridSearchCV para encontrar os melhores hiperparâmetros
    grid_search_gbc = GridSearchCV(estimator = gbc, param_grid = param_grid_gbc, cv = 3, n_jobs = -1, verbose = 2)
    grid_search_gbc.fit(X_combined, y_combined)
    
    grid_search_svc = GridSearchCV(estimator = svc, param_grid = param_grid_svc, cv = 3, n_jobs = -1, verbose = 2)
    grid_search_svc.fit(X_combined, y_combined)

    # Treina os modelos com os melhores hiperparâmetros
    best_gbc = grid_search_gbc.best_estimator_
    best_svc = grid_search_svc.best_estimator_

    # Cria um ensemble dos melhores modelos
    # voting='soft' usa as probabilidades previstas para fazer a classificação final
    ensemble_model = VotingClassifier(estimators = [('gbc', best_gbc), ('svc', best_svc)], voting = 'soft')
    ensemble_model.fit(X_combined, y_combined)
    
    return ensemble_model

# Simula novos dados de treinamento (por simplicidade, reutilizamos X_test_drifted)
X_new_train, X_new_test, y_new_train, y_new_test = train_test_split(X_test_drifted, y_teste, test_size = 0.3, random_state = 42)

print("\nOtimização de Hiperparâmetros...\n")

# Re-treina o modelo com os novos dados e otimização de hiperparâmetros
modelo_v2 = retreina_modelo(X_treino_scaled, y_treino, X_new_train, y_new_train)

# Função para monitorar o desempenho do modelo
def monitora_performance_modelo(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Avalia o modelo re-treinado
acuracia_pos_retreino = round(monitora_performance_modelo(modelo_v2, X_new_test, y_new_test), 2)

print("\nProjeto 7 - Script 5 - Estratégia de Mitigação de Data Drift")

print("\nAcurácia Após Retreinamento do Modelo com Novos Dados e Otimização de Hiperparâmetros:", acuracia_pos_retreino)

# Salva o modelo treinado e o padronizador
modelo_arquivo = 'modelo_v4.pkl'
scaler_arquivo = 'scaler_v4.pkl'
joblib.dump(modelo_v2, modelo_arquivo)
joblib.dump(scaler, scaler_arquivo)

print(f"\nModelo salvo: {modelo_arquivo}")
print(f"\nPadronizador salvo: {scaler_arquivo}")

print("\nScript 5 Executado com Sucesso!\n")