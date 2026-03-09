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