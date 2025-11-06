#  Construção de Feature Store e Engenharia de Atributos no Pipeline de Machine Learning

## Execute os comandos abaixo no terminal 

Ir para a pasta do projeto

```bash
cd 01-deploy-ml/05-construcao-feature-store/
```

Cria um ambiente virtual para o projeto usando o Python 3

```bash
python3.12 -m venv mlvenv 
```

Ativa o ambiente virtual criado
```bash
source mlvenv/bin/activate 
```

Instala todas as dependências listadas no arquivo requirements.txt no ambiente virtual
```bash
pip install -r requirements.txt
```

Associa o ambiente virtual ao código fonte do nosso pipeline
Quando você executa pip install -e . em um diretório que contém um arquivo setup.py ou pyproject.toml, o pip instala o pacote definido nesse diretório. A instalação no modo editável cria apenas uma ligação entre o seu ambiente de desenvolvimento (por exemplo, o ambiente virtual) e o diretório do código-fonte. Isso significa que quaisquer alterações feitas no código-fonte serão refletidas imediatamente no ambiente onde o pacote está instalado, sem a necessidade de reinstalação.

```bash
pip install -e .
```

Reativa o ambiente virtual

```bash
source mlvenv/bin/activate
```

Executa o script Python localizado em src/pipeline.py dentro do ambiente virtual

```bash
python src/pipeline.py
```

Desativa o ambiente virtual, retornando ao ambiente global do sistema

```bash
deactivate
```


