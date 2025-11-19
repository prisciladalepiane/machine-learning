# Backpropogation

Backpropagation é o **algoritmo que permite uma rede neural aprender**, ajustando seus pesos para reduzir o erro entre as previsões da rede e os valores verdadeiros.

A ideia central é simples:

1. A rede faz uma previsão.
2. Calcula quanto errou.
3. Propaga esse erro de volta por todas as camadas.
4. Ajusta os pesos para que o erro diminua na próxima vez.

Partes:

### 1. Forward pass: a rede faz uma previsão

Os dados entram pela primeira camada e vão passando camada por camada até gerar uma saída.

Exemplo em cada camada:

* soma ponderada: $ z = W x + b $
* ativação: $ a = f(z) $

No final, temos a previsão $\hat{y}$.


### 2. Cálculo do erro

Comparamos a previsão com o valor verdadeiro.

Exemplo com erro quadrático médio:

$
\text{Loss} = \frac{1}{n} \sum (y - \hat{y})^2
$

Se o erro está alto, os pesos estão “ruins”.


### 3. Backward pass: propagação do erro

Agora o erro é **retropropagado** da última camada para a primeira.

A pergunta que o backprop tenta responder é:

**"Como cada peso contribuiu para o erro?"**

Para isso, ele usa cálculo diferencial (regra da cadeia).

Exemplo da ideia para um peso ( w ):

$$
\frac{\partial \text{Loss}}{\partial w}
$$

Essa derivada diz:

* se for positiva, o peso está aumentando o erro → diminuir o peso
* se for negativa, o peso está diminuindo o erro → aumentar o peso
* se for zero, o peso não influencia o erro naquele momento


### 4. Atualização dos pesos

Depois de calcular os gradientes, atualizamos cada peso:

$$
w_{novo} = w_{antigo} - \eta \frac{\partial \text{Loss}}{\partial w}
$$

Onde:

* $ \eta $ é a **taxa de aprendizado**
* o gradiente mostra a direção para reduzir o erro

Esse processo é chamado de **gradiente descendente**.


## Como isso acontece em uma rede profunda?

O backpropagation calcula os gradientes camada por camada de trás para frente:

1. Última camada: calcula gradiente do erro direto
2. Camadas intermediárias: recebem parte do gradiente das camadas seguintes
3. Primeira camada: termina a cadeia de derivadas

O algoritmo aplica a **regra da cadeia** muitas vezes.


### Resumo

1. **Forward:** calcula a previsão.
2. **Erro:** compara com o valor real.
3. **Backward:** calcula como cada peso afeta o erro.
4. **Atualiza pesos:** ajusta tudo usando gradiente descendente.

