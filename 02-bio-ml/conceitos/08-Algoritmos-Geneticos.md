# Algoritmos Genéticos (AG)

Algoritmos Genéticos (AGs) são uma técnica de otimização e busca inspirada na teoria da evolução de Charles Darwin. Eles simulam processos evolutivos para encontrar soluções aproximadas para problemas complexos. Aqui estão os princípios fundamentais:

**Codificação**: Cada solução possível para o problema é representada por um "indivíduo" ou "cromossomo", que é uma estrutura de dados com uma representação específica. Normalmente, usa-se uma string binária ou uma sequência de números, onde cada posição representa uma característica (ou "gene") da solução.

**População Inicial**: Um conjunto de indivíduos (população) é gerado aleatoriamente no início do processo. A quantidade de indivíduos na população pode afetar a velocidade e a qualidade da convergência da solução.

**Função de Avaliação (Fitness)**: Cada indivíduo é avaliado de acordo com uma função de "fitness", que mede a qualidade ou adequação da solução que ele representa. O objetivo do AG é maximizar ou minimizar essa função de fitness.

**Seleção**: Com base na função de fitness, os indivíduos mais bem avaliados têm uma chance maior de serem escolhidos para a reprodução. Métodos de seleção comuns incluem a roleta (onde a probabilidade é proporcional ao fitness), torneio e seleção por ranking.

**Cruzamento (Crossover)**: Dois indivíduos selecionados (pais) trocam partes de suas representações para criar novos indivíduos (filhos). Esse processo simula a troca genética e permite a combinação de boas características de ambos os pais. Existem vários tipos de cruzamento, como o de um ponto e o de dois pontos.

**Mutação**: Para manter a diversidade genética e evitar que o algoritmo fique preso em soluções locais, pequenas alterações aleatórias são aplicadas aos genes dos indivíduos. A mutação ocorre com baixa probabilidade e garante que novas características possam surgir na população.

**Substituição**: Após a geração de novos indivíduos, eles substituem alguns dos antigos na população. A estratégia de substituição depende do AG e pode ser parcial (onde apenas alguns dos piores indivíduos são substituídos) ou total (onde a nova geração inteira substitui a antiga).

**Convergência**: O AG itera o processo de avaliação, seleção, cruzamento e mutação até que uma condição de parada seja atingida. Isso pode ser um número fixo de gerações, um tempo limite, ou quando a melhoria na função de fitness atinge um patamar insignificante.

Os Algoritmos Genéticos são amplamente utilizados em problemas de otimização complexos, onde é difícil ou impossível encontrar uma solução exata em tempo razoável. 

## Estratégias de Seleção

As estratégias de seleção em Algoritmos Genéticos (AGs) determinam quais indivíduos de uma população são escolhidos para se reproduzir e gerar a próxima geração. Essas estratégias são essenciais, pois influenciam a taxa de convergência e a capacidade do algoritmo de encontrar soluções ótimas. Abaixo estão as principais estratégias de seleção:

### 1. Seleção por Roleta (Roulette Wheel Selection)

Nesta abordagem, cada indivíduo recebe uma "fatia" de uma roleta proporcional à sua aptidão (fitness). Indivíduos com fitness mais alto têm fatias maiores e a roleta é girada para selecionar indivíduos.

Como em uma roleta de cassino, a probabilidade de um indivíduo ser escolhido é proporcional ao seu fitness em relação ao fitness total da população.

- Vantagem: Simples de implementar.

- Desvantagem: Pode favorecer excessivamente os indivíduos mais aptos, resultando em perda de diversidade na população.


### 2. Seleção por Torneio (Tournament Selection)

Um grupo de indivíduos é selecionado aleatoriamente e o indivíduo com o maior fitness dentro desse grupo é escolhido para reprodução.

O tamanho do torneio é um parâmetro importante: torneios maiores aumentam a pressão seletiva, enquanto torneios menores promovem maior diversidade.

- Vantagem: Simples e flexível. Mantém diversidade ao escolher apenas os melhores de pequenos grupos.

- Desvantagem: Se o tamanho do torneio for muito grande, pode levar a uma convergência prematura.

### 3. Seleção por Ranking (Rank Selection)

Em vez de usar diretamente o fitness, os indivíduos são classificados de acordo com o fitness. Em seguida, cada indivíduo recebe uma probabilidade de seleção com base na sua posição na classificação.

Indivíduos mais aptos têm maiores chances de serem escolhidos, mas a pressão seletiva é mais equilibrada, já que a probabilidade não depende diretamente dos valores de fitness.

- Vantagem: Reduz o risco de "dominância" de indivíduos com fitness muito alto, mantendo uma seleção mais balanceada.

- Desvantagem: Pode diminuir a pressão seletiva, o que resulta em uma convergência mais lenta.

### 4. Seleção por Amostragem Estocástica Universal (Stochastic Universal Sampling - SUS)

É uma variação da seleção por roleta. Aqui, uma linha reta é imaginada e dividida em segmentos proporcionais ao fitness dos indivíduos. Então, vários indivíduos são escolhidos simultaneamente, em intervalos regulares ao longo dessa linha.

Funciona bem para manter a diversidade, pois seleciona indivíduos com fitness alto e baixo de forma balanceada.

- Vantagem: Menor variabilidade na seleção, resultando em uma representação mais precisa das probabilidades de seleção.

- Desvantagem: Um pouco mais complexa que a roleta padrão.

### 5. Seleção Elitista (Elitism)

Esta abordagem garante que os melhores indivíduos de uma geração sejam diretamente transferidos para a próxima geração sem modificação. É usada em combinação com outras estratégias de seleção.

O número de indivíduos a serem mantidos (taxa de elitismo) é determinado pelo usuário. Comumente, 1 ou 2 indivíduos são preservados.

- Vantagem: Garante que a melhor solução até o momento nunca seja perdida.

- Desvantagem: Pode levar a uma convergência prematura se a taxa de elitismo for muito alta, já que a população pode ficar estagnada.

### 6. Seleção Truncada (Truncation Selection)

Nesta estratégia, apenas uma porcentagem dos melhores indivíduos é selecionada para reprodução. Essa fração é escolhida com base em um valor de corte predeterminado.

Todos os indivíduos selecionados têm a mesma probabilidade de reprodução, independente de sua classificação específica dentro do grupo de elite.

- Vantagem: Fácil de implementar e promove uma seleção simples e rápida.

- Desvantagem: Se a fração de corte for muito pequena, a diversidade genética pode diminuir rapidamente.

### 7. Seleção Baseada em Roleta Com Penalidades (Fitness-Proportionate Selection with Penalization)

Funciona de forma semelhante à seleção por roleta, mas indivíduos que repetem genes ou que geram pouca diversidade genética recebem penalizações no fitness.

A ideia é diminuir as chances de escolha de indivíduos que possam reduzir a variabilidade genética na população.

- Vantagem: Ajuda a manter a diversidade, limitando a reprodução de indivíduos muito parecidos.

- Desvantagem: Implementação mais complexa e pode afetar negativamente a pressão seletiva se a penalização não for bem calibrada.

Essas estratégias permitem ajustar o equilíbrio entre a exploração do espaço de busca (mantendo diversidade) e a exploração de soluções promissoras (focando nas melhores soluções). A escolha da estratégia depende da natureza do problema, dos requisitos de performance e da diversidade desejada ao longo das gerações.