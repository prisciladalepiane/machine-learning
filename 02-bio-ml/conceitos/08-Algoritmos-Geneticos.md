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