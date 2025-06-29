# Design do Processo Treino e Teste
## Porque dividimos os dados em Treino e Teste nno processo de MAchine Learning?

No processo de Machine Learning, uma das etapas é dividir os dados em treino e teste. Usamos a amostra de treino para treinar o modelo e a amostra de teste para avaliar o modelo depois do treinamento.

A divisão dos dados em conjunto de treino e teste é uma prática padrão em MAchine Learning por várias razões:
- Avaliação Realista do Desempenho do Modelo
- Prevenção de Overfitting
- Ajuste de hiperparâmetros
- COnfiança na performace do modelo

> DIVIDIMOS OS DADOS EM TREINO E TESTE PARA PODER TREINAR E AVALIAR O MODELO USANDO AMOSTRAS DIFERENTES, CASO CONTRÁRIO AS INTERPRETAÇÕES SOBRE O MODELO ESTARIAM ERRADAS.

## Técnicas e Regras Para Divisão de Dados

Não exite um padrão, porém existe um conjunto de boas práticas. Existem várias técnicas e regras que ajudam a garantir que os modelos sejam treinados e avaliados de maneira eficaz. Aqui estão algumas das principais técnicas e regras:

### Proporção de divisão

Regra geral: Uma divisão comum é 70% dos dados para treino e 30% para teste. No entanto essta proporção pode variar dependendo do tamanho do conjunto de dados.

Para conjuntos de dados muito grandes, uma menor proporção (como 90% treino, 10% teste) pode ser suficiente.

Em caso de conjunto de dados pequenos, técnicas como validação cruzada (onde dados são divididos em várias partições) são mais adequadas.

> Não existe uma proporção exata para usar sempre. Perguntar sempre se o conjunto de dados de treino é suficiente para o modelo e se o conjunto de teste é suficiente para avaliar o modelo.

### Amostragem aleatória

Regra Geral: Os dados devem ser divididos aleatóriamente para evitar qualquer viés. 
Bibliotecas como `Scikit-learn` fornecem funções para dividir dados aleatpriamente e de forma eficiente.

Para garantir que as proporções de diferentes classes ou grupos sejam mantidas tanto no conjunto de treino quanto no de teste, a **estratificação** pode ser utilizada. Isso é particularmente importante em casos de desiquilibro de classes, onde algumas classes são muito menos representadas do que outras.

### Divisão baseada no Tempo

Regra geral: Em conjunto de dados onde a sequência temporal é importante (como séries temporais), a divisão deve ser feita de forma que os dados de treino incluam apenas pontos de doados anteriores ao conujneto de teste.

Ou seja, se temos dados de 12 meses, podemos colocar os dados dos primeiros 8 meses na amostra de treino e os dados dos 4 meses seguintes na amostra de teste.

### Validação cruzada (cross-validation)

Regra geral: Ao invés de treinar o modelo com todos os dados disponíveis de uma vez, a validação cruzada divide os dados em partes, chamadas de folds, e testa o modelo em diferentes conjuntos.
Isso ajuda a ter uma avaliação mais confiável, principalmente quando se tem poucos dados.

Técnicas mais comum são k-fold e leave-one-out.

#### Como funciona a validação cruzada k-fold
Os dados são divididos em k partes iguais (k = 5).

1. O modelo é treinado k vezes, cada vez usando:

- k-1 partes para treino

- 1 parte diferente para teste

2. Ao final, calcula-se a média da métrica (ex: acurácia, erro) em todos os testes.

Exemplo k = 5
```
Rodada 1: Treina com [2 3 4 5] → Testa com [1]
Rodada 2: Treina com [1 3 4 5] → Testa com [2]
Rodada 3: Treina com [1 2 4 5] → Testa com [3]
Rodada 4: Treina com [1 2 3 5] → Testa com [4]
Rodada 5: Treina com [1 2 3 4] → Testa com [5]
```

### Evitar Vazamento de Dados

É essencial garantir que nenhum dado do conjunto de teste vaze para o conjunto de treino, Isso pode enviedsr o modelo e fdar uma falsa impressão de alto desempenho.

Por isso algumas técnicas de pré-proecessamento devem ser feitas após a divisão em treino e teste.