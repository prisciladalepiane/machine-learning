# Vetorização com TF-IDF

A vetorização com TF-IDF (Term Frequency-Inverse Document Frequency) é uma técnica amplamente utilizada em processamento de linguagem natural (PLN) para converter texto em um formato numérico que pode ser processado por algoritmos de machine learning.
O modelo é mais simples, mas fácil de interpretar e de treinar.

Componentes dessa técnica:

**Vetorização**: 

Vetorização é o processo de converter texto em vetores de números. Em PLN, isso geralmente envolve a conversão de palavras ou frases em um vetor, onde cada dimensão do vetor representa uma característica específica do texto, como a presença ou frequência de uma palavra.

**Term Frequency (TF):** 

O TF é uma medida da frequência com que uma palavra ocorre em um documento. É calculado como o número de vezes que uma palavra aparece no documento dividido pelo número total de palavras no documento. Isso dá uma medida de quão importante uma palavra é para um documento individual em um corpus.

$$ TF(t,d) = frac{freq(t,d)}{total de palavras em d} $$

Onde:

 - _t_ é o termo (palavra)
 - _d_ é o documento

**Inverse Document Frequency (IDF):**

O IDF é uma medida de quão importante uma palavra é em todo o corpus de documentos. É calculado como o logaritmo do número total de documentos no corpus dividido pelo número de documentos que contêm a palavra. O IDF diminui o peso de palavras que ocorrem muito frequentemente em um corpus (como "e", "o", "a") e que são, portanto, menos informativas.
Mede **quão rara é a palavra no conjunto de documentos**.

$$ IDF(t) = \log( \frac{N}{df(t)} ) $$

Onde:

N = número total de documentos
df(t) = número de documentos que contêm o termo

**TF-IDF:** 

A pontuação TF-IDF de uma palavra é o produto de seu TF e IDF. Isso significa que palavras que são frequentes em um documento, mas não muito frequentes no corpus, recebem uma pontuação alta. Isso ajuda a identificar palavras importantes para um documento específico em relação ao resto do corpus.

**Aplicações de TF-IDF:**

O TF-IDF é usado para várias tarefas em PLN, como recuperação de informação, extração de palavras-chave e como uma etapa de pré-processamento para algoritmos de machine learning em tarefas como classificação de texto, agrupamento de documentos e detecção de similaridade entre documentos.

**Vetores TF-IDF:**

Ao aplicar TF-IDF a um corpus inteiro, cada documento é transformado em um vetor. Cada dimensão desse vetor corresponde a uma palavra única no corpus, e o valor nessa dimensão é a pontuação TF-IDF da palavra nesse documento específico. Esses vetores podem então ser usados como entrada para algoritmos de machine learning.

A vetorização com TF-IDF é eficaz para destacar as palavras mais relevantes em documentos e para lidar com a grande dimensionalidade que é comum em tarefas de PLN.

No entanto, ela não capta a ordem das palavras ou a semântica contextual, limitações que são abordadas por técnicas mais avançadas como word embeddings e modelos de linguagem baseados em transformers.

