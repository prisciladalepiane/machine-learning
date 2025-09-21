# O Que é Análise de Componentes Principais?

https://ieeexplore.ieee.org/document/7005973

A Análise de Componentes Principais (PCA, do inglês Principal Component Analysis) é uma técnica de redução de dimensionalidade amplamente utilizada em Ciência de Dados e Machine Learning.

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

#### Descrição do Algoritmo PCA

Abaixo temos a descrição do algoritmo PCA (links de referência estão ao final do capítulo). Antes de iniciar, você deve considerar dados tabulares organizados com linhas e colunas.

O algoritmo que será descrito é basicamente o que acontece quando você executa estas 3 linhas de código em Python:

```python
# Aplicando PCA
from sklearn.decomposition import PCA
pca = PCA()
X_pca = pca.fit_transform(X)
```

1. Seus dados de entrada devem estar divididos em uma ou mais colunas de entrada (representado por X) e uma ou mais colunas de saída (representado por Y). Aplicamos o PCA em X. Se os seus dados tiverem a variável de saída Y, ela não entra no cálculo do PCA. Nesse caso você reduziria a dimensionalidade de X para então tentar prever Y. PCA trabalha no X.

---

2. Pegue a matriz de variáveis independentes X e, para cada coluna, subtraia a média dessa coluna de cada entrada (Isso garante que cada coluna tenha uma média de zero).

---

3. Decida se deve ou não padronizar. Dadas as colunas de X, os recursos com variação mais alta são mais importantes do que os recursos com variação menor ou a importância dos recursos é independente da variação? (Nesse caso, importância significa quão bem esse recurso prevê Y). Se a importância dos recursos for independente da variação dos recursos, divida cada observação em uma coluna pelo desvio padrão dessa coluna (Isso, combinado com a etapa 2, padroniza cada coluna de X para garantir que cada coluna tenha média zero e desvio padrão 1). Chame a matriz centralizada (e possivelmente padronizada) Z. PCA espera receber os dados padronizados.

---

4. Pegue a matriz Z, transponha-a e multiplique a matriz transposta por Z (Escrevendo isso matematicamente, teríamos ZᵀZ.) A matriz resultante é a matriz de covariância de Z.

---

5. (Este é provavelmente o passo mais difícil a seguir) Calcule os autovetores e seus autovalores correspondentes de Z. A composição automática de ZᵀZ é onde decompomos ZᵀZ em PDP⁻¹, onde P é a matriz de autovetores e D é a matriz diagonal com autovalores na diagonal e valores de zero em qualquer outro lugar. Os autovalores na diagonal de D serão associados à coluna correspondente em P - ou seja, o primeiro elemento de D é λ₁ e o autovetor correspondente é a primeira coluna de P. Isso vale para todos os elementos em D e seus autovetores correspondentes em P. Sempre poderemos calcular o PDP⁻¹ dessa maneira. 

---

6. Pegue os autovalores λ₁, λ₂,…, λn e classifique-os do maior para o menor. Ao fazer isso, classifique os autovetores em P de acordo (Por exemplo, se λ₂ é o maior autovalor, pegue a segunda coluna de P e coloque-a na posição da primeira coluna). Dependendo do pacote de computação, isso pode ser feito automaticamente. Chame essa matriz classificada de autovetores P* (As colunas de P* devem ser as mesmas que as de P, mas talvez em uma ordem diferente). Observe que esses autovetores são independentes um do outro.

---

7. Calcular Z* = ZP*. Essa nova matriz, Z*, é uma versão centralizada/padronizada de X, mas agora cada observação é uma combinação das variáveis originais, onde os pesos são determinados pelo autovetor. Como um bônus, porque nossos autovetores em P* são independentes um do outro, cada coluna de Z* também é independente uma da outra!

---

8. Finalmente, precisamos determinar quantos recursos (componentes principais) manter versus quantos deixar de fora. Existem três métodos comuns para determinar isso, discutidos abaixo:


* Método 1: Selecionamos arbitrariamente quantas dimensões queremos manter. Talvez eu queira representar visualmente os dados em duas dimensões, para que eu possa manter apenas duas características. Isso depende do caso de uso e não existe uma regra rígida para quantos recursos devo escolher.


* Método 2: Calculamos a proporção de variação explicada para cada recurso, escolhemos um limite e adicionamos recursos até atingir esse limite (Por exemplo, se você deseja explicar 80% da variabilidade total possivelmente explicada pelo seu modelo, adicionamos recursos com a maior proporção de variação explicada até que a proporção de variação explicada atinja ou exceda 80%). Este é o método ideal e que usaremos daqui a pouco.


* Método 3: Este está intimamente relacionado ao método 2. Calculamos a proporção de variação explicada para cada recurso, classificamos os recursos por proporção de variação explicada e plotamos a proporção acumulada de variação explicada à medida que mantemos mais recursos (gráfico será mostrado abaixo). É possível escolher quantos recursos incluir, identificando o ponto em que a adição de um novo recurso tem uma queda significativa na variação explicada em relação ao recurso anterior e a escolha de recursos até esse ponto (Chamamos isso de método “encontre o cotovelo”, pois olhar para a “curva” ou “cotovelo” no gráfico determina onde ocorre a maior queda na proporção da variação explicada).

Como cada autovalor é aproximadamente a importância do seu autovetor correspondente, a proporção de variação explicada é a soma dos autovalores dos recursos que você manteve divididos pela soma dos autovalores de todos os recursos.

Os autovetores da matriz de covariância são as direções principais, enquanto os autovalores representam a magnitude dessas direções. Os autovalores são importantes para entender a quantidade de variação capturada por cada componente principal.

### Por que o PCA Funciona?

#### Autovalores (Eigenvalues) e Autovetores (Eigenvectors)

Uma forma automática de detectar associações multicolineares (e descobrir problemas numéricos em uma inversão de matriz) é usar autovetores. Explicados em termos simples, os autovetores são uma maneira muito inteligente de recombinar a variância entre as variáveis, criando novos recursos acumulando toda a variância compartilhada. Tal recombinação pode ser obtida usando a função NumPy linalg.eig, resultando em um vetor de autovalores (representando a quantidade de variância recombinada para cada nova variável) e autovetores (uma matriz nos dizendo como as novas variáveis se relacionam com as antigas).

Na álgebra linear, um autovetor ou vetor característico de uma transformação linear é um vetor diferente de zero que muda no máximo por um fator escalar quando essa transformação linear é aplicada a ele.

Existe uma correspondência direta entre matrizes quadradas n por n e transformações lineares de um espaço vetorial n-dimensional em si mesmo, dada qualquer base do espaço vetorial. Por esse motivo, em um espaço vetorial de dimensão finita, é equivalente a definir autovalores e autovetores usando a linguagem das matrizes ou a linguagem das transformações lineares. 

Geometricamente, um autovetor correspondente a um autovalor real diferente de zero, aponta para uma direção em que é inclinado pela transformação e o autovalor é o fator pelo qual é inclinado. Se o autovalor for negativo, a direção será invertida. Falando livremente, em um espaço vetorial multidimensional, o autovetor não é rotacionado. No entanto, em um espaço vetorial unidimensional, o conceito de rotação não tem sentido.

Depois de extrair os autovalores, imprimimos em ordem decrescente e procuramos qualquer elemento cujo valor seja próximo de zero ou pequeno em comparação com os outros. Valores próximos a zero podem representar um problema real para equações normais e outros métodos de otimização baseados na inversão matricial. Valores pequenos representam uma fonte elevada, mas não crítica, de multicolinearidade. 

#### Interpretação do PCA.

Embora o PCA seja um método muito técnico, baseado em algoritmos de álgebra linear aprofundados, é um método relativamente intuitivo quando você pensa sobre isso.

* Primeiro, a matriz de covariância ZᵀZ é uma matriz que contém estimativas de como cada variável em Z se relaciona com todas as outras variáveis ​​em Z. Compreender como uma variável está associada a outra é bastante poderoso.


* Segundo, autovalores e autovetores são importantes. Os autovetores representam direções. Pense em plotar seus dados em um gráfico de dispersão multidimensional. Então, pode-se pensar em um autovetor como uma “direção” específica em seu gráfico de dispersão de dados. Os autovalores representam magnitude ou importância. Autovalores maiores se correlacionam com direções mais importantes.


* Finalmente, assumimos que mais variabilidade em uma direção específica se correlaciona com a explicação do comportamento da variável dependente. Muita variabilidade geralmente indica sinal, enquanto pouca variabilidade geralmente indica ruído. Assim, quanto maior a variabilidade em uma direção específica, teoricamente, é indicativo de algo importante que queremos detectar.

Assim, o PCA é um método que reúne:

* Uma medida de como cada variável está associada uma à outra (Matriz de covariância).
* As direções nas quais nossos dados estão dispersos (Autovetores).
* A importância relativa dessas diferentes direções (Autovalores).
* O PCA combina nossos preditores e nos permite eliminar os autovetores que são relativamente sem importância.


### Procedimento para construir o algoritmo PCA em Python

Os passos abaixo devem ser seguidos para construir o algoritmo PCA:

**Padronização dos Dados**: PCA é sensível à escala das variáveis. Portanto, é comum padronizar os dados para que cada característica contribua igualmente. Isso envolve subtrair a média e dividir pelo desvio padrão de cada característica.

**Calculando a Matriz de Covariância**: A matriz de covariância representa a covariância de cada par de características. Ela é essencial no algoritmo PCA, pois suas direções principais são os autovetores dessa matriz.

**Encontrando os Autovetores e Autovalores**: Os autovetores da matriz de covariância são as direções principais, enquanto os autovalores representam a magnitude dessas direções. Os autovalores são importantes para entender a quantidade de variação capturada por cada componente principal.

**Ordenando os Componentes Principais**: Ordenamos os autovetores com base nos autovalores em ordem decrescente. Isso nos dá os componentes principais em ordem de importância.

**Projetando os Dados:** Finalmente, os dados originais são projetados nos principais componentes escolhidos. Esta etapa reduz a dimensionalidade dos dados, mantendo a maior parte da informação.
