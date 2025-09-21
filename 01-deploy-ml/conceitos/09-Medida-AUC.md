# AUC - Área sob a Curva ROC

https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html

A **AUC** (*Area Under the Curve*) é uma métrica usada para avaliar o desempenho de modelos de classificação binária. Ela representa a **área sob a curva ROC** (*Receiver Operating Characteristic*), que é uma representação gráfica da sensibilidade (TPR) versus 1 - especificidade (FPR) em diferentes limiares de decisão.

### Intuição da Curva ROC

- **Eixo Y**: Taxa de verdadeiros positivos (TPR ou *Recall*)
- **Eixo X**: Taxa de falsos positivos (FPR = 1 - Especificidade)

Cada ponto da curva ROC representa um par (TPR, FPR) para um determinado limiar de decisão.

### O que representa a AUC?

- **AUC = 1.0**: Classificação perfeita.
- **AUC = 0.5**: Modelo aleatório (sem capacidade de discriminação).
- **AUC < 0.5**: Modelo pior que o acaso (inversão de classes).

A AUC pode ser interpretada como a **probabilidade do modelo rankear corretamente** uma instância positiva acima de uma negativa escolhida aleatoriamente.

### Vantagens da AUC

- Independe do limiar de decisão.
- Leva em conta toda a distribuição dos scores de predição.
- Robusta a desbalanceamentos de classe (não depende da proporção de positivos e negativos).

### Limitações da AUC

- Pode ser otimista em datasets desbalanceados quando há muitos negativos.
- Não reflete o custo real de falsos positivos ou falsos negativos.
- Não considera o desempenho em um limiar específico de operação.

### Quando usar AUC?

A AUC é útil para **comparar modelos de classificação binária**, especialmente quando:
- O limiar de decisão ainda não foi definido.
- As classes estão desbalanceadas.
- O objetivo é maximizar a separabilidade entre classes.


**Exemplo prático**:
Se um modelo A tem AUC = 0.90 e um modelo B tem AUC = 0.85, o modelo A tem maior capacidade de distinguir entre classes positivas e negativas, em média.

## Algumas razões para optar por um modelo com maior AUC:

**Medida de Desempenho Abrangente**: A AUC-ROC é uma medida que considera todos os limiares de classificação possíveis, fornecendo uma visão geral do desempenho do modelo em diferentes níveis de sensibilidade e especificidade. Um modelo com uma AUC mais alta geralmente indica que tem uma melhor capacidade de distinguir entre as classes positivas e negativas em vários limiares.

**Robustez a Classes Desbalanceadas**: Em muitos problemas reais, o número de observações em uma classe é muito maior do que o outro, o que pode levar a um modelo tendencioso. A AUC-ROC é menos afetada pelo desbalanceamento de classes do que outras métricas, como a precisão, porque ela avalia o desempenho do modelo em todos os limiares de classificação, não apenas na decisão de corte padrão.

**Equilíbrio entre Sensibilidade e Especificidade**: A escolha de um modelo com a maior AUC implica que o modelo não apenas identifica corretamente os verdadeiros positivos (sensibilidade) mas também exclui corretamente os verdadeiros negativos (especificidade). Isso é fundamental em muitas aplicações práticas, como no diagnóstico médico, onde tanto os falsos negativos quanto os falsos positivos podem ter consequências graves.

**Comparação de Modelos**: A AUC oferece uma única métrica que pode ser usada para comparar a performance de diferentes modelos em um problema de classificação. Isso simplifica a escolha entre modelos, já que uma AUC mais alta indica, de maneira geral, um modelo que desempenha melhor a tarefa de classificar as observações corretamente.

**Independência de Decisão de Corte**: Diferentemente de métricas que dependem de um ponto de corte específico (como precisão, recall e F1-Score), a AUC considera a performance do modelo em todos os possíveis pontos de corte. Isso significa que a AUC reflete a qualidade do modelo em termos de sua capacidade de ranquear previsões corretamente, independentemente de como o limiar de decisão é posteriormente escolhido.

**Previsão de Probabilidades**: A curva ROC e, consequentemente, a AUC são particularmente úteis quando estamos interessados em prever probabilidades de classe em vez de classificações binárias. Um modelo que produz probabilidades calibradas e discriminativas entre as classes terá uma AUC mais alta.
