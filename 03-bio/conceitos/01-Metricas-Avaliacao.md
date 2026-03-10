# Principais Métricas de Avaliação do Modelo de Machine Learning

As métricas de avaliação em machine learning medem a performance de um modelo. Elas variam de acordo com o tipo de tarefa (classificação, regressão, detecção de anomalias, etc.).

Apresentamos a seguir algumas das métricas mais comuns por tarefa:

## Para Classificação

 - **Acurácia**: Proporção de previsões corretas sobre o total. É mais útil quando as classes estão equilibradas.

 - **Precisão**: Proporção de previsões positivas corretas. Importante quando o custo dos falsos positivos é alto.

 - **Recall** (Sensibilidade): Proporção de verdadeiros positivos identificados. Crucial quando é importante detectar todos os casos positivos.


 - **F1-Score**: Média harmônica entre precisão e recall. Útil quando se busca um equilíbrio entre precisão e recall.

 - **Curva ROC e AUC** (Área sob a Curva ROC): Medem a capacidade do modelo de distinguir entre as classes. AUC é um resumo numérico da curva ROC.

 - **Matriz de Confusão**: Tabela que mostra os verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos.

## Para Regressão


 * **Erro Quadrático Médio (MSE):** Média dos quadrados dos erros. Sensível a outliers.

 * **Raiz do Erro Quadrático Médio (RMSE)**: Raiz quadrada do MSE. Interpretação mais direta em termos das unidades originais.
 
 * **Erro Absoluto Médio (MAE)**: Média dos valores absolutos dos erros. Menos sensível a outliers do que o MSE.

 * **R² (Coeficiente de Determinação)**: Proporção da variância na variável dependente que é previsível a partir das variáveis independentes.
 
 ## Outras Métricas

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

A **Sensibilidade** é a capacidade do modelo em identificar, dentre as pessoas com suspeita da doença, àquelas realmente doentes. Ou seja, prever a classe positiva.

A **Especificidade** é a capacidade do mesmo modelo prever a classe negativa nos indivíduos que não apresentam a doença que está sendo investigada.

___

- Sensibilidade = TruePositive / (TruePositive + FalseNegative)
- Sensibilidade = True Positive Rate

___

- Especificidade (Recall) = TrueNegative / (FalsePositive + TrueNegative)
- Especificidade = 1 – False Positive Rate

___

O modelo ideal seria aquele que apresentasse 100% de sensibilidade e 100% de especificidade. Assim, teríamos apenas dois resultados: negativo (a pessoa não estaria doente) ou positivo (o indivíduo estaria doente). Portanto, não teríamos o falso-negativo ou o falso-positivo.

Infelizmente, isso raramente ocorre na prática. Imagine uma balança, onde um dos pratos é a sensibilidade e o outro, a especificidade. Se ocorre melhora na sensibilidade de um modelo (o prato da balança sobe), frequentemente ocorre diminuição na especificidade (o prato da balança desce). Em algumas situações, ter uma sensibilidade de 100% é muito importante, como nas triagens sorológicas em bancos de sangue, onde os testes são realizados para a prevenção de transmissão de infecções.

Para a detecção de uma doença, por exemplo, a sensibilidade clínica é influenciada por fatores diversos, como por exemplo: o dia da coleta em relação ao início da infecção, o tipo de amostra utilizada, manifestações clínicas do paciente e a qualidade pré-técnica da amostra.

Muitos algoritmos de aprendizado de máquina são capazes de prever uma probabilidade ou uma pontuação de associação de classe.

Geralmente, isso é útil porque fornece uma medida da certeza ou incerteza de uma previsão. Ele também fornece granularidade adicional sobre apenas prever o rótulo da classe que pode ser interpretado.

Algumas tarefas de classificação requerem uma previsão exata do rótulo da classe. Isso significa que, embora uma probabilidade ou pontuação de associação de classe seja prevista, ela deve ser convertida em um rótulo de classe claro.

A decisão de converter uma probabilidade prevista ou pontuação em um rótulo de classe é governada por um parâmetro denominado "limite de decisão", "limite de discriminação" ou simplesmente o "limite" (threshold). O valor padrão para o limite é 0,5 para probabilidades previstas normalizadas ou pontuações no intervalo entre 0 ou 1.

Por exemplo, em um problema de classificação binária com rótulos de classe 0 e 1, e um limite de 0,5, então, valores menores que o limite de 0,5 são atribuídos à classe 0 e valores maiores ou iguais a 0,5 são atribuídos à classe 1 .

- Previsão < 0,5 = Classe 0
- Previsão >= 0,5 = Classe 1