# Módulo de Retreinamento do Modelo

import subprocess # Usado para criar novos processos
import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Importa funções do módulo versiona_modelo
from versiona_modelo import salva_nova_versao_modelo, lista_versao_modelos

# Função para executar outros scripts (módulos) Python
def executa_modulos(script_name):
    
    # Executa o script Python especificado
    result = subprocess.run(['python', script_name], capture_output = True, text = True)
    
    # Retorna o código de retorno, a saída padrão e a saída de erro
    return result.returncode, result.stdout, result.stderr

# Função para retreinar o modelo
def retreina_modelo(new_data_path, version):
    
    # Lê os novos dados do arquivo CSV
    new_data = pd.read_csv(new_data_path)
    
    # Separa as variáveis independentes (X_new) da variável dependente (y_new)
    X_new = new_data.drop('y', axis = 1)
    y_new = new_data['y']
    
    # Cria uma instância do modelo RandomForestClassifier
    modelo_dsa = RandomForestClassifier(n_estimators = 100, random_state = 42)
    
    # Treina o modelo com os novos dados
    modelo_dsa.fit(X_new, y_new)
    
    # Salva a nova versão do modelo
    salva_nova_versao_modelo(modelo_dsa, version)

# Função para carregar o modelo mais recente
def carrega_modelo_mais_recente():
    
    # Define o diretório onde os modelos estão armazenados
    models_dir = 'modelos/'
    
    # Lista todos os arquivos no diretório que começam com 'modelo_v'
    models = [f for f in os.listdir(models_dir) if f.startswith('modelo_v')]
    
    # Ordena os modelos pela versão e seleciona o mais recente
    modelo_mais_recente = sorted(models, key=lambda x: int(x.split('_v')[1].split('.')[0]))[-1]
    
    # Carrega o modelo mais recente a partir do arquivo
    modelo = joblib.load(f'{models_dir}{modelo_mais_recente}')
    
    return modelo

# Executa o código se o script for executado diretamente
if __name__ == "__main__":

    # Executa o módulo de pré-processamento de dados
    script1 = 'src/preprocessa_dados.py'
    returncode1, stdout1, stderr1 = executa_modulos(script1)
    print(f"\nExecutando {script1}:")
    print(f"Código de retorno: {returncode1}")
    print(f"Saída:\n{stdout1}")
    if stderr1:
        print(f"Erros:\n{stderr1}")
    
    # Verifica a nova versão do modelo
    nova_versao = len(lista_versao_modelos()) + 1
    
    # Retreina o modelo com os novos dados
    retreina_modelo('dados/processados/dados_treino.csv', nova_versao)
    
    # Carrega o modelo mais recente retreinado
    modelo = carrega_modelo_mais_recente()
    
    # Salva o modelo mais recente com o nome final para o deploy
    joblib.dump(modelo, 'modelos/modelo_mais_recente.pkl')

    # Executa o módulo de avaliação do modelo
    script2 = 'src/avalia_modelo.py'
    returncode2, stdout2, stderr2 = executa_modulos(script2)
    print(f"Executando {script2}:")
    print(f"Código de retorno: {returncode2}")
    print(f"Saída:\n{stdout2}")
    if stderr2:
        print(f"Erros:\n{stderr2}")

    print('Módulo de Retreinamento do Modelo Executado Com Sucesso!\n')





