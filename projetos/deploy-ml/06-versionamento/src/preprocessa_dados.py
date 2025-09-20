# Módulo de Pré-Processamento de Dados

# Importa a biblioteca pandas para manipulação de dados
import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split  


# Função para processar dados
def processa_dados():
    
    # Lê os dados do arquivo CSV
    df = pd.read_csv('dados/originais/dataset.csv')
    
    # Separa as variáveis independentes (X) da variável dependente (y)
    X = df.drop('y', axis = 1)
    y = df['y']
    
    # Divide os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    
    # Combina os dados de treino em um único DataFrame
    train_data = pd.concat([X_train, y_train], axis = 1)
    
    # Combina os dados de teste em um único DataFrame
    test_data = pd.concat([X_test, y_test], axis = 1)
    
    # Salva os dados de treino em um arquivo CSV
    train_data.to_csv('dados/processados/dados_treino.csv', index = False)
    
    # Salva os dados de teste em um arquivo CSV
    test_data.to_csv('dados/processados/dados_teste.csv', index = False)

# Executa as funções se o script for executado diretamente
if __name__ == "__main__":
    processa_dados()
    print('\nMódulo de Pré-Processamento de Dados Executado Com Sucesso!\n')




