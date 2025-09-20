# Módulo de Versionamento do Modelo
import os
import joblib

# Função para salvar uma nova versão do modelo
def salva_nova_versao_modelo(model, version):
    
    # Define o caminho do arquivo para salvar o modelo
    model_path = f'modelos/modelo_v{version}.pkl'
    
    # Salva o modelo no caminho especificado
    joblib.dump(model, model_path)

# Função para listar as versões dos modelos
def lista_versao_modelos():
    
    # Define o diretório onde os modelos estão armazenados
    models_dir = 'modelos/'
    
    # Lista todos os arquivos no diretório que começam com 'modelo_v'
    models = [f for f in os.listdir(models_dir) if f.startswith('modelo_v')]
    
    # Retorna a lista de modelos encontrados
    return models

# Executa o código se o script for executado diretamente
if __name__ == "__main__":
    
    # Obtém a lista de versões dos modelos
    models = lista_versao_modelos()
    
    # Imprime as versões disponíveis
    print("\nVersões Disponíveis:\n")
    
    # Itera sobre a lista de modelos e imprime cada um
    for model in models:
        print(model)

    print('\nMódulo de Versionamento do Modelo Executado Com Sucesso!\n')



    