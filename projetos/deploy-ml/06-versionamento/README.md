# Projeto 6 - Pipeline de Versionamento, Retreinamento e Deploy de Modelo de Machine Learning

## Instruções para Primeira Execução

1. Navegue até o diretório do projeto

    ```bash
    cd projetos/deploy-ml/06-versionamento
    ```

2. Cria um ambiente virtual para o projeto usando o Python 3.12

    ```bash
    python3.12 -m venv mlvenv
    ```

3. Ativa o ambiente virtual criado

    ```bash
    source mlvenv/bin/activate 
    ```

3. Instala as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Instruções para Execução

1. Pré-Processamento dos dados:
    ```
    python src/preprocessa_dados.py
    ```

2. Treinamento do modelo inicial:
    ```
    python src/treina_modelo.py
    ```

3. Avaliação do modelo:
    ```
    python src/avalia_modelo.py
    ```

4. Versionamento do modelo:
    ```
    python src/versiona_modelo.py
    ```

5. Retreinamento do modelo:
    ```
    python src/retreina_modelo.py
    ```

6. Deploy do modelo:
    ```
    python src/deploy_modelo.py
    ```

7. Usa um cliente Python para fazer uma chamada ao modelo:
    ```
    python src/cliente.py
    ```