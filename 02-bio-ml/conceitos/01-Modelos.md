# Modelagem Preditiva

A modelagem preditiva é uma técnica de análise de dados que utiliza modelos estatísticos e algoritmos de aprendizado de máquina para prever resultados futuros com base em dados históricos. O objetivo é criar um modelo que possa prever tendências e comportamentos, facilitando a tomada de decisões proativas em diversas áreas, como negócios, saúde, engenharia, ciências sociais e mais.

### Etapas Fundamentais Da Modelagem Preditiva:

1. <u> **Coleta de Dados:**</u>  Inicialmente, é necessário coletar uma grande quantidade de dados históricos relevantes para o problema.

2. <u> **Preparação dos Dados:** </u> Os dados coletados precisam ser limpos e transformados para garantir que estejam em um formato utilizável pelos modelos.

3. <u> **Divisão dos Dados:**</u> Os dados são geralmente divididos em conjuntos de treinamento e teste. O conjunto de treinamento é usado para desenvolver o modelo, enquanto o conjunto de teste ajuda a avaliar sua eficácia.

4. <u> **Seleção e Treinamento do Modelo:**</u> Escolhe-se um modelo estatístico ou de aprendizado de máquina adequado ao problema e treina-se esse modelo usando os dados de treinamento.

5. <u> **Validação do Modelo:** </u>O modelo é validado e ajustado para melhorar a precisão das previsões, utilizando técnicas como a validação cruzada.

6. <u> **Implementação e Monitoramento:** </u> Após ser validado, o modelo é implementado para fazer previsões em novos dados. O modelo também é monitorado e atualizado conforme necessário para manter sua relevância e precisão ao longo do tempo.

> Os modelos preditivos são usados em uma variedade de aplicações, incluindo previsão de demanda de produtos, identificação de riscos de crédito, otimização de operações logísticas, detecção de fraudes e personalização de recomendações em serviços de streaming. A modelagem preditiva tornou-se uma ferramenta essencial para muitas organizações que buscam ganhar vantagem competitiva ao prever tendências futuras de forma mais precisa e eficaz.

## Aprendizado Supervisionado e Não Supervisionado

O aprendizado de máquina pode ser dividido principalmente em duas categorias: aprendizado supervisionado e aprendizado não supervisionado. Cada um desses tipos tem suas próprias características e aplicações. Vamos explorar cada um deles:

### <u> Aprendizado Supervisionado </u>
No aprendizado supervisionado, os modelos são treinados usando um conjunto de dados que já contém as respostas corretas, conhecidas como "labels" ou "etiquetas". O objetivo é que o modelo aprenda a mapear as entradas para as saídas corretas.

Esse tipo de aprendizado é chamado de "supervisionado" porque o processo de treinamento é orientado pelas respostas corretas. Após o treinamento, o modelo é capaz de prever a saída para novos dados que não foram vistos anteriormente.

Exemplos comuns de aprendizado supervisionado incluem:

- **Classificação**: Prever uma categoria (por exemplo, se um e-mail é spam ou não spam).

- **Regressão**: Prever um valor numérico contínuo (por exemplo, o preço de uma casa com base em suas características).
### <u> Aprendizado Não Supervisionado </u>

No aprendizado não supervisionado, os dados de entrada não vêm com etiquetas correspondentes. O modelo tenta aprender a estrutura ou padrões dos dados sem qualquer orientação explícita sobre o resultado correto.

O aprendizado não supervisionado é útil para explorar a estrutura dos dados ou para encontrar agrupamentos naturais.

Exemplos comuns incluem:

- **Agrupamento (Clustering)**: Agrupar um conjunto de objetos de modo que os objetos no mesmo grupo (ou cluster) sejam mais semelhantes entre si do que com os de outros grupos. Exemplo: segmentação de clientes em marketing.

- **Redução de dimensionalidade:** Reduzir o número de variáveis aleatórias sob consideração, útil para visualização de dados ou para simplificar modelos. Exemplo: análise de componente principal (PCA).

### Diferenças Chave
- **Rótulos de dados**: No supervisionado, os rótulos são necessários e fundamentais para o treinamento. No não supervisionado não há rótulos e o modelo trabalha para identificar padrões.

- **Complexidade e aplicabilidade**: O aprendizado supervisionado geralmente requer uma preparação de dados mais complexa, mas é mais direto para avaliar. O aprendizado não supervisionado pode ser mais difícil de interpretar e aplicar, mas é valioso para ganhar insights dos dados.

- **Tipos de problemas**: O aprendizado supervisionado é comumente aplicado em previsões e classificações precisas, enquanto o não supervisionado é usado para exploração de dados e descoberta de informações ocultas.

## Modelos de Classificação

Os modelos de classificação estão entre os mais comuns algoritmos no aprendizado de máquina supervisionado, utilizados para prever a categoria ou classe de um dado elemento.

Esses modelos são treinados com dados que já possuem etiquetas de classe, permitindo que o modelo aprenda a associar as características dos dados às suas respectivas categorias. Depois de treinado, o modelo pode então classificar novos dados em uma das categorias conhecidas.

Apresentamos a seguir alguns dos modelos de classificação mais comuns e amplamente utilizados:

### 1. Regressão Logística

Apesar do nome, é um modelo de classificação que estima a probabilidade de uma variável binária (duas categorias) baseada em uma ou mais variáveis independentes. É utilizado principalmente para problemas de classificação binária.

Exemplo de uso: Prever se um cliente fará ou não a renovação de uma assinatura.

### 2. Árvores de Decisão

Utiliza uma estrutura de árvore onde cada nó interno representa um "teste" em um atributo, cada ramificação representa o resultado do teste e cada nó folha representa uma etiqueta de classe. Pode ser usado para classificação e regressão.

Exemplo de uso: Diagnosticar pacientes com base em características clínicas.

### 3. Florestas Aleatórias (Random Forests)

Um método de ensemble que constrói múltiplas árvores de decisão durante o treinamento e utiliza a média para melhorar a precisão preditiva e controlar o overfitting.

Exemplo de uso: Classificar tipos de plantas com base em medições morfológicas.

### 4. Máquinas de Vetores de Suporte (Support Vector Machines, SVM)

Busca a melhor fronteira de decisão, chamada de hiperplano, que separa diferentes classes com a maior margem possível. É eficaz em espaços de alta dimensão.

Exemplo de uso: Classificação de imagens, reconhecimento de padrões em biologia computacional.

### 5. Redes Neurais Artificiais

Sistemas inspirados no cérebro humano que são capazes de aprender a partir de grandes quantidades de dados. São particularmente poderosas para lidar com dados complexos e não lineares.

Exemplo de uso: Reconhecimento de fala, classificação de textos.

### 6. k-Vizinhos Mais Próximos (k-Nearest Neighbors, k-NN)

Classifica novos casos com base em uma similaridade de características com casos conhecidos, considerando os 'k' vizinhos mais próximos.

Exemplo de uso: Recomendação de produtos com base nas preferências de usuários similares.

### 7. Naive Bayes

Um classificador probabilístico baseado no teorema de Bayes com a suposição de independência entre os preditores. Simples, mas surpreendentemente eficaz.

Exemplo de uso: Filtragem de spam em e-mails.


## Modelos de Regressão

Os modelos de regressão são uma classe de algoritmos de aprendizado de máquina supervisionado utilizados para prever valores contínuos. 

A seguir apresentamos uma visão geral de alguns dos modelos de regressão mais comuns e suas aplicações:

### 1. Regressão Linear Simples

Este modelo assume uma relação linear entre a variável dependente e uma variável independente. A relação é modelada através de uma linha reta (Y = a + bX).

Exemplo de uso: Prever o preço de venda de uma casa com base na sua área total.

### 2. Regressão Linear Múltipla

Extensão da regressão linear simples, onde diversas variáveis independentes são usadas para prever a variável dependente. 

Exemplo de uso: Estimar o consumo de combustível de um veículo com base em atributos como peso, potência do motor e tipo de combustível.

### 3. Regressão Polinomial

Uma forma de regressão linear onde a relação entre a variável independente e a variável dependente é modelada como um polinômio de grau n. É útil para modelar relações não lineares.

Exemplo de uso: Modelar a progressão de doenças ao longo do tempo com mudanças não lineares.

### 4. Regressão Ridge (Ridge Regression)

Um método que introduz o termo de regularização (L2) no modelo de regressão linear para prevenir overfitting, o que é especialmente útil quando há multicolinearidade nos dados ou quando o número de parâmetros é quase igual ao número de observações.

Exemplo de uso: Prever rendimentos baseados em dados demográficos em estudos de economia.

### 5. Regressão Lasso

Semelhante à regressão Ridge, mas usa a regularização L1, que tem a capacidade de reduzir os coeficientes de algumas variáveis preditoras exatamente a zero. Isso proporciona uma seleção automática de características e modelos mais esparsos.

Exemplo de uso: Seleção de variáveis em modelagem genética para identificar genes significativos.

### 6. Regressão Elastic Net

Combina as penalidades das normas L1 e L2 da regressão Lasso e Ridge. É útil quando existem várias características correlacionadas.

Exemplo de uso: Previsão de risco de crédito onde muitos atributos podem ser intercorrelacionados.

### 7. Regressão Quantílica

Diferente da regressão ordinária que estima a média condicional, a regressão quantílica visa estimar os quantis (por exemplo, a mediana) da variável dependente, proporcionando uma visão mais completa da possível distribuição dos dados de resposta.

Exemplo de uso: Economia para prever diferentes percentis de renda.

### 8. Modelos de Regressão Generalizados (Generalized Linear Models, GLM)

Generaliza a regressão linear para permitir que a variável dependente tenha uma distribuição de erro que não seja necessariamente uma distribuição normal, incluindo distribuições como binomial, Poisson, e outras.

Exemplo de uso: Modelar o número de sinistros de seguro, que tipicamente segue uma distribuição Poisson.
Cada um desses modelos tem suas próprias forças e limitações, e a escolha do modelo apropriado depende da natureza dos dados, dos objetivos do estudo, e das suposições subjacentes que se pode razoavelmente fazer sobre a distribuição dos dados e a relação entre as variáveis.


# Regressão Logistica

A Regressão Logística é um método estatístico utilizado para prever a probabilidade de uma variável dependente categórica, geralmente binária, onde os resultados são classificados em duas categorias, como "sucesso/falha" ou "0/1".

Este modelo utiliza a função logística (ou sigmóide) para modelar a probabilidade de que a variável dependente pertença a uma das categorias, com base em uma ou mais variáveis independentes (preditoras).

A função sigmóide transforma qualquer valor de entrada real para um valor de saída entre 0 e 1, o que é interpretado como a probabilidade de a variável dependente pertencer à categoria "1".

A regressão logística calcula os pesos (coeficientes) das variáveis independentes de forma a maximizar a verossimilhança dos dados observados, geralmente através de métodos como o da máxima verossimilhança.

No contexto da regressão logística, as probabilidades modeladas são convertidas em previsões binárias com base em um limiar de decisão, comumente 0,5.

Se a probabilidade prevista for maior que o limiar, a previsão é categorizada como "1"; caso contrário, é categorizada como "0".

Essa abordagem permite que o modelo lide com casos em que as categorias não são igualmente prováveis e ajuste a importância das variáveis preditoras na determinação do resultado.

A regressão logística é amplamente utilizada em diversas áreas, como:

* Medicina, para prever a probabilidade de uma doença com base em fatores de risco;

* Marketing, para prever a probabilidade de um cliente comprar um produto;

* Setor Financeiro, para avaliar o risco de inadimplência de um empréstimo, devido à sua flexibilidade e interpretabilidade.

# Naive Bayes

https://scikit-learn.org/stable/modules/naive_bayes.html

O modelo Naive Bayes é um classificador probabilístico fundamentado no Teorema de Bayes, que opera sob a suposição "ingênua" de independência entre os preditores.

Em outras palavras, assume que a presença de uma característica particular em uma classe é independente da presença de qualquer outra característica. Essa suposição simplifica os cálculos, permitindo que o modelo seja treinado de maneira eficiente mesmo em grandes conjuntos de dados.

O modelo é utilizado para tarefas de classificação, onde o objetivo é prever a probabilidade de uma observação pertencer a uma das classes.

A base do Naive Bayes é o cálculo das probabilidades condicionais de cada classe dadas as características observadas, utilizando o Teorema de Bayes para atualizar as probabilidades a priori das classes com base nas evidências fornecidas pelos dados.

Naive Bayes é particularmente popular em aplicações de classificação de texto, como filtragem de spam e análise de sentimentos, devido à sua simplicidade, eficiência e eficácia nessas tarefas.

O modelo calcula a probabilidade de um documento pertencer a uma classe específica (por exemplo, "spam" ou "não spam") com base na frequência das palavras nele contidas.

Apesar de sua suposição simplista de independência, Naive Bayes pode oferecer um desempenho surpreendentemente bom em muitos casos práticos. Isso se deve, em parte, à sua habilidade de lidar com a alta dimensionalidade dos dados de entrada, como é típico em problemas de classificação de texto, onde o número de características (palavras ou termos) pode ser extremamente grande.

Além disso, Naive Bayes é fácil de implementar e requer uma quantidade relativamente pequena de dados de treinamento para estimar os parâmetros necessários para a classificação.

## Modelagem Preditiva Probabilística

A modelagem preditiva probabilística com Naive Bayes é uma abordagem estatística para classificação e previsão que se baseia no Teorema de Bayes. Ela é chamada de "naive" (ingênua) porque faz uma suposição fundamental de independência entre as características (ou features) dos dados, considerando que a presença (ou ausência) de uma característica particular é independente da presença (ou ausência) de outras características, dado o resultado da variável alvo. Essa suposição simplifica os cálculos e, apesar de sua simplicidade, modelos Naive Bayes muitas vezes funcionam surpreendentemente bem em muitas aplicações práticas, especialmente em classificação de texto, filtragem de spam, diagnóstico médico e detecção de sentimentos.

O núcleo da modelagem preditiva probabilística com Naive Bayes é o Teorema de Bayes, que é uma maneira de calcular a probabilidade posterior P(Y∣X) de uma classe Y dado um vetor de características X.

# XGBoost (Xtreme Gradient Boosting Classifier)

O XGBoost (Xtreme Gradient Boosting) é uma implementação avançada do algoritmo gradiente boosting que tem ganhado popularidade devido à sua eficiência e eficácia em competições de Ciência de Dados e aplicações práticas.

O princípio por trás do XGBoost é a otimização sequencial de árvores de decisão, onde cada nova árvore é construída para corrigir os erros residuais das árvores anteriores.

Diferentemente de outros métodos de boosting, o XGBoost utiliza um modelo formal de otimização para encontrar a melhor forma de combinar as previsões das árvores, minimizando uma função de perda que quantifica a diferença entre as previsões e os verdadeiros valores.

Além disso, incorpora técnicas de regularização (L1 e L2) para controlar a complexidade do modelo, ajudando a prevenir o overfitting e melhorando a capacidade de generalização do modelo.

O XGBoost é notável por sua velocidade e desempenho, atribuídos a várias otimizações na construção do modelo e na utilização de recursos computacionais.

Por exemplo: emprega técnicas como a "quantização de características" para reduzir o uso de memória e melhorar a eficiência do treinamento, e o "pruning" de árvores baseado em ganho, cortando ramos que adicionam pouco valor às previsões.

Ele também suporta computação paralela e distribuída, o que permite que lide eficientemente com grandes volumes de dados.

O XGBoost é flexível, podendo ser aplicado a tarefas de regressão, classificação (binária e multiclasse), ranking e muitas outras.

Sua capacidade de lidar com dados esparsos e ausentes, juntamente com a extensiva gama de parâmetros ajustáveis, faz do XGBoost uma ferramenta poderosa e versátil para modelagem preditiva, sendo amplamente adotado em indústrias e pesquisa.
