# O Que é Análise de Componentes Principais?A Análise de Componentes Principais (PCA, do inglês Principal Component Analysis) é uma técnica de redução de dimensionalidade amplamente utilizada em Ciência de Dados e Machine Learning.

O objetivo principal com PCA é transformar um conjunto de variáveis possivelmente correlacionadas em um conjunto de valores de variáveis linearmente não correlacionadas, chamadas de componentes principais. Este processo é realizado mantendo-se o máximo possível da variabilidade presente no conjunto de dados original.

O funcionamento do algoritmo PCA pode ser descrito da seguinte maneira:

**Normalização dos Dados**: Inicialmente, os dados são normalmente padronizados, especialmente se as variáveis têm unidades de medida diferentes. Isso envolve subtrair a média e dividir pelo desvio padrão de cada variável.

**Cálculo da Matriz de Covariância:** A matriz de covariância é calculada para entender como as variáveis no conjunto de dados estão variando em relação umas às outras.

**Determinação de Autovalores e Autovetores**: A partir da matriz de covariância, são calculados os autovalores e autovetores. Os autovalores indicam a quantidade de variância que pode ser atribuída a cada autovetor (ou componente principal).

**Seleção dos Componentes Principais**: Os componentes principais são selecionados com base na quantidade de variância que eles representam. Geralmente, escolhe-se um número de componentes que somam a maior parte da variância total, o que permite uma representação simplificada do conjunto de dados original.

**Transformação dos Dados:** Por fim, os dados originais são transformados em um novo conjunto de dados com base nos componentes principais selecionados.

PCA é especialmente útil em situações com dados de alta dimensionalidade (com muitas variáveis), onde a visualização e análise se tornam complexas.

Ao reduzir o número de variáveis, PCA facilita a visualização dos dados, a descoberta de padrões importantes e a redução do ruído, mantendo ao mesmo tempo as características mais significativas do conjunto de dados. Isso a torna uma ferramenta valiosa para a análise exploratória de dados, pré-processamento para algoritmos de Machine Learning, compressão de dados, entre outras aplicações.

#### Por Que Precisamos Reduzir a Dimensionalidade dos Dados?

Normalmente, os dados contêm dezenas, centenas ou mesmo milhares de recursos (atributos). Ou seja, os dados podem ter alta dimensionalidade. 

Trabalhar diretamente com dados de alta dimensionalidade apresenta algumas dificuldades: é difícil analisar, a interpretação é difícil, a visualização é quase impossível e (do ponto de vista prático) o armazenamento dos vetores de dados pode ser custoso computacionalmente. 

Dados de alta dimensionalidade são muitas vezes incompletos, ou seja, muitas dimensões são redundantes e podem ser explicadas por uma combinação de outras dimensões. 

Reduzimos a dimensionalidade dos dados para diminuir a complexidade dos dados. Quanto menos recursos, menor é a complexidade, e mais fácil para analisar, visualizar e compreender os dados.

Redução de dimensionalidade nos permite trabalhar com uma representação mais compacta dos dados, idealmente sem perder informações. Nós podemos pensar redução da dimensionalidade como técnica de compressão, semelhante ao jpeg ou mp3, que são algoritmos de compactação para imagens e música, respectivamente.

#### Definindo PCA - Principal Component Analysis

A análise de componentes principais (PCA) é uma técnica usada para enfatizar a variação e detectar padrões fortes em um conjunto de dados. Nós a usamos para entender melhor os dados.

Nas tarefas de análise de dados do mundo real, analisamos dados complexos, ou seja, dados multidimensionais. Plotamos os dados e encontramos vários padrões ou os usamos para treinar modelos de aprendizado de máquina. 

À medida que as dimensões dos dados aumentam, também aumenta a dificuldade de visualizá-los e executar cálculos. Ao reduzir as dimensões dos dados removemos dimensões redundantes e mantemos apenas as dimensões mais importantes.

PCA é a principal técnica de redução de dimensionalidade, sendo normalmente classificado como algoritmo de aprendizagem não supervisionado.

#### Quando Devo Usar PCA?

Para decidir se deve usar ou não o PCA, você deve responder "sim" para as 5 perguntas abaixo:

* 1- Você tem um dataset de alta dimensionalidade?
* 2- Deseja reduzir o número de variáveis, mas não consegue identificar variáveis para remover completamente?
* 3- Deseja garantir que suas variáveis sejam independentes umas das outras?
* 4- Você se sente à vontade para tornar suas variáveis independentes um pouco menos interpretáveis?
* 5- Está disposto a perder uma parte da informação (variação) contida nos dados?

Se você respondeu "sim" às 5 perguntas, o PCA é uma boa alternativa. 

#### Como o PCA Funciona?

O PCA se baseia nos conceitos de Matriz de Variância e Covariância.

* Variância: É uma medida da variabilidade dos dados, ou seja, simplesmente mede como os dados estão espalhados. Matematicamente é o desvio quadrado médio da pontuação média. 

* Covariância: É uma medida da extensão em que os elementos correspondentes de dois conjuntos de dados ordenados se movem na mesma direção. A fórmula é mostrada abaixo, indicada por cov(x, y) como a covariância de x e y. Onde, xi é o valor de x na i-ésima dimensão.

Uma maneira de definir a covariância é como dois conjuntos de dados estão inter-relacionados.

No algoritmo PCA, precisamos calcular uma matriz que resume como todas as nossas variáveis se relacionam.

Em seguida, dividimos essa matriz em dois componentes separados: direção e magnitude. Podemos então entender as “direções” de nossos dados e sua “magnitude” (ou quão “importante” cada direção é). 


https://ieeexplore.ieee.org/document/7005973