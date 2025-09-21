# Módulo de Avaliação do Modelo

import os
import re
import joblib  
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score  


def obtem_modelo_mais_recente(diretorio):
    
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)
    
    # Filtra apenas os arquivos que correspondem ao padrão 'modelo_vX.pkl'
    modelos = [arq for arq in arquivos if re.match(r'modelo_v\d+\.pkl', arq)]
    
    # Ordena os arquivos pela versão (vX)
    modelos.sort(key=lambda x: int(re.search(r'v(\d+)', x).group(1)), reverse = True)
    
    # Retorna o nome do modelo mais recente
    return os.path.join(diretorio, modelos[0]) if modelos else None

# Função para avaliar o modelo
def avalia_modelo():

    # Lê os dados de teste do arquivo CSV
    dados_teste = pd.read_csv('dados/processados/dados_teste.csv')
    
    # Separa as variáveis independentes (X_teste) da variável dependente (y_teste)
    X_teste = dados_teste.drop('y', axis=1)
    y_teste = dados_teste['y']
    
    # Obtém o caminho do modelo mais recente
    caminho_modelo = obtem_modelo_mais_recente('modelos')

    if caminho_modelo:

        print(f'\nAvaliando o Modelo: {caminho_modelo}')

        # Carrega o modelo treinado a partir do arquivo
        modelo_dsa = joblib.load(caminho_modelo)
    
        # Faz previsões com o modelo usando os dados de teste
        y_pred = modelo_dsa.predict(X_teste)
    
        # Calcula a acurácia das previsões
        accuracy = accuracy_score(y_teste, y_pred)
    
        # Calcula a precisão das previsões
        precision = precision_score(y_teste, y_pred)
    
        # Calcula o recall das previsões
        recall = recall_score(y_teste, y_pred)
    
        # Imprime a acurácia
        print(f'\nAcurácia: {accuracy}')
    
        # Imprime a precisão
        print(f'Precisão: {precision}')
    
        # Imprime o recall
        print(f'Recall: {recall}\n')

        print('\nMódulo de Avaliação do Modelo Executado Com Sucesso!\n')
    else:
        print('\nNenhum modelo encontrado no diretório especificado.\n')

# Executa a função se o script for executado diretamente
if __name__ == "__main__":
    avalia_modelo()




