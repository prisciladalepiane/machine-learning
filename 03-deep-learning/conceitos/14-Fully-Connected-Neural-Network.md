# Arquitetura Fully Connected Neural Network

É um tipo classico de arquitetura  de rede neural usada em deep-learning

**1. Estrutura Básica:**
Em uma FCNN, cada neurônio em uma camada está conectado a todos os neurônios na camada anterior e na camada seguinte. Isso difere de outras arquiteturas, como as redes neurais convolucionais (CNNs), onde as conexões são parciais ou localizadas.

**2. Camadas:**
Uma FCNN típica consiste em uma camada de entrada, várias camadas ocultas e uma camada de saída. A camada de entrada recebe os dados de entrada, as camadas ocultas realizam a maior parte do processamento através de pesos e funções de ativação, e a camada de saída produz a previsão ou classificação final.

**3. Neurônios e Pesos:**
Cada neurônio em uma camada está conectado a todos os neurônios na camada seguinte por meio de pesos. Esses pesos são ajustados durante o treinamento da rede para minimizar a diferença entre a saída prevista e a real.\
Exemplo, se uma camada tem: 3 neurônios -> a próxima tem 5 neurônios -> então existem 3 × 5 conexões (pesos) entre elas.
Cada conexão tem um peso, e cada neurônio tem um viés (bias).

**4. Funções de Ativação:**

As funções de ativação, como a função sigmóide, ReLU (Rectified Linear Unit) ou tanh, são aplicadas aos resultados das somas ponderadas dos neurônios. Elas introduzem não-linearidades na rede, o que é crucial para aprender e modelar relações complexas nos dados.

**5. Backpropagation e Treinamento:**

O treinamento de uma FCNN é geralmente feito usando o algoritmo de backpropagation, que ajusta os pesos da rede de forma iterativa com base no erro (diferença entre a saída prevista e a real). O Gradient Descent é frequentemente usado para encontrar a direção e o passo do ajuste dos pesos.

**6. Aplicações:**

FCNNs são versáteis e podem ser usadas para uma variedade de tarefas, como classificação, regressão, e até mesmo como parte de arquiteturas mais complexas em tarefas como processamento de linguagem natural e visão computacional.

**7. Desvantagens:**

Uma das desvantagens das FCNNs é que elas podem se tornar muito grandes e computacionalmente caras, especialmente para entradas de alta dimensão, pois cada neurônio em uma camada está conectado a todos os neurônios na camada anterior. Isso também pode levar a um risco maior de overfitting, onde a rede se torna muito bem ajustada aos dados de treinamento e não generaliza bem para novos dados.

Limitações:

- Não escala bem para imagens, texto ou sequências longas
- Número de parâmetros cresce muito rápido
- Não explora estrutura espacial ou temporal
- Facilmente sofre overfitting

**8. Comparação com Outras Arquiteturas:**

Em comparação com CNNs e RNNs (Redes Neurais Recorrentes), as FCNNs são mais simples e não têm a capacidade de lidar eficientemente com dados que têm uma estrutura espacial ou temporal inerente, como imagens ou séries temporais.


**Resumo**
Uma FCNN aprende combinações não lineares de todas as features ao mesmo tempo, sem assumir estrutura especial nos dados.

Ela é:

- poderosa em dados tabulares
- conceitualmente simples
- a base de praticamente tudo em Deep Learning