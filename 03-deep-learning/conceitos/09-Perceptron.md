# Introdução ao Perceptron

Inventada em 1957 por Frank Rosenblatt

- Unidade básica de uma rede Neural mais complexa.
- Representação simplificada de um neurônio biológico e consiste num algoritmo de aprendizagem supervisionada para classificação binária, o que significa que pode prever se uma entrada pertence a uma das classes possíveis.

```

                                             Soma           Função 
Inputs                 Pesos                 Ponderada      de Ativação
(x₁, x₂, ..., xₙ) --> (w₁, w₂, ..., wₙ) -->  Σ (soma)   --> φ(·) -->  y
                        
```

## O Que o Perceptron é Capaz de Resolver?

O Perceptron é capaz de resolver problemas **linearmente separáveis**, ou seja, quando as duas
classes podem ser separadas por uma **linha reta** (ou, em dimensões superiores, um **plano** ou **hiperplano**).

No entanto, ele **não é capaz** de resolver problemas onde essa separação linear não é possível,
como o famoso **problema do XOR**.

## Importância do Perceptron

A importância do Perceptron na história da Inteligência Artificial é notável, pois forneceu a base
para o desenvolvimento de redes neurais mais complexas, contribuindo significativamente para o campo do aprendizado de máquina.

## Do Perceptron para as Redes Neurais Multicamadas (MLP)

A transição do Perceptron para as MLP (_MultiLayer Perceptrons_) foi uma evolução significativa no campo da IA e do aprendizado de maquina, marcado por avanços, desafios e um período conhecido como "inverno da IA"

Pontos principais dessa evolução:

**Limitações do Perceptron**

- O Perceptron original de Rosenblatt era um modelo de camada única que só conseguia resolver problemas linearmentes separáveis.

- O Perceptron não conseguia resolver certos tipos de problema, como a função XOR, que é não-linearmente separável.

**Avanços e MLP**

- Nos anos 1980, os pesquisadores começaram a explorar modelos de redes neurais com múltiplas camadas, que poderiam aprender representações mais complexas dos dados.

- A introdução do algoritmo de retropropagação (_backpropagation_) permitiu que as redes com múltiplas camadas ajustassem seus pesos internos de forma eficaz e aprendessem a representar funções não-lineares.

**Contribuições das MLPs:**

- A retropropagação forneceu um meio para as redes neurais aprenderem a partir de erros, ajustando pesos não apenas na camada de saída, mas também em camadas ocultas.

- As MLPs são compostas por uma camada de entrada, uma ou mais camadas ocultas e uma camada de saída, com cada camada contendo um número de neurônios.

- Cada neurônio nas camadas ocultas pode modelar interações não-lineares entre as entradas, e a adição de múltiplas camadas ocultas permite que a rede aprenda representações cada vez mais complexas.