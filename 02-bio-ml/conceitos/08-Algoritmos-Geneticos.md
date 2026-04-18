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

## Crossover

O Crossover e a Mutação são os principais operadores dos Algoritmos Genéticos (AGs). Eles são inspirados pela reprodução e pela variabilidade genética observadas na natureza e servem para gerar novas soluções (ou indivíduos) a partir de uma população existente. Vamos detalhar cada um deles, começando pelo Crossover e seus tipos.

**Crossover (ou Cruzamento)**

O Crossover é o processo pelo qual dois indivíduos (ou pais) trocam partes de suas representações genéticas para criar novos indivíduos (ou filhos). Esse operador é fundamental para combinar características de boas soluções e explorar o espaço de busca. Existem várias técnicas de Crossover, cada uma com suas particularidades:

**Crossover de um ponto:**

Um ponto de corte é escolhido aleatoriamente no cromossomo (representação genética). As porções dos dois pais são trocadas nesse ponto para formar dois novos indivíduos. Por exemplo, se o ponto de corte for no meio do cromossomo, a primeira metade de um pai se combina com a segunda metade do outro e vice-versa. É uma técnica simples e comumente utilizada.

**Crossover de dois pontos:**

Dois pontos de corte são escolhidos aleatoriamente ao longo do cromossomo. A parte intermediária entre esses pontos é trocada entre os pais, criando dois novos indivíduos. Essa técnica permite uma combinação genética mais variada e é útil para problemas onde características mais distribuídas no cromossomo precisam ser trocadas.

**Crossover Uniforme**

Em vez de cortar o cromossomo em pontos específicos, cada gene do cromossomo é trocado aleatoriamente com uma probabilidade determinada (geralmente 50%).

Esse tipo de Crossover permite uma combinação mais diversificada de genes entre os pais e pode aumentar a variabilidade genética.

**Crossover Aritmético**

É mais comum em AGs que lidam com números reais. Aqui, os genes dos pais são combinados usando uma média aritmética ou outra operação matemática para gerar os filhos.

Exemplo: se dois genes numéricos dos pais são 5 e 10, o gene do filho poderia ser uma média, 7,5, ou um valor entre 5 e 10.

**Crossover em Anel (ou Circular)**

Genes são tratados em uma estrutura circular. O Crossover começa em um ponto aleatório e continua até que um determinado número de genes seja trocado.

É especialmente útil em problemas de otimização onde a ordem dos genes é significativa, como o Problema do Caixeiro Viajante.

O objetivo do Crossover é explorar o espaço de busca, permitindo que boas soluções se combinem para possivelmente criar soluções ainda melhores. A taxa de Crossover define a probabilidade de que o Crossover ocorra, e é um parâmetro importante para controlar a exploração do AG.

## Mutação

A Mutação é o operador que realiza pequenas alterações aleatórias nos indivíduos, e serve para garantir diversidade genética. Enquanto o Crossover combina informações existentes, a mutação introduz novas informações, ajudando o algoritmo a evitar a convergência prematura para soluções subótimas. Diferentes tipos de Mutação são usados para atender diferentes representações genéticas.

**Mutação por Inversão**

Um segmento do cromossomo é escolhido aleatoriamente e sua ordem é invertida. Isso é útil para problemas onde a ordem dos genes é significativa.


**Mutação de Ponto**

Um gene individual é escolhido aleatoriamente e alterado para outro valor possível. Por exemplo, se o cromossomo é uma string binária (como 101011), a mutação pode mudar um bit, resultando em 100011.


**Mutação Por Deslocamento**

Uma parte do cromossomo é deslocada para a esquerda ou direita, enquanto os genes deslocados são preenchidos novamente em outra parte do cromossomo. Usada em problemas de otimização onde a posição relativa dos genes é importante.


**Mutação Gaussiana (para números reais)**

Utilizada em AGs com valores contínuos. A mutação adiciona um valor aleatório, retirado de uma distribuição gaussiana, a um gene específico. Essa técnica permite pequenas variações controladas, adequadas para problemas de otimização fina.

**Mutação de Troca**

Dois genes são escolhidos aleatoriamente e trocados entre si. Muito utilizada em problemas de ordenação e de permutação, como o Problema do Caixeiro Viajante, onde a posição dos elementos importa.


A taxa de Mutação controla a probabilidade de que uma Mutação ocorra. Geralmente, essa taxa é baixa (ex: 1% a 5%), pois a Mutação excessiva pode levar o algoritmo a um comportamento mais aleatório, dificultando a convergência para uma solução ótima.

Enquanto o Crossover combina boas soluções, a Mutação introduz variação, garantindo que o AG possa escapar de ótimos locais e buscar soluções melhores no espaço de busca.

## Aplicações de Algoritmos Genéticos em Otimização Biomédica

Algoritmos Genéticos (AGs) têm se mostrado extremamente úteis na otimização biomédica, graças à sua capacidade de lidar com problemas complexos e não lineares. Eles são amplamente aplicados para:

**Design de Drogas**: AGs são utilizados para buscar combinações moleculares que maximizem a eficácia terapêutica e minimizem efeitos colaterais. Eles ajudam a identificar configurações moleculares ideais com base em grandes conjuntos de dados.

**Diagnóstico e Imagem Médica**: Em tomografia, ressonância magnética e outras técnicas de imagem, AGs são usados para otimizar parâmetros de reconstrução de imagem e segmentação de tecidos. Isso ajuda na melhoria da precisão e na qualidade das imagens médicas, facilitando diagnósticos mais precisos.

**Modelagem de Sistemas Biológicos**: AGs são empregados para calibrar modelos matemáticos complexos, como redes metabólicas e simulações de tecidos. Com isso, eles ajustam parâmetros para representar melhor os processos biológicos reais

**Planejamento de Tratamentos e Radioterapia**: Na radioterapia, AGs otimizam a dose de radiação, minimizando danos aos tecidos saudáveis ao redor e maximizando o impacto sobre o tecido canceroso. Eles ajudam a definir planos de tratamento personalizados e mais seguros.

**Análise de Dados Genômicos**: Os AGs são aplicados para identificar padrões e associações em dados genômicos, auxiliando na descoberta de predisposições genéticas para doenças e na personalização de tratamentos baseados no perfil genético de cada paciente.

Essas aplicações demonstram a flexibilidade dos AGs para lidar com os desafios da biomedicina, permitindo avanços na precisão, segurança e eficácia de procedimentos e tratamentos médicos.