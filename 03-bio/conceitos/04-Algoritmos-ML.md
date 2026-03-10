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
