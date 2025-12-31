# Principais Métricas de Classificação

Métricas de classificação são utilizadas para avaliar o desempenho de modelos de aprendizado de máquina cujo objetivo é a previsão de classes ou categorias.

Estas métricas fornecem informações importantes sobre a eficácia do modelo em prever corretamente diferentes classes. Elas são essenciais para entender a qualidade das previsões do modelo e para guiar a otimização e ajuste do modelo.

Dentre as métricas mais importantes destacamos:


### 1. Acurácia (Accuracy)

Mede a proporção de previsões corretas (tanto positivas quanto negativas) em relação ao total de previsões feitas pelo modelo.

### 2. Precisão (Precision)

Avalia a proporção de previsões positivas corretas em relação ao total de previsões positivas feitas pelo modelo.

### 3. Recall (Sensibilidade ou Taxa de Verdadeiros Positivos)

Mede a proporção de casos positivos reais que foram corretamente identificados pelo modelo.

### 4. F1-Score

Combina precisão e recall em uma única métrica, fornecendo um equilíbrio entre eles. É particularmente útil em situações onde as classes estão desequilibradas.

### 5. Curva ROC (Receiver Operating Characteristic) e Área sob a Curva (AUC-ROC)

A curva ROC mostra a performance do modelo em todos os limiares de classificação, enquanto a AUC quantifica a performance geral do modelo, sendo 1.0 a performance perfeita e 0.5 equivalente a um palpite aleatório.

### 6. Matriz de Confusão

Fornece uma visão detalhada do desempenho do modelo, mostrando a distribuição das previsões em relação aos valores reais através de verdadeiros positivos, falsos positivos, verdadeiros negativos e falsos negativos.

### 7. Sensibilidade e Especificidade

Sensibilidade (ou recall) mede a proporção de positivos reais identificados corretamente, enquanto a especificidade mede a proporção de negativos reais identificados corretamente.

### 8. Taxa de Falsos Positivos (False Positive Rate, FPR)

Mede a proporção de falsos positivos em relação ao total de casos negativos reais.

A escolha da métrica adequada depende do problema específico e dos objetivos do modelo. Por exemplo, em aplicações médicas onde é vital não perder casos positivos, o recall pode ser mais importante.

Em outros cenários onde os falsos positivos têm um custo alto, a precisão pode ser priorizada.