# Arquitetura Transformer

A Arquitetura Transformer, introduzida no artigo "Attention is Allt You Need" de Vaswani"
é uma arquitetura que depende exclusivamente de mecanismos de atenção, sem recorrência (como em ENNs) ou convoluções (como em CNNs).

Mecanismos de atenção e transformadores são conceitos avançados em Inteligência Artificial que têm revolucionado particularmente o campo do Processamento de Linguagem Natural (PLN), e também têm sido aplicados com sucesso em outras áreas , como visão computacional e Séries Temporais.

O mecanismo de atenção permite que os modelos de aprendizado de máquina foquem em partes específicas da entrada quando estão processando dados, de forma similar à atenção seletiva dos humanos.

Em vez de tratar todas as partes de entrada igualmente, o mecanismo de atenção aprende a distribuir pesos diferentes indicando quais partes são mais relevantes para a tarefa em questão.

A arquiterura transformer foi criada inicialmente para problemas de PLN mas pode ser empregada em diversas áreas. Porém transformers requer uma quantidade massiva de dados (bilhões/trilhões).

https://quantdare.com/transformers-is-attention-all-we-need-in-finance-part-i/

https://arxiv.org/abs/1706.03762

## Camadas

```
INPUT Tokens → Embedding → Atenção → Feed Forward → Saída
```

### Embedding

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
embedding_dim = 5  # cada palavra vira um vetor de 5 números

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

