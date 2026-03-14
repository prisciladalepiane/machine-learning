# Validação e Verificação de Modelos

A validação e verificação de modelos são etapas críticas no processo de desenvolvimento de modelos de aprendizado de máquina. Ambos os processos visam garantir que o modelo seja confiável, preciso e adequado para o propósito pretendido. 

A validação e verificação são essenciais para:

- Garantir a confiabilidade e precisão do modelo.
- Evitar overfitting e underfitting.
- Assegurar que o modelo seja útil na prática, e não apenas em teoria.
- Facilitar a tomada de decisões informada baseada nas previsões do modelo.

## Validação de Modelos
Validação de modelos envolve testar a eficácia do modelo em termos de sua capacidade de realizar a tarefa para a qual foi projetado, geralmente usando dados que não foram vistos durante o treinamento.

A validação busca garantir que o modelo seja generalizável, ou seja, capaz de funcionar bem em novos, variados e futuros conjuntos de dados, não apenas no conjunto de dados de treinamento.

**Técnicas:** 

<u> **Validação Cruzada** </u>: Divide o conjunto de dados em várias partes menores (folds). O modelo é treinado em várias combinações desses folds e testado no fold restante. Isso ajuda a avaliar a estabilidade e confiabilidade do modelo.

<u> **Conjunto de Testes** </u>: Após o treinamento, o modelo é avaliado usando um conjunto de testes separado que não foi usado durante o treinamento. Isso verifica a capacidade do modelo de generalizar.

<u> **Validação Externa** </u>: Quando possível, o modelo é testado em um conjunto de dados completamente externo ou em um contexto diferente do que foi usado para treinamento, para verificar sua aplicabilidade a novas condições.

## Verificação de Modelos
Verificação de modelos refere-se ao processo de garantir que o modelo foi implementado corretamente e está funcionando como previsto. Envolve a verificação técnica de que o modelo está livre de erros no código, que os dados estão sendo processados corretamente, e que os resultados gerados são consistentes com as expectativas.

É um passo fundamental antes de avançar para a validação mais aprofundada do modelo.

Atividades Comuns na Verificação de Modelos:

<u> **Testes de Unidade** </u>: Checar cada componente ou função do modelo isoladamente para garantir que está funcionando corretamente.

<u> **Testes de Integração** </u>: Testar a integração de diferentes componentes do modelo para verificar se trabalham juntos sem problemas.

<u> **Revisão de Código** </u>: Avaliar o código do modelo para garantir boas práticas de programação e evitar bugs.


## Principais Métricas de Avaliação do Modelo de Machine Learning

As métricas de avaliação em machine learning medem a performance de um modelo. Elas variam de acordo com o tipo de tarefa (classificação, regressão, detecção de anomalias, etc.).

Apresentamos a seguir algumas das métricas mais comuns por tarefa:

### Para Classificação

 - **Acurácia**: Proporção de previsões corretas sobre o total. É mais útil quando as classes estão equilibradas.

 - **Precisão**: Proporção de previsões positivas corretas. Importante quando o custo dos falsos positivos é alto.

 - **Recall** (Sensibilidade): Proporção de verdadeiros positivos identificados. Crucial quando é importante detectar todos os casos positivos.


 - **F1-Score**: Média harmônica entre precisão e recall. Útil quando se busca um equilíbrio entre precisão e recall.

 - **Curva ROC e AUC** (Área sob a Curva ROC): Medem a capacidade do modelo de distinguir entre as classes. AUC é um resumo numérico da curva ROC.

 - **Matriz de Confusão**: Tabela que mostra os verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos.

### Para Regressão


 * **Erro Quadrático Médio (MSE):** Média dos quadrados dos erros. Sensível a outliers.

 * **Raiz do Erro Quadrático Médio (RMSE)**: Raiz quadrada do MSE. Interpretação mais direta em termos das unidades originais.
 
 * **Erro Absoluto Médio (MAE)**: Média dos valores absolutos dos erros. Menos sensível a outliers do que o MSE.

 * **R² (Coeficiente de Determinação)**: Proporção da variância na variável dependente que é previsível a partir das variáveis independentes.
 
 ### Outras Métricas

 - **Log Loss:** Usada para modelos probabilísticos em classificação.

 - **Precisão-Recall AUC**: Semelhante ao AUC-ROC, mas foca na relação entre precisão e recall.

 - **Coeficiente de Correlação de Pearson**: Mede a correlação linear entre previsões e resultados reais.

Cada métrica tem seu próprio contexto de aplicação e deve ser escolhida com base nas necessidades específicas do problema e nas características do conjunto de dados.

Em alguns casos, pode ser útil considerar uma combinação de várias métricas para obter uma avaliação abrangente do modelo.

## Funções Auxiliares
**Split de Dados:** Dividir o conjunto de dados em treinamento, validação (opcionalmente) e teste, para avaliar a performance do modelo de maneira justa.

**Cross-Validation:** Técnica para avaliar a generalização do modelo e reduzir o risco de overfitting, dividindo o conjunto de dados em partes iguais para treinamento e teste.

**Feature Scaling/Normalization**: Normalizar ou padronizar as características dos dados para melhorar o desempenho de certos algoritmos de modelagem.

**Feature Selection/Engineering:** Selecionar as características mais importantes ou criar novas características para melhorar a performance do modelo.

**Hyperparameter Tuning**: Ajustar os parâmetros do modelo para maximizar sua performance, muitas vezes utilizando métodos como Grid Search ou Random Search.

# Sensibilidade e Especifidade 

A análise de sensibilidade e especificidade são duas métricas imporantes utilizadas para avaliar a performance de modelos de classificação, especialmente em campos como medicina e diagnóstico.

Essas métricas ajudam a entender como um modelo é eficaz em identificar corretamente as condições positivas e negativas, oferecendo uma visão clara sobre a confiabilidade dos resultados do modelo em diferentes cenários.

A **Sensibilidade** é a capacidade do modelo em identificar, dentre as pessoas com suspeita da doença, àquelas realmente doentes. Ou seja, prever a classe positiva.

A **Especificidade** é a capacidade do mesmo modelo prever a classe negativa nos indivíduos que não apresentam a doença que está sendo investigada.

### Sensibilidade (ou Recall)

A sensibilidade, também conhecida como recall ou taxa de verdadeiros positivos, mede a proporção de verdadeiros positivos (isto é, resultados corretamente identificados como positivos pelo modelo) em relação ao total de casos que são realmente positivos. Ela indica quão bem o modelo é capaz de detectar as condições positivas.
___

- Sensibilidade = TruePositive / (TruePositive + FalseNegative)
- Sensibilidade = True Positive Rate
___

Por exemplo, na área médica, se um teste de diagnóstico é aplicado para detectar uma doença, a sensibilidade do teste indica a probabilidade de que, se um paciente tem a doença, o teste identificará corretamente a doença.

### Especificidade
A especificidade, também chamada de taxa de verdadeiros negativos, mede a proporção de verdadeiros negativos (isto é, resultados corretamente identificados como negativos pelo modelo) em relação ao total de casos que são realmente negativos. 

Ela reflete quão bem o modelo pode identificar corretamente as condições negativas.

___
- Especificidade (Recall) = TrueNegative / (FalsePositive + TrueNegative)
- Especificidade = 1 – False Positive Rate
___

Por exemplo, em um teste de diagnóstico, a especificidade de um teste indica a probabilidade de que, se um paciente não tem a doença, o teste confirmará corretamente que o paciente está livre da doença.

### Importância

Essas métricas são particularmente importantes quando:
Em contextos médicos, por exemplo, falhar na identificação de uma doença pode ter consequências graves, assim como identificar incorretamente uma doença em uma pessoa saudável pode levar a ansiedade desnecessária ou tratamentos desnecessários.

Geralmente, existe um trade-off entre sensibilidade e especificidade. Aumentar uma pode diminuir a outra, e o equilíbrio ideal depende da aplicação específica.

A escolha entre um modelo com alta sensibilidade ou alta especificidade pode depender do custo associado a falsos positivos versus falsos negativos.

O modelo ideal seria aquele que apresentasse 100% de sensibilidade e 100% de especificidade. Assim, teríamos apenas dois resultados: negativo (a pessoa não estaria doente) ou positivo (o indivíduo estaria doente). Portanto, não teríamos o falso-negativo ou o falso-positivo.

Infelizmente, isso raramente ocorre na prática. Imagine uma balança, onde um dos pratos é a sensibilidade e o outro, a especificidade. Se ocorre melhora na sensibilidade de um modelo (o prato da balança sobe), frequentemente ocorre diminuição na especificidade (o prato da balança desce). Em algumas situações, ter uma sensibilidade de 100% é muito importante, como nas triagens sorológicas em bancos de sangue, onde os testes são realizados para a prevenção de transmissão de infecções.

Para a detecção de uma doença, por exemplo, a sensibilidade clínica é influenciada por fatores diversos, como por exemplo: o dia da coleta em relação ao início da infecção, o tipo de amostra utilizada, manifestações clínicas do paciente e a qualidade pré-técnica da amostra.

Muitos algoritmos de aprendizado de máquina são capazes de prever uma probabilidade ou uma pontuação de associação de classe.

Geralmente, isso é útil porque fornece uma medida da certeza ou incerteza de uma previsão. Ele também fornece granularidade adicional sobre apenas prever o rótulo da classe que pode ser interpretado.

Algumas tarefas de classificação requerem uma previsão exata do rótulo da classe. Isso significa que, embora uma probabilidade ou pontuação de associação de classe seja prevista, ela deve ser convertida em um rótulo de classe claro.

A decisão de converter uma probabilidade prevista ou pontuação em um rótulo de classe é governada por um parâmetro denominado "limite de decisão", "limite de discriminação" ou simplesmente o "limite" (threshold). O valor padrão para o limite é 0,5 para probabilidades previstas normalizadas ou pontuações no intervalo entre 0 ou 1.

Por exemplo, em um problema de classificação binária com rótulos de classe 0 e 1, e um limite de 0,5, então, valores menores que o limite de 0,5 são atribuídos à classe 0 e valores maiores ou iguais a 0,5 são atribuídos à classe 1 .

___

- Previsão < 0,5 = Classe 0
- Previsão >= 0,5 = Classe 1
___

O limite (threshold) no Scikit-Learn é 0,5 para classificação binária e qualquer classe que tenha a maior probabilidade em classificação multiclasse. Em muitos problemas, um resultado muito melhor pode ser obtido ajustando o limite. 

A maioria dos métodos de ajuste do limite é baseada nas características de operação do receptor (ROC) e na estatística J de Youden, mas também pode ser feito por outros métodos, como uma pesquisa com um algoritmo genético.

Aqui está um artigo que descreve como fazer isso em problemas na área Biomédica:

http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2515362/


> Os Limites de teste alteram o trade-off entre Sensibilidade e Especificidade

### Alternativas 

#### Alternativa 1

Para aumentar a Sensibilidade ou a Especificidade uma alternativa é definir o limiar que você deseja.

Exemplo: `limiar = 0.00009 `

#### Alternativa 2

Outra alternativa para ajustar o modelo é aplicar as probabilidades previamente calculadas (com base em evidências estatísticas).

Para definir os priors em um modelo Naive Bayes usando a biblioteca sklearn, você precisa passar uma lista com as probabilidades a priori de cada classe para o parâmetro priors do GaussianNB. 

Esses priors devem ser proporcionais à frequência relativa esperada de cada classe. Por exemplo, se você espera que 10% dos exemplos sejam da classe 0 e 90% sejam da classe 1, você pode definir os priors da seguinte forma: 

`priors = [0.1, 0.9]`

É importante lembrar que a soma dos priors deve ser igual a 1. Além disso, os priors são úteis quando você tem conhecimento prévio sobre a distribuição das classes no seu conjunto de dados ou quando o conjunto de dados é desbalanceado. Se você não tem essa informação ou se o conjunto de dados é balanceado, pode não ser necessário definir os priors e o modelo irá estimá-los a partir dos dados de treinamento.

## Curva ROC

A análise de sensibilidade e especificidade pode ser visualizada através de uma Curva de Característica de Operação do Receptor (**ROC**), onde a taxa de verdadeiros positivos (sensibilidade) é plotada em função da taxa de falsos positivos (1 - especificidade). A área sob a curva ROC (**AUC-ROC**) fornece uma medida agregada de desempenho de um modelo de classificação em todos os limiares de classificação.