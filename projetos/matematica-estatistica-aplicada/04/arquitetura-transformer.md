# Funcionamento Geral da Arquitetura Transformer

O modelo Transformer, introduzido no artigo "Attention is All You Need" (Vaswani et al., 2017) pelos pesquisadores do Google, revolucionou a maneira como as sequências de dados são processadas, particularmente na área de Processamento de Linguagem Natural (PLN). Diferente de RNNs e LSTMs, ele não processa tokens de forma sequencial, mas em paralelo, usando apenas mecanismos de atenção. Seu funcionamento geral pode ser descrito em etapas principais:

### Entrada de Dados

- Cada palavra (ou token) é convertida em um vetor denso por meio de uma camada de embedding. Isso permite que o modelo trate as palavras (ou qualquer outro tipo de unidade de dados) como representações densas em um espaço vetorial de alta dimensão. 

- Como o Transformer não processa tokens em ordem, adiciona-se uma codificação posicional (positional encoding), que injeta informação sobre a posição de cada token na sequência.

Assim, a entrada inicial é a soma:

$$X=Embedding(tokens)+PositionalEncoding$$


### Mecanismo de Atenção: 

O coração do Transformer é o mecanismo de atenção, especificamente a atenção multi-cabeça. Este mecanismo permite que o modelo pondere a importância de diferentes partes da sequência de entrada ao processar um determinado elemento. Em outras palavras, o modelo pode "olhar" para todas as partes da entrada simultaneamente e decidir quais partes são mais relevantes para o cálculo atual. A atenção multi-cabeça repete esse processo várias vezes em paralelo, cada uma focando em diferentes subespaços das representações vetoriais.

**Blocos do Encoder:**

O encoder é composto por N camadas empilhadas (no artigo original, N = 6).
Cada camada tem duas subpartes principais:

1. Atenção Multi-Cabeça (Multi-Head Attention)

    - Cada “cabeça” aprende a focar em diferentes relações entre tokens.
    - Isso é feito a partir de três matrizes:

        - Q (queries): o que estou perguntando.
        - K (keys): onde buscar.
        - V (values): a informação a ser extraída.
    A versão multi-cabeça faz isso várias vezes em paralelo e concatena os resultados.

2. Rede Feed-Forward Posição-Sábia

    - Cada posição é passada por uma pequena rede neural densa (duas camadas lineares + ativação ReLU).

    - Isso ajuda a modelar relações não lineares.

Em cada subcamada, temos ainda conexões residuais + normalização de camada, garantindo estabilidade no treinamento.


### Conexões Residuais e Normalização:

 Para facilitar o treinamento de redes profundas, cada subcamada no encoder e no decoder tem uma conexão residual em torno dela seguida por uma normalização de camada. Isso significa que a saída de cada subcamada é somada à sua entrada antes de ser passada à próxima subcamada, ajudando a mitigar o problema do desvanecimento do gradiente em redes profundas.

**Blocos do Decoder:**

O decoder também tem N camadas empilhadas, mas com 3 subpartes:

1. Masked Multi-Head Attention

 - Parecido com a atenção do encoder, mas com uma máscara que impede o modelo de “olhar para frente” (garantindo causalidade).

 - Isso força o modelo a prever o próximo token apenas com base nos anteriores.

2. Atenção Encoder-Decoder

- O decoder usa atenção sobre as saídas do encoder, conectando a representação da entrada com o processo de geração da saída.

3. Feed-Forward Posição-Sábia

 - Igual ao encoder.

> Também há conexões residuais + normalização em cada subparte.

### Saída Final
No final do decoder, a saída passa por uma camada linear e, em seguida, por uma função softmax para gerar as probabilidades da próxima palavra na sequência. Essas probabilidades são usadas para selecionar a saída final, seja durante o treinamento ou na geração de texto.

 - O último vetor do decoder passa por uma camada linear que projeta para o tamanho do vocabulário.
 - Em seguida, aplica-se softmax, produzindo uma distribuição de probabilidades sobre as próximas palavras possíveis.
 - Durante geração, o token mais provável (ou amostrado) é escolhido, e o processo continua até formar a sequência final.

---

Em resumo, o Transformer processa sequências de entrada utilizando um mecanismo de atenção que lhe permite considerar toda a sequência de uma vez, ao invés de sequencialmente. Isso, junto com sua arquitetura encoder-decoder, torna-o excepcionalmente bom em capturar relações complexas em dados sequenciais, tornando-o uma escolha popular para uma ampla gama de tarefas.

```
Entrada + Positional Encoding
          ↓
       Encoder → Representações da entrada
          ↓
       Decoder (usa saída do encoder + tokens já gerados)
          ↓
   Linear + Softmax
          ↓
  Distribuição sobre tokens de saída
```