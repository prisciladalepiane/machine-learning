# Função de Perda (Loss Function)

A **função de perda**, também chamada de **função de custo** (*cost function*) ou **função objetivo**, é um **mecanismo matemático usado para medir o erro** de um modelo de aprendizado de máquina.

Ela indica **o quão bem ou mal o modelo está se saindo**, isto é, **a diferença entre o valor predito ($\hat{y}$)** e o **valor real ($y$)**.


## Objetivo
O objetivo do treinamento de um modelo é **minimizar a função de perda**, ou seja:
$$
\min_{\theta} \; L(y, \hat{y})
$$

onde:
- $L$ → é a função de perda,
- $y$ → valores reais,
- $\hat{y}$ → valores previstos pelo modelo,
- $\theta$ → parâmetros (pesos e vieses da rede neural).

Quanto **menor o valor da perda**, **melhor o modelo está aprendendo**.


## Como funciona

1. O modelo faz uma **previsão** $\hat{y}$.
2. A função de perda compara $\hat{y}$ com o valor verdadeiro $y$.
3. Calcula um **erro (loss)**.
4. Esse erro é usado pelo **backpropagation** para ajustar os pesos e reduzir a perda nas próximas iterações.


## Tipos Comuns de Funções de Perda

| Tipo de Problema | Função de Perda | Fórmula | Descrição |
|------------------|----------------|----------|------------|
| **Regressão** | **Erro Quadrático Médio (MSE)** | $$L = \frac{1}{n} \sum_i (y_i - \hat{y}_i)^2$$ | Mede o erro médio ao quadrado entre as previsões e os valores reais. Penaliza erros grandes. |
| **Regressão** | **Erro Absoluto Médio (MAE)** | $$L = \frac{1}{n} \sum_i |y_i - \hat{y}_i|$$ | Mede a diferença média absoluta entre previsão e verdade. Menos sensível a outliers. |
| **Classificação Binária** | **Entropia Cruzada Binária (Binary Cross-Entropy)** | $$L = -\frac{1}{n} \sum_i [y_i \log(\hat{y}_i) + (1 - y_i)\log(1 - \hat{y}_i)]$$ | Mede a divergência entre a distribuição real e a predita (probabilidades). |
| **Classificação Multiclasse** | **Entropia Cruzada Categórica (Categorical Cross-Entropy)** | $$L = -\sum_i y_i \log(\hat{y}_i)$$ | Usada com *Softmax*. Penaliza previsões incorretas mais fortemente. |
| **Classificação com Margem** | **Hinge Loss** | $$L = \max(0, 1 - y \cdot \hat{y})$$ | Usada em SVMs — força as classes a ficarem separadas por uma margem. |


## Intuição

Pense na **função de perda** como um **termômetro de aprendizado**:
- Se o valor da perda é **alto**, o modelo está errando muito.
- Se o valor da perda é **baixo**, o modelo está se aproximando da resposta correta.

Durante o treinamento, o **algoritmo de otimização** (como o **Gradiente Descendente**) busca **reduzir essa perda** ajustando os pesos da rede.

## Exemplo simples

Se o modelo prevê $\hat{y} = 0.8$ para um valor real $y = 1$ e usamos MSE:

$$
L = (1 - 0.8)^2 = 0.04
$$

Esse valor representa o erro que o modelo cometeu nessa predição.

---

## Em resumo

| Conceito | Explicação |
|-----------|------------|
| **Função de perda** | Mede o erro entre a previsão e o valor real. |
| **Objetivo do treinamento** | Minimizar essa perda. |
| **Usada em** | Regressão, classificação e outros tipos de tarefas. |
| **Ligação com Backpropagation** | É a fonte do erro que será retropropagado para atualizar os pesos. |


---

# O Que é Função de Perda?

A função de perda, frequentemente referida como função de custo, função de erro ou função objetivo, é uma parte essencial dos algoritmos de  aprendizado de máquina e Deep Learning. Ela quantifica o quão bem as previsões de um modelo se alinham com os valores reais observados. Em outras palavras, ela fornece uma medida do erro entre as previsões do modelo e os dados verdadeiros. Durante o treinamento de um modelo, o objetivo principal é minimizar essa função de perda.

**Machine Learning é de fato um problema de otimização matemática.** 

Nosso objetivo é encontrar os <u>parâmetros que minimizam a função de erro</u>. A escolha da função de perda depende do tipo de problema que você está tentando resolver.

Para **problemas de regressão**, onde o objetivo é prever um valor contínuo, as funções de perda mais comuns são:

- **Erro Quadrático Médio (MSE)**: Calcula a média dos quadrados das diferenças entre as previsões e os valores verdadeiros.

- **Erro Absoluto Médio (MAE)**: Calcula a média dos valores absolutos das diferenças entre previsões e valores verdadeiros.

Para **problemas de classificação**, onde o objetivo é categorizar uma entrada em uma de várias classes, as funções de perda mais comuns incluem:

- **Entropia Cruzada (ou log loss)**: É uma medida da dissimilaridade entre a distribuição prevista pelo modelo e a distribuição real dos rótulos. Para classificação binária, é frequentemente  chamada  de log loss binária e para classificação  multiclasse, é referida como entropia cruzada categórica.

- **Hinge Loss**: Usada principalmente para máquinas de vetores de suporte (SVMs) em tarefas de classificação.


Modelos Generativos: Para modelos que geram algum tipo de saída, como Generative Adversarial Networks (GANs), as funções de perda são projetadas para medir a diferença entre os dados gerados e os dados reais. 

Durante o processo de treinamento, o algoritmo ajusta os parâmetros do modelo (como os pesos em uma rede neural) para minimizar a função de perda. A otimização é frequentemente realizada usando técnicas como gradiente descendente ou variantes deste algoritmo.

É importante escolher a função de perda adequada ao problema específico que você está abordando,  pois  a  função  de  perda  determina  como  o  modelo  será  ajustado  durante  o treinamento e pode afetar significativamente o desempenho do modelo final
