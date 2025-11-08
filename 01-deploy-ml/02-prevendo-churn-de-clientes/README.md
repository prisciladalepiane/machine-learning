# Projeto 2 - Prevendo o Churn de Clientes com RandomForest 

Abra o terminal ou prompt de comando, navegue até a pasta com os arquivos e execute o comando abaixo para criar um ambiente virtual:

```bash
conda create --name deployml2 python=3.12
```

Ative o ambiente:

```bash
conda activate deployml2 (ou: source activate deployml2)
```

Instale o pip e as dependências:

```bash
conda install pip
pip install -r requirements.txt 
```

Execute o comando abaixo para acessar o jupyter notebook e treinar o modelo:

```bash
jupyter notebook
```

Execute o comando abaixo para o deploy do modelo:

```bash
streamlit run deploy.py
```

Use os comandos abaixo para desativar o ambiente virtual e remover o ambiente (opcional):

```bash
conda deactivate
conda remove --name deployml2 --all
```


## Sobre o projeto

Este projeto visa desenvolver um modelo preditivo robusto para prever o churn de clientes utilizando o algoritmo _RandomForest_. O projeto abrange desde a concepção do problema até a fase de deploy do modelo. 

Fases do Projeto:

**Concepção do Problema:** Identificação e definição clara do problema de churn de clientes. Análise de como o churn afeta a empresa e quais padrões podem ser observados nos dados históricos.

**Coleta de Dados:** Reunir dados históricos relevantes dos clientes. Usaremos dados fictícios com variáveis que representam informações reais para esse tipo de problema.

**Pré-processamento e Limpeza de Dados:** Limpar e formatar os dados para análise. Isso inclui tratar valores ausentes, remover duplicatas e normalizar os dados.

**Exploração de Dados:** Análise exploratória para entender as tendências, padrões e relações nos dados. Isso ajudará a formular hipóteses para o modelo.

**Modelagem com RandomForest:** Utilização do algoritmo RandomForest para construir um modelo preditivo. O RandomForest foi escolhido pela sua eficácia em lidar com grandes conjuntos de dados e sua habilidade em modelar interações complexas entre variáveis.

**Avaliação do Modelo:** Testar o modelo com um conjunto de dados separado para avaliar sua precisão e eficácia. Ajustes e otimizações serão feitos com base nos resultados.

**Implementação(Deploy):** Desenvolver uma estratégia para implementar o modelo que então será usado com novos dados para entregar as previsões.

**Objetivo Final:** Reduzir a taxa de churn de clientes através de previsões precisas, permitindo que a empresa tome ações proativas. Este projeto é ideal para empresas que buscam entender melhor o comportamento de churn dos seus clientes e querem implementar soluções baseadas em dados para melhorar a retenção de clientes.