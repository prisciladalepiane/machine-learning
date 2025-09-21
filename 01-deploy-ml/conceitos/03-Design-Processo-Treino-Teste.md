# Design do Processo Treino e Teste
## Porque dividimos os dados em Treino e Teste no processo de MAchine Learning?

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

É essencial garantir que nenhum dado do conjunto de teste vaze para o conjunto de treino, Isso pode enviesar o modelo e dar uma falsa impressão de alto desempenho.

Por isso algumas técnicas de pré-proecessamento devem ser feitas após a divisão em treino e teste, como a padronização ou normalização dos dados.

> A escolha de técnica adequada para divisão depende: dos tipos de dados, do tamanho do conjunto de dados, da naturezado problema de negócio e dos recursos computacionais disponíveis. 

## Teste durante ou depois de treinar o modelo?

**Conjunto de Treino:** Utilizado para treinar o modelo. O modelo aprende a partir deste conjunto.

**Conjunto de Teste:** Utilizado para avaliar o modelo depois de treinado. Avalia a perforace do modelo em dados que não foram vistos durante o treinanto.

Além disso, muitas vezes um **terceiro conjunto**, chamado COnjunto de Validação é utilizado durante o treinamento para ajustar os parâmetros do modelo, selecionar entre vários modelos ou para fazer a sintonia fina dos hiperparâmetros.

O modelo é ajustado até que a performace no conjunto de validação não melhore mais.
Isso é especialmente útil em modelos de Deep LEarning ou com grande conjuntos de dados.

> Portanto, o teste do modelo pode acontecer durante e depois do treinamento.

**Durante:** O conjunto de validação é usado para monitorar e ajustar o modelo durante o treinamento (por exemplo, pra evitar overfitting). Não é exatamente um "teste" no sentido estrito, mas sim uma validação e otimização.

**Depois:** Após o modelo ser treinado e ajustado, o conjunto de teste é utilizado para avaliar a performace final do modelo.

É uma maneira de verificar se o modelo aprendeu padrões verdadeiros nos dados e não apenas ruído ou detalhes específicos do conjunto de treino.

Para a validação, diminuir os dados de teste, não de treino, exemplo: (70%, 15% e 15%)

## Estratégias de Avaliação de Desempenho DURANTE o Treino do modelo

### CALLBACKS
Em Machine Learning, especialmente ao treinar modelos com bibliotecas como Keras (usada com TensorFlow), um callback é um mecanismo que permite executar funções específicas em determinados momentos do treinamento do modelo, como no final de uma época (epoch), após um batch, no início ou fim do treino, etc.

Um callback é uma função ou classe que “escuta” o treinamento do modelo e intervém automaticamente quando certas condições são atendidas.

**Early Stopping:** Para interromper o treinamento quando uma métrica monitorada parou de melhorar, prevenindo overfitting.

**Model Checkpointing:** Para salvar o modelo em diferentes pontos do treinamento, geralmente mantendo apenas a melhor versão do modelo de acordo com uma métrica de desempenho escolhida.

**TensorBoard Integration:**
Para integrar com ferramentas de visualização como o TensorBoard, permitindo que você monitore o progresso do treinamento em tempo real.

**Dynamic Adjustments:**
Para fazer ajustes dinâmicos em hiperparâmetros ou na estrutura do modelo em resposta ao desempenho do treinamento.

**Condition-based Actions:**
Para realizar ações com base no estado atual do treinamento, como aumentar a complexidade do modelo se o treinamento estiver indo bem, ou simplificá-lo se estiver ocorrendo overfitting.

**Custom Callbacks:**
Para executar ações personalizadas que você define. Por exemplo, você pode criar um callback para enviar uma mensagem de alerta se determinadas condições forem atendidas ou para modificar os dados de entrada de maneiras específicas antes de cada época.

> Use callbacks sempre que quiser automatizar decisões durante o treinamento do modelo. Isso ajuda a evitar overfitting, economiza tempo e melhora a reprodutibilidade do processo.

## Estratégias de Avaliação de Desempenho DEPOIS o Treino do modelo

Após o treinamento do modelo de ML, DEVEMOS realizar uma rigorosa avaliação de desempenho para entender como o modelo provavelmente se comportará com dados novos e não vistos.

**Conjunto de Teste**: Utilizar um conjunto de dados separados que não foi usado durante  o treino nem na validação para avalir a performace do modelo. Este é o teste final que fornece a estimativa mais realista do desempenho do modelo em condições reais.

**Métricas de desempenho**: CAlcular métricas específicas para o problema em questão, como: precição, recall, F1 score para problemas de classificação; MSE, RMSE, MAE para problemas de regressão; conficiente de silhoeta para problemas de clustering.

**Matriz de confusão:** Para problemas de classificação, uma matriz de confusão pode ajudar a entender as taxas de verdadeiro positivo, falso positivo, verdadeiro negativo e falso negativo.

**Curvas ROC e AUC**: Avaliar a capacidade do modelo de discriminar entre classes. A área sob a curva (AUC) da curva ROC (Receiver Operating Characteristic) é uma métrica agregada de desempenho em todos os limiares de classificação.

**Análise de Erros:** Examinar casos onde o modelo falhou para entender os erros e potencialmente melhorar o modelo.

**Comparação com modelos de referência:** Comparar o desempenho do modelo com modelos de linha de base simples ou modelos previamente estabelecidos para avaliar ganhos de desempenho.

**Testes Estatísticos:** Para modelos preditivos, realizar testes estatísticos, como teste t, para comparar a média das métricas de desempenho do modelo com outros modelos ou com um benchmar.

**Análise de Sensibilidade e Especificidade:** Para problemas de classificação médica, por exemplo, a sensibilidade (tava de verdadeiro positivo) e a especificidade (tava de verdadeiro negativo) são métricas que devem ser verificadas.

**Teste de significância:** Avaliar de as diferenças no desempenho entre modelos são estatísticamente significativas.

**Avaliação de desempenho em subgrupos:** Verificas o desempenho do modelo em diferentes segmentos dos dados para identificar se o modelo tem um viés em relação a determinados grupos.

**Análise de Custo-Benefício:** Em certos cados, como em marketing ou diagnósticos médicos, é importante considerar o custo de falsos positivos e falsos negativos para avaliar a performace do modelo de uma perspectiva de negócios ou clínica.

**Feedback de Pós-Impantação:** Após a implementação do modelo, coletar feedback contínuo sobre seu desempenho para monitorar o desempenho a longo prazo.

## Como detectar Overfitting e Underfitting?

Pode ser difícil e em muitos casos só conseguimos detectar ao final do processo, quando muito trabalho já foi realizado. Quanto antes for detectado e resolvido, menos retrabalho será necessário.

Estratégias comuns:

- Regra Geral - Desempenho no Conjunto de Treino vs. Conjunto de Teste

*Overfitting*: Se o modelo tem desempenho muito bom no conjunto de treino mas pobre no conjunto de teste ou de validação, é sinal clássico de overfitting.

*Underfitting*: Se o modelo tem um desempenho ruim tanto no conjunto de treino quanto no conjunto de teste, pode estar ocorrendo underfitting.

- Desenhe curvas de aprendizado que mostram o desempenho do modelo nos conjuntos de treino e validação/teste ao longo das épocas de treinamento. *Overfitting* pode ser indicado por uma grande lacuna entre as duas curvas. 
- O uso de **validação cruzada** fornece uma estimativa mais robusta do desempenho do modelo. Se o modelo tem um alto desempenho na validação cruzada, mas um desempenho muito menor no conjunto de teste, isso pode indicar *overfitting*.
- Modelos com **muitos parâmetros** comparados em relação ao número de observações pode estar propenso ao *overfitting*. tendem a se ajustar demais aos dados de treino.
- Uma **matriz de confusão** que mostra desempenho muito alto em uma classe e ruim nas demais pode revelar **sobreajuste/overfitting**.

### Estratégias para tratar overfitting e underfitting

Para Overfitting:

- Simplifique o modelo (reduza a arquitetura)
- Use técnicas de regularização (L1, L2, dropout)
- Colete mais dados de treino
- Utilize técnicas como data augmentation
- Aplique early stopping durante o treino
- Reduza a complexidade das features (feature selection)

Para Underfitting:

- AUmente a complexidade do modelo (adicione mais camadas/neurônios)
- Treine modelos por mais tempo
- Experimente diferentes algoritmos de otmização
- Adicione mais atributos ou crie atributos mais complexos
- Revise o pré-processamento dos dados para garantir que não está demasiadamente simplificado

## Data Augmentation

**Data Augmentation** é uma técnica usada para aumentar artificialmente o volume de dados, por meio de modificações nos dados existentes ou da geração de dados sintéticos. Essa abordagem é especialmente útil quando o conjunto de dados é pequeno, ajudando a melhorar a generalização do modelo e a reduzir o overfitting.

### Pontos-chave:

- **Variação de Dados Existentes**: Inclui transformações como rotações, cortes e mudanças de cor (em imagens) ou substituição de palavras e reestruturação de frases (em texto).
- **Geração de Dados Sintéticos**: Pode ser feita com técnicas como GANs ou simulações.
- **Melhoria da Generalização**: Aumenta a exposição do modelo a diferentes variações, melhorando sua performance em dados não vistos.
- **Prevenção de Overfitting**: Reduz a chance de o modelo memorizar dados em vez de aprender padrões.
- **Aplicação Ampla**: Utilizável com imagens, texto, áudio e dados tabulares.
- **Parte do Pré-processamento**: Geralmente integrado ao pipeline de preparação dos dados.
- **Balanceamento de Classes**: Útil para aumentar a representatividade de classes minoritárias.

> ⚠️ Deve ser usado com cautela: exageros podem comprometer a representatividade e a qualidade dos dados.
