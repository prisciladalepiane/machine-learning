# Portifólio de Machine Learning e Data Science

Repositório dedicado a estudos, anotações e projetos práticos em Data Science e Machine Learning. 

## 📂 Desenvolvimento e Deploy de Modelos de Machine Learning
Projetos voltados ao ciclo completo de criação e entrega de modelos de machine learning.

📘 [Conceitos teóricos e explicações](01-deploy-ml/conceitos)

### 1 - Modelo de Classificação para área de Logística

Este projeto demonstra a construção e o deploy de um modelo de Machine Learning aplicado à logística, com o objetivo de prever o tipo de produto eletrônico contido em uma embalagem com base em duas variáveis: peso e tipo de embalagem. Utilizando a biblioteca `scikit-learn`, o modelo foi desenvolvido com o algoritmo **Decision Tree Classifier,** que aprende a relacionar essas variáveis para identificar o produto mais provável. Após o treinamento e avaliação do modelo (com métricas como acurácia e relatório de classificação) o sistema foi integrado em uma aplicação web desenvolvida com `flask`, permitindo realizar previsões em tempo real a partir de um formulário interativo. O projeto simula um cenário logístico real, onde a previsão automática do conteúdo das embalagens pode otimizar o manuseio de produtos e reduzir erros operacionais.

📁 [01-deploy-ml/01-modelo-ml-logistica](01-deploy-ml/01-modelo-ml-logistica)

### 2 - Prevendo Churn de clientes

O projeto utiliza o algoritmo de classificação **Random Forest**, implementado com a biblioteca `scikit-learn`, para prever o churn de clientes. Na primeira etapa, os dados são explorados e pré-processados, e diferentes configurações do modelo são testadas com base em métricas de desempenho, como acurácia, incluindo a otimização de hiperparâmetros para aprimorar os resultados. Na segunda etapa, o modelo final é salvo com `joblib` e integrado em uma aplicação interativa desenvolvida com `streamlit`, permitindo realizar previsões de forma prática e visual, simulando um ambiente real de deploy de modelo de Machine Learning.

📁 [01-deploy-ml/02-prevendo-churn-de-clientes](01-deploy-ml/02-prevendo-churn-de-clientes)

### 3 -  Projeto na Nuven AWS

O projeto consistiu na criação e implantação de modelos de Machine Learning (**Regressão Logística, Random Forest e SVM**) para prever a admissão de estudantes com base em variáveis como notas e QI. O processo incluiu pré-processamento, padronização dos dados, divisão em treino e teste, avaliação por métricas de desempenho (Acurácia, AUC, F1-score) e comparação de algoritmos.
O modelo foi posteriormente preparado para deploy na AWS, integrando o fluxo de previsão a um ambiente de nuvem para uso em aplicações educacionais.

📁 [01-deploy-ml/03-modelo-ml-nuven-aws-escola](01-deploy-ml/03-modelo-ml-nuven-aws-escola)

### 4 - Deploy de API para Geração de Texto a partir de Imagens com LLM

Este projeto desenvolve e implanta uma API de Machine Learning capaz de gerar respostas em texto a partir de imagens, utilizando um Modelo de Linguagem de Grande Escala (LLM) multimodal. O modelo empregado, [dandelin/vilt-b32-finetuned-vqa](dandelin/vilt-b32-finetuned-vqa), proveniente do _Hugging Face Hub_, é especializado em Visual Question Answering (VQA), permitindo que o sistema interprete imagens e responda perguntas sobre o conteúdo visual.

A API foi construída com `FastAPI` e empacotada em um container Docker, garantindo portabilidade e execução independente de plataforma, seja local ou em nuvem. O fluxo inclui um cliente Python que envia uma imagem e uma pergunta à API, e recebe como resposta o texto gerado pelo modelo. O projeto demonstra o processo completo de integração entre modelos de IA multimodais, APIs REST e containers, simulando um ambiente real de deploy de aplicações de visão e linguagem natural.

📁 [01-deploy-ml/04-api-texto-img](01-deploy-ml/04-api-texto-img)

### 5 - Construção de feature-store e Aplicação de Engenharia de Atributos

Este projeto implementa um pipeline completo de Machine Learning, desde a geração sintética de dados e criação de uma Feature Store até o treinamento, avaliação e salvamento automatizado do modelo e suas previsões. O fluxo é composto por módulos independentes responsáveis por cada etapa: criação da **feature store**, exploração e **visualização dos dados**, **engenharia de atributos**, treinamento de modelo (com Random Forest), e salvamento de artefatos e métricas.

O objetivo é demonstrar como estruturar um pipeline reproduzível e escalável, aplicando boas práticas de MLOps, como modularização, versionamento e persistência de resultados. Todo o processo é executado por meio do script pipeline.py, que automatiza as etapas e registra o desempenho do modelo em formato JSON.

📁 [01-deploy-ml/05-construcao-feature-store](01-deploy-ml/05-construcao-feature-store)

### 6 - Pipeline de Versionamento, Retreinamento e Deploy

O projeto implementa um fluxo completo de MLOps em Python, desde o pré-processamento e treinamento inicial de um modelo até seu deploy via API Flask. O pipeline automatiza etapas como **validação cruzada**, **avaliação de métricas**, **versionamento de modelos** e retreinamento com novos dados, garantindo reprodutibilidade e rastreabilidade. Cada nova versão é salva e avaliada antes de ser promovida a produção, enquanto o modelo mais recente pode ser consumido por requisições HTTP, simulando um ambiente real de manutenção e atualização contínua de modelos de Machine Learning.

📁 [01-deploy-ml/06-versionamento](01-deploy-ml/06-versionamento)

### 7 - Monitoramento de Data Driften

O Projeto tem como foco o desenvolvimento de um sistema automatizado para detectar e mitigar mudanças no comportamento dos dados e na performance dos modelos de Machine Learning ao longo do tempo. Utilizando o dataset de vinhos da UCI Machine Learning Repository, o projeto simula cenários de _Data Drift_ e _Model Drift_, monitorando a degradação da acurácia e aplicando estratégias de mitigação como retreinamento com novos dados, otimização de hiperparâmetros e mudança de algoritmos. São implementados diferentes estágios de resposta, desde o reuso do modelo inicial até a combinação de modelos com o `GradientBoostingClassif`.

📁 [01-deploy-ml/07-monitorar-data-driften](01-deploy-ml/07-monitorar-data-driften)


### 8 - Deploy de Modelo de Classificação através de API em Linguagem Rust

Projeto para construir, treinar e fazer o deploy de um modelo de classificação em Rust. Deploy feito através de uma API com endpoint de previsão usando o modelo treinado. O pipeline permite que o modelo seja treinado com os dados históricos imediatamente antes de ser usado no deploy com novos dados, a cada execução.

📁 [01-deploy-ml/08-deploy-rust](01-deploy-ml/08-deploy-rust)


-----------------------------------------------------------------------------

# 🔗 Outros Projetos

Lista de repositórios externos.

## ♾️ MLOPs
- [mlops](https://github.com/prisciladalepiane/mlops)

## 🧠 Deep Learning
- [deep-learning](https://github.com/prisciladalepiane/deep-learning): Estudos e projetos com redes neurais, fundamentos de arquiteturas profundas, treinamento, avaliação e experimentos aplicados.

## 🔬 Ciência de Dados com Python

- [data_sci_py](https://github.com/prisciladalepiane/data_sci_py): Scripts e notebooks de estudos com Python, Pandas, Matplotlib, Scikit-Learn, etc.

## 🧪 Shiny e TCT

- [app_shiny_tct](https://github.com/prisciladalepiane/app_shiny_tct): Aplicativo Shiny para visualização de resultados em Teoria Clássica dos Testes (TCT) usando dados educacionais.

## 🗃️ Banco de Dados

- [banco_de_dados](https://github.com/prisciladalepiane/banco_de_dados): Modelagem e consultas SQL com foco em bancos relacionais. Inclui scripts de criação de tabelas e casos de uso.

## 📚 Artigo Teoria de Resposta ao Item

- [artigo-tri-latex](https://github.com/prisciladalepiane/artigo-tri-latex): Repositório da monografia sobre TRI, com código LaTeX e referências.

---

**Priscila Gonçalves Dalepiane**
Estatística | Engenharia de Software | Pós em Machine Learning e MLOps  

[LinkedIn](https://www.linkedin.com/in/priscila-gon%C3%A7alves-dalepiane-947b65b2/) | [Rpubs](https://rpubs.com/prisciladalepiane) | [GitHub](https://github.com/prisciladalepiane)
