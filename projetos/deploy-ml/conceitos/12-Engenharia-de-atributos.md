# Engenharia de Atributos

## O Que é Engenharia de Atributos?

Engenharia de atributos, ou feature engineering, trata-se da técnica de usar o conhecimento do domínio para selecionar, modificar ou criar novos atributos (também chamados de features) a partir dos dados brutos, com o objetivo de melhorar o desempenho dos modelos de aprendizado de máquina.

Essa prática é importante porque a qualidade e a relevância dos atributos inseridos em um modelo têm um impacto significativo na capacidade do modelo de aprender e fazer previsões ou classificações precisas.

Por vezes, dados brutos não estão imediatamente prontos para serem eficazmente utilizados por modelos de aprendizado de máquina, seja devido à presença de ruído, valores faltantes ou simplesmente porque a informação relevante não está sendo apresentada de uma forma que os modelos possam facilmente aproveitar.

A engenharia de atributos envolve várias técnicas, como:

**Seleção de Atributos**
Identificar e selecionar as variáveis mais relevantes para o problema em questão.


**Transformação de Atributos**
Aplicar transformações matemáticas ou estatísticas para alterar a escala ou a distribuição dos dados.


**Criação de Atributos**
Derivar novos atributos a partir dos existentes, por exemplo, combinando duas colunas de dados para criar uma nova que capture uma interação relevante.


**Codificação de Variáveis Categóricas**
Converter variáveis categóricas, como gênero ou país, em uma forma numérica que os modelos de aprendizado de máquina possam processar, utilizando técnicas como codificação one-hot ou ordinal.


**Normalização ou Padronização**
Ajustar a escala dos atributos para que tenham uma distribuição mais uniforme, o que pode ajudar na convergência dos algoritmos de aprendizado.

A engenharia de atributos é frequentemente vista como uma arte tanto quanto uma ciência, pois requer intuição, criatividade e um profundo entendimento dos dados, além de um conhecimento sólido dos algoritmos de aprendizado de máquina a serem aplicados.

É um processo iterativo e pode consumir uma grande parte do tempo em um projeto de aprendizado de máquina, mas é essencial para construir modelos eficazes e precisos.

## Técnicas de Engenharia de Atributos

As técnicas de engenharia de atributos podem ser amplamente categorizadas com base em seu propósito e na natureza dos dados com os quais estão lidando.

Detalhamos a seguir algumas das técnicas mais comuns utilizadas na engenharia de atributos:

1. Seleção de Atributos
Filtragem: Usa estatísticas para selecionar atributos baseando-se em seu relacionamento com a variável alvo.

Wrapper methods: Usam um modelo preditivo para avaliar a importância dos atributos, selecionando aqueles que melhoram a performance do modelo.

Embedded methods: Integram a seleção de atributos como parte do processo de treinamento do modelo, como é o caso de modelos que utilizam regularização.

2. Extração e Criação de Atributos
Análise de Componentes Principais (PCA): Reduz a dimensionalidade dos dados ao transformá-los em um conjunto menor de variáveis sumárias (componentes) que retêm a maior parte da variabilidade original dos dados.


Engenharia de Atributos Temporais: Derivação de novos atributos a partir de variáveis de tempo, como hora do dia, dia da semana, diferenças de tempo entre eventos etc.

Combinação e Transformação de Atributos: Criação de novos atributos por meio da combinação ou transformação de atributos existentes, como somar, subtrair, multiplicar ou dividir duas ou mais colunas.
3. Tratamento de Dados Categóricos
Codificação One-Hot: Transforma variáveis categóricas em uma forma que possa ser fornecida aos algoritmos de ML, criando uma nova coluna binária para cada categoria.

Codificação de Frequência: Substitui as categorias pela frequência (ou porcentagem) de sua ocorrência nos dados.

Codificação Target (Mean encoding): Substitui a categoria pelo valor médio da variável alvo para essa categoria.

4. Normalização e Padronização
Normalização (Min-Max Scaling): Escala os atributos para que fiquem dentro de um intervalo específico, geralmente entre 0 e 1.

Padronização (Z-score normalization): Transforma os atributos para que tenham média 0 e desvio padrão 1.

5. Tratamento de Dados Faltantes
Imputação: Substituição de valores faltantes por um valor estimado com base em outras observações.

Indicadores de Dados Faltantes: Criação de novos atributos que indicam a presença de dados faltantes em outros atributos.

6. Tratamento de Dados Desbalanceados
Sobreamostragem (Oversampling) ou Subamostragem (Undersampling): Ajusta o balanceamento das classes alvo por meio da replicação de exemplos da classe minoritária ou remoção de exemplos da classe majoritária.

SMOTE: Técnica de sobreamostragem que cria exemplos sintéticos da classe minoritária.

7. Detecção e Tratamento de Outliers
Métodos estatísticos: Uso de scores Z ou intervalos interquartis (IQR) para identificar outliers.

Truncamento ou Capping: Limitação de valores extremos a um certo limite definido.

Cada uma dessas técnicas pode ser aplicada conforme necessário, dependendo do conjunto de dados específico e do problema que está sendo resolvido.

A escolha e aplicação eficaz dessas técnicas podem significativamente melhorar a qualidade do modelo de aprendizado de máquina, impactando diretamente seu desempenho e precisão.


## Importância da Qualidade dos Atributos

A qualidade dos atributos é fundamental no aprendizado de máquina porque determina a capacidade dos modelos de aprender padrões significativos nos dados e fazer previsões ou classificações precisas.

A seleção, criação e otimização de bons atributos são etapas essenciais que podem impactar diretamente o sucesso ou fracasso de um projeto de aprendizado de máquina.

Vejamos a seguir  os principais motivos que tornam a qualidade dos atributos tão importante:

1. Melhora o Desempenho do Modelo
Atributos de alta qualidade fornecem informações claras e relevantes que facilitam a tarefa do modelo em identificar padrões.

Modelos alimentados com dados bem preparados tendem a alcançar uma precisão mais alta, menor taxa de erro e melhor generalização para dados não vistos.

2. Facilita a Convergência do Modelo
Atributos bem selecionados e adequadamente preparados ajudam a otimizar o processo de treinamento, permitindo que o modelo alcance a convergência mais rapidamente.

Isso é particularmente importante em modelos complexos, onde o custo computacional do treinamento pode ser significativo.

3. Reduz a Complexidade do Modelo
A eliminação de atributos irrelevantes ou redundantes através de técnicas de seleção de atributos pode reduzir a complexidade do modelo.

Modelos mais simples são geralmente mais rápidos para treinar, mais fáceis de interpretar e manter, e menos propensos ao overfitting.

4. Melhora a Interpretabilidade
Modelos construídos com atributos de alta qualidade e bem entendidos são mais fáceis de interpretar.

Isso é essencial para aplicações em que a tomada de decisões precisa ser explicada ou justificada, como em contextos financeiros, médicos ou jurídicos.

5. Adequação aos Diferentes Tipos de Dados e Modelos
Cada modelo de aprendizado de máquina tem suas próprias exigências quanto ao tipo, escala e distribuição dos atributos de entrada.

A qualidade dos atributos influencia diretamente a compatibilidade com diferentes algoritmos, maximizando a eficácia do modelo escolhido.

6. Gestão de Dados Faltantes e Outliers
O tratamento cuidadoso de dados faltantes e outliers é parte da engenharia de atributos.

Atributos de qualidade são aqueles que foram devidamente tratados para minimizar distorções e viéses no modelo causados por anomalias nos dados.

7. Adaptação a Mudanças nos Dados
Em ambientes dinâmicos, onde os padrões de dados podem mudar com o tempo (drift de conceito), atributos de alta qualidade permitem uma melhor adaptação a essas mudanças, mantendo a precisão do modelo ao longo do tempo.

A qualidade dos atributos é um dos pilares mais importantes do aprendizado de máquina, impactando diretamente a eficácia, eficiência, e aplicabilidade dos modelos gerados.

Investir tempo e recursos na engenharia de atributos é fundamental para o sucesso de qualquer projeto de aprendizado de máquina.

## Seleção de Atributos

A seleção de atributos, também conhecida como seleção de variáveis ou seleção de características, é um processo crítico na preparação de dados para modelagem de aprendizado de máquina.

Seu objetivo é identificar e selecionar os atributos (ou variáveis) mais relevantes para a tarefa preditiva, removendo os dados irrelevantes ou redundantes.

Isso não apenas pode melhorar o desempenho do modelo, mas também tornar o modelo mais eficiente, reduzindo o tempo de treinamento e simplificando o modelo, o que, por sua vez, pode facilitar a interpretação.

### Por que é Seleção de Atributos é Importante?


Reduz a Complexidade do Modelo: Diminuir o número de atributos pode simplificar o modelo, tornando-o mais rápido para treinar e mais fácil de entender e interpretar.

Melhora o Desempenho: Remover dados irrelevantes ou redundantes pode melhorar a precisão do modelo, pois o modelo não é mais distraído por ruídos nos dados.

Previne Overfitting: Menos atributos significam menos oportunidades para o modelo aprender o ruído nos dados de treinamento como se fossem padrões significativos, o que pode melhorar a capacidade do modelo de generalizar para novos dados.

Reduz o Tempo de Treinamento: Menos dados significam que os algoritmos de aprendizado de máquina podem processar mais rápido, reduzindo o tempo necessário para treinar os modelos.


### Técnicas Comuns de Seleção de Atributos

1. Métodos de Filtragem (Filter Methods)
Essas técnicas aplicam um critério estatístico para avaliar a relação entre cada atributo e a variável alvo, independentemente do modelo.

Exemplos incluem:

* Correlação: Seleciona atributos com base na força da correlação (positiva ou negativa) com a variável alvo.


* Testes estatísticos: Chi-quadrado, testes ANOVA, etc., para avaliar a importância dos atributos.



2. Wrapper Methods
Esses métodos avaliam subconjuntos de atributos, criando modelos usando esses subconjuntos e calculando a qualidade do modelo para determinar a importância dos atributos.

Exemplos incluem:

* RFE (Recursive Feature Elimination): Iterativamente constrói modelos e remove o pior ou os piores atributos, continuando este processo até que o número desejado de atributos seja alcançado.

* Métodos de busca sequencial: Como busca sequencial para frente (forward selection) e busca sequencial para trás (backward elimination).


3. Embedded Methods
Integram a seleção de atributos como parte do processo de treinamento do modelo e são específicos para determinados tipos de modelos. Esses métodos aproveitam a penalização (como L1/Lasso e L2/Ridge) para adicionar custos aos atributos, efetivamente realizando seleção de atributos enquanto o modelo é treinado.

Exemplos incluem:

* Modelos baseados em penalidades: Lasso (L1), que pode reduzir os coeficientes de alguns atributos para zero, efetivamente selecionando um subconjunto de atributos úteis.

* Árvores de decisão e modelos baseados em árvores: Como Random Forests e Gradient Boosting, que podem avaliar a importância dos atributos com base na sua contribuição para a melhoria do modelo.


A escolha da técnica de seleção de atributos depende do tipo de dados, do problema específico e do tipo de modelo que se pretende utilizar.

Em muitos casos, uma combinação de métodos pode ser usada para alcançar os melhores resultados.

A seleção de atributos é um passo iterativo e primordial no processo de modelagem de aprendizado de máquina, que pode significativamente impactar o sucesso do projeto.

