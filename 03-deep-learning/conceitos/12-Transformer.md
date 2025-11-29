# Arquitetura Transformer

A Arquitetura Transformer, introduzida no artigo "Attention is Allt You Need" de Vaswani"
é uma arquitetura que depende exclusivamente de mecanismos de atenção, sem recorrência (como em ENNs) ou convoluções (como em CNNs).

Mecanismos de atenção e transformadores são conceitos avançados em Inteligência Artificial que têm revolucionado particularmente o campo do Processamento de Linguagem Natural (PLN), e também têm sido aplicados com sucesso em outras áreas , como visão computacional e Séries Temporais.

O mecanismo de atenção permite que os modelos de aprendizado de máquina foquem em partes específicas da entrada quando estão processando dados, de forma similar à atenção seletiva dos humanos.

Em vez de tratar todas as partes de entrada igualmente, o mecanismo de atenção aprende a distribuir pesos diferentes indicando quais partes são mais relevantes para a tarefa em questão.

A arquiterura transformer foi criada inicialmente para problemas de PLN mas pode ser empregada em diversas áreas. Porém transformers requer uma quantidade massiva de dados (bilhões/trilhões).

https://quantdare.com/transformers-is-attention-all-we-need-in-finance-part-i/

https://arxiv.org/abs/1706.03762


```
INPUT Tokens → Embedding → Atenção → Feed Forward → Saída
```

## Embedding

Imagine que você tem uma frase. O modelo não entende palavras. Ele só entende números. Então antes de treinar qualquer rede neural, você precisa transformar:

["gato", "correu", "rápido"]

em números, como:

[12, 84, 203]

O problema é que esses números não significam nada para a rede.
Eles são só índices.

É aí que entra o _embedding_.

Se `embedding_dim = 4`, cada palavra vira um vetor de 4 números.

```python
import torch
import torch.nn as nn

# Temos um "vocabulário" de 4 palavras
# vamos supor:
# 0 = gato
# 1 = cachorro
# 2 = carro
# 3 = casa

vocab_size = 4
embedding_dim = 5 # cada palavra vira um vetor de 5 números

embedding = nn.Embedding(vocab_size, embedding_dim)

# Entrada: uma frase com tokens
# Exemplo: "gato cachorro carro"
entrada = torch.tensor([0, 1, 2]) 

# Passa pelo embedding
saida = embedding(entrada)

print("Vetores resultantes:")
print(saida)
```

Cada palavra foi transformada em um vetor de 5 dimensões. Esses números começam aleatórios, mas durante o treinamento a rede ajusta esses vetores para que palavras com significados parecidos fiquem próximas.

## Atenção
O mecanismo de atenção tenta responder a uma pergunta simples: ao processar um token, para quais outros tokens ele deve prestar mais atenção?

De forma simples, o funcionamento é este:

Cada palavra (já transformada em vetor pelo embedding) é usada para criar três vetores diferentes: Query, Key e Value.

Query = o que estou procurando
Key = o que eu ofereço
Value = a informação que eu carrego

Para cada palavra da frase, o modelo compara sua Query com todas as Keys das outras palavras.
Isso gera uma pontuação que indica o quanto uma palavra deve olhar para outra.

Essas pontuações passam por um softmax, viram pesos de atenção.

Cada palavra recebe uma combinação ponderada dos Values das outras palavras, usando esses pesos.
Assim, ela coleta informação relevante do contexto.

O resultado é um vetor enriquecido, que entende relações na frase.

Exemplo simples:
Na frase : "o gato bebeu água porque estava com sede",
ao ler "porque", o modelo aprende que deve prestar mais atenção a gato e bebeu água para entender quem está com sede.

Atenção é o mecanismo que permite ao modelo olhar para o contexto inteiro e decidir o que importa para cada palavra.

### Componentes Q (Query), K (Key) e V (Value)

Dentro da arquitetura Transformer, o mecanismo de atenção, especificamente a atenção do tipo "scaled dot-product", utiliza três componentes principais: Q (Query), K (Key) e V (Value).

Estes componentes são essenciais para o funcionamento da atenção, que é o coração do Transformer, permitindo que ele lide eficientemente com sequências de dados, como texto, ao determinar a importância relativa de diferentes partes da entrada. Vejamos o que faz cada componente:

**Q (Query)**

Função: As Queries (Consultas) representam a parte da informação em que estamos interessados. Em um contexto de Processamento de Linguagem Natural (PLN), por exemplo, se estivéssemos traduzindo uma frase, a query seria a parte da frase que estamos tentando traduzir no momento.

Uso: Em um modelo Transformer, para cada posição na sequência de entrada (ou saída, no caso do decoder), uma query é gerada. Estas queries são usadas para pontuar o quão relevante cada parte da entrada é para essa posição particular.

**K (Key)**

Função: As Keys (Chaves) são usadas para pontuar cada parte da entrada. Elas são comparadas com as queries para determinar o grau de "atenção" que cada parte da entrada deve receber.

Uso: Em termos práticos, a comparação entre uma query e todas as keys resulta em um conjunto de pontuações, que indicam quão relevante cada parte da entrada é para a parte representada pela query.


**V (Value)**

Função: Os Values (Valores) contêm a informação real que queremos extrair. Depois que as queries e as keys determinam onde o modelo deve focar, os values são usadas para compor a saída do mecanismo de atenção.

Uso: Cada value é associado a uma key. Depois que as pontuações são calculadas entre queries e keys, estas pontuações são usadas para ponderar os values. O resultado ponderado destes values é a saída do mecanismo de atenção.

**Como Funciona na Prática**

No Transformer, Q, K e V são derivados da mesma entrada em camadas de atenção do encoder, mas de entradas diferentes no decoder (Q vem da saída da camada anterior do decoder, enquanto K e V vêm da saída do encoder). O mecanismo de atenção calcula um conjunto de pontuações (usando o produto escalar entre Q e K, daí o nome "scaled dot-product attention"), aplica uma função softmax para obter pesos de atenção e usa esses pesos para ponderar os values, criando uma saída que é uma combinação ponderada das informações relevantes de entrada.

Este processo permite que o modelo dê "atenção" às partes mais relevantes da entrada para cada parte da saída, o que é especialmente útil em tarefas como tradução, onde a relevância de diferentes palavras da entrada pode variar dependendo da parte da fraseque está sendo traduzida.

## Scaled Dot-Product Attention

A Scaled Dot-Product Attention calcula o quanto cada palavra deve prestar atenção às outras comparando seus vetores Query e Key por meio de um produto escalar(dot-product) entre: quanto maior o resultado, mais relevante uma palavra é para a outra. Esses valores são divididos pela raiz da dimensão dos vetores para evitar números grandes e instáveis, e depois passam por um softmax que transforma tudo em pesos de atenção. Por fim, esses pesos são usados para combinar os vetores Value, gerando uma representação final onde cada palavra incorpora informações importantes de todas as outras no contexto.

3 passos:

**1. Calcular similaridade entre palavras**

O modelo cria três vetores para cada token:
Query (Q), Key (K) e Value (V).

Para medir o quanto uma palavra A deve olhar para uma palavra B, fazemos:

similaridade = Q • K


Isso é um dot-product: ele mede o alinhamento entre os dois vetores.
Quanto maior, mais atenção A deve dar a B.

**2. Escalar (dividir pela raiz quadrada da dimensão)**

Sem esse passo, os valores poderiam ficar muito grandes e deixar o softmax instável.

O ajuste é:

$$\frac{(Q • K)}{\sqrt{d_k}}$$



Onde d_k é o tamanho do vetor Key.
Isso reduz a explosão dos valores e deixa o cálculo mais suave.

Por isso o nome scaled (escalado).

**3. Transformar em pesos com softmax**

Aplicamos o softmax para transformar as similaridades em probabilidades:

```
weights = softmax( 
    (Q • K) / sqrt(d_k) 
    )
```

Esses pesos dizem quanto cada palavra importa.

**4. Combinar com os valores (Values)**

Os valores finais da atenção são:

```
attention_output = weights × V
```


Ou seja: cada palavra vira uma média ponderada (com pesos inteligentes) da informação de todas as outras palavras.


> **Scaled Dot-Product Attention** pega Queries e Keys para medir similaridade, divide para estabilizar e usa isso para combinar inteligentemente os Values que carregam informação.

## Stack de Encoders e Decoders

Em sua essência, a arquitetura Transformers contém uma pilha de camadas codificadoras e camadas decodificadoras. Para evitar confusão, nos referiremos à camada individual como Codificador ou Decodificador e usaremos a pilha do codificador ou a pilha do decodificador para um grupo de camadas do codificador.

A pilha do codificador e a pilha do decodificador têm, cada uma, suas camadas de incorporação (embedding) correspondentes para suas respectivas entradas. Finalmente, existe uma camada de saída para gerar a saída final.

Todos os codificadores são idênticos entre si. Da mesma forma, todos os decodificadores são idênticos.

O codificador contém a importante camada de autoatenção que calcula o relacionamento entre as diferentes palavras na sequência, bem como uma camada de feed-forward.

O Decodificador contém a camada de autoatenção e a camada de feed-forward, bem como uma segunda camada de atenção do codificador-decodificador.

Cada codificador e decodificador possui seu próprio conjunto de pesos. Existem muitas variações da arquitetura do Transformer. Algumas arquiteturas de Transformer não possuem nenhum decodificador e dependem apenas do codificador.

## O Que Faz a **Autoatenção**?

A chave para o desempenho inovador do Transformer é o uso da Atenção, especificamente da Autoatenção.

Ao processar uma palavra, a Atenção permite que o modelo se concentre em outras palavras da entrada que estejam intimamente relacionadas a essa palavra.

Por exemplo. ‘Bola’ está intimamente relacionado com ‘azul’ e ‘segurar’. Por outro lado, ‘azul’ não está relacionado com ‘menino’.

```
O menino está segurando a bola azul
``` 

A arquitetura do Transformer usa Autoatenção relacionando cada palavra na sequência de entrada com todas as outras palavras.