# Backpropagation (Retropropagação do Erro)

O **Backpropagation** é o algoritmo central de aprendizado em redes neurais artificiais. 
Ele permite **ajustar os pesos da rede** de forma eficiente, **minimizando o erro** entre a saída prevista e a saída real. 

Foi popularizado por Rumelhart, Hinton e Williams (1986) e é usado até hoje em quase todos os modelos de Deep Learning.

---

## Ideia Geral

O processo ocorre em **duas fases principais**:

1. **Propagação direta (Forward Pass):**
 - Os dados entram na rede e passam camada por camada até gerar uma **saída predita** ($\hat{y}$).
 - Essa saída é comparada com a **saída real** ($y$) para calcular o **erro (loss)**.

2. **Propagação reversa (Backward Pass):**
 - O erro é **retropropagado** através das camadas da rede.
 - Calcula-se o **gradiente da função de custo** em relação a cada peso usando a **Regra da Cadeia (Chain Rule)** do cálculo diferencial.
 - Esses gradientes são então usados para **ajustar os pesos**, reduzindo o erro na próxima iteração.

---

## Etapas Matemáticas

1. **Cálculo da saída (forward):**
 $$
 z_j = \sum_i w_{ij} x_i + b_j
 $$
 $$
 a_j = f(z_j)
 $$
 onde $f$ é a **função de ativação**.

2. **Cálculo do erro (função de custo):**
 $$
 E = \frac{1}{2} (y - \hat{y})^2
 $$
 (para um problema de regressão simples).

3. **Propagação do erro (backward):**
 - Calculamos o gradiente do erro em relação aos pesos:
 $$
 \frac{\partial E}{\partial w_{ij}} = \frac{\partial E}{\partial a_j} \cdot \frac{\partial a_j}{\partial z_j} \cdot \frac{\partial z_j}{\partial w_{ij}}
 $$
 - Essa é a **regra da cadeia**, que “propaga” o erro de volta, camada por camada.

4. **Atualização dos pesos (descida do gradiente):**
 $$
 w_{ij}^{(t+1)} = w_{ij}^{(t)} - \eta \frac{\partial E}{\partial w_{ij}}
 $$
 onde $\eta$ é a **taxa de aprendizado** (*learning rate*).

<center>

| Etapa | Descrição |
|-------|------------|
| **Forward pass** | Calcula a saída da rede. |
| **Erro** | Mede o quanto a saída está errada (função de custo). |
| **Backward pass** | Propaga o erro de volta, calculando gradientes. |
| **Atualização** | Ajusta pesos e vieses para reduzir o erro. |
</center>


## Função de Custo e Otimização

O **backpropagation** trabalha junto com um **algoritmo de otimização**, geralmente uma variação da **descida do gradiente** (*Gradient Descent*), como:
- **SGD (Stochastic Gradient Descent)**
- **Adam**
- **RMSprop**

Esses métodos determinam **como atualizar os pesos** com base nos gradientes.


## Desafios

- **Desaparecimento ou explosão do gradiente:** em redes muito profundas, os gradientes podem ficar muito pequenos ou muito grandes. 
- **Convergência lenta:** pode exigir ajustes finos de hiperparâmetros (como taxa de aprendizado). 
- **Overfitting:** a rede pode memorizar os dados de treino.


## Em resumo

O **Backpropagation** é o **mecanismo de aprendizado das redes neurais**, que permite:
- calcular **quanto cada peso contribuiu para o erro**,
- **ajustar esses pesos** de modo eficiente,
- e **fazer a rede aprender padrões complexos** nos dados.

# O Papel do Backpropagation e Otimização em Deep Learning

O backpropagation, também conhecido como retropropagação, é um algoritmo fundamental em Deep Learning, utilizado para reinar redes neurais. Seu papel principal é calcular o gradiente da função de perda (ou erro) em relação a cada peso da rede, de modo eficiente, através da aplicação da regra da cadeia do cálculo diferencial. Este gradiente indica a direção e magnitude de mudança para cada peso, a fim de minimizar o erro da rede.

Quando alimentamos uma rede neural com uma entrada, a informação flui da camada de entrada através das camadas ocultas até a camada de saída em um processo chamado "feedforward". Ao comparar a saída produzida pela rede com a saída desejada, obtemos um valor de erro utilizando uma função de perda. O backpropagation entra em cena para determinar como esse erro se propaga de volta através da rede, do final para o início. Ele calcula quanto cada peso na rede contribuiu para o erro, fornecendo um mapa de como ajustar os pesos para melhorar o desempenho da rede.No entanto, saber o gradiente por si só não é suficiente. É aqui que entra a otimização. O processo de otimização ajusta iterativamente os pesos da rede na direção oposta ao gradiente, buscando minimizar o erro. O tamanho do ajuste é geralmente determinadopor um parâmetro chamado "taxa de aprendizado". Um dos otimizadores mais básicos e amplamente conhecidos é o Gradiente Descendente (e suas variantes como Gradiente Descendente Estocástico e Gradiente Descendente em Mini-lotes). No entanto, existem muitos outros otimizadores, como Adam, RMSprop e Adagrad, que não só consideram o gradiente atual, mas também incorporam informações de gradientes anteriores para fazer atualizações mais informadas.

No entanto, saber o gradiente por si só não é suficiente. É aqui que entra a otimização. O processo de otimização ajusta iterativamente os pesos da rede na direção oposta ao gradiente, buscando minimizar o erro. O tamanho do ajuste é geralmente determinadopor um parâmetro chamado "taxa de aprendizado". Um dos otimizadores mais básicos e amplamente conhecidos é o Gradiente Descendente (e suas variantes como Gradiente Descendente Estocástico e Gradiente Descendente em Mini-lotes). No entanto, existem muitos outros otimizadores, como Adam, RMSprop e Adagrad, que não só consideram o gradiente atual, mas também incorporam informações de gradientes anteriores para fazer atualizações mais informadas.

Juntos, o backpropagation e os algoritmos de otimização formam a espinha dorsal do treinamento de redes neurais em Deep Learning. Eles permitem que a rede aprenda padrões complexos e não lineares nos dados, ajustando-se iterativamente para reduzir o erro e melhorar a precisão. Esta combinação de calcular gradientes e ajustar pesos é repetida muitas vezes até que a rede alcance um desempenho satisfatório ou até que se cumpra algum critério de parada definido