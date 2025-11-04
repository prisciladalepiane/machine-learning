# 🌲 Compreendendo o Algoritmo Random Forest

O **Random Forest** é um algoritmo de *Machine Learning* do tipo **ensemble** (conjunto), que constrói múltiplas **árvores de decisão** e combina seus resultados para realizar previsões mais robustas.

Ele pertence à classe de algoritmos de ensemble conhecida como **bagging** (*Bootstrap Aggregating*), cuja principal ideia é reduzir a variância e evitar overfitting combinando vários modelos fracos.

---

## 🔍 Como o Random Forest Funciona

### 1.  Amostragem Bootstrap

- Para cada árvore da floresta, o algoritmo gera um novo conjunto de dados através de **amostragem com reposição** (*bootstrap*) a partir do conjunto original.
- Isso significa que alguns dados podem aparecer mais de uma vez, e outros podem não aparecer.

---

### 2.  Construção das Árvores de Decisão

- Cada conjunto de dados bootstrap é usado para construir uma **árvore de decisão**.
- Em cada ponto de divisão (nó), é considerado **um subconjunto aleatório de features**, o que aumenta a diversidade entre as árvores.
- Isso ajuda a evitar overfitting, pois cada árvore tem uma perspectiva diferente dos dados.

---

### 3. Seleção de Divisões

- Ao contrário de uma árvore tradicional (única) onde todas as características são consideradas para fazer uma divisão, o Random Forest **seleciona aleatoriamente um número limitado de variáveis** para encontrar a melhor divisão em cada nó.
- Essa aleatoriedade promove a diversidade e ajuda a evitar o overfitting.

---

### 4. Crescimento das Árvores

- As árvores são **crescidas até o máximo**, sem poda.
- Elas continuam a se expandir até que cada folha seja **pura** (contendo uma única classe) ou atinja um número mínimo de amostras.

---

### 5. Previsão/Predição

- **Classificação**: cada árvore vota em uma classe, e a **classe mais votada (moda)** é a predição final.
- **Regressão**: a **média** das previsões de todas as árvores é usada como resultado.

---

### 6. Redução de Variância

- O Random Forest reduz a variância combinando os resultados de várias árvores.
- Isso torna o modelo **mais estável e menos sensível ao ruído** nos dados de treinamento, se comparado a uma única árvore de decisão.

---

### 7. Importância das Características/Features

- O algoritmo permite estimar a **importância de cada variável** para a predição.
- Isso é feito analisando a contribuição de cada feature na **redução da impureza** das divisões ao longo da floresta.

---

## Vantagens do Random Forest

- Funciona bem para **classificação e regressão**
- **Robusto ao overfitting**, mesmo com muitas árvores
- Pouca necessidade de ajuste fino de hiperparâmetros
- Funciona com dados **não normalizados** e **features irrelevantes**
- Permite **avaliação de importância das variáveis**

---

> O Random Forest é um dos algoritmos mais usados em Machine Learning devido à sua **eficácia, simplicidade** e **capacidade de generalização**.
