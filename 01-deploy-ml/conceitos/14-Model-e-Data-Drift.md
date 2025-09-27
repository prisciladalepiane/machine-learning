# Model e Data Drift 

## Model Drift (ou "Desvio de Modelo"):

Refere-se à degradação da performance do modelo ao longo do tempo. Isso pode ocorrer por várias razões:

- **Mudança nas distribuições de dados**: Quando os dados usados para treinar o modelo não são mais representativos do padrão usado no treinamento do modelo.

- **Mudança nos padrões**: Novos padrões podem emergir nos dados que não estavam presentes ou eram menos prevalentes durante o treinamento.

- **Evolução dos objetivos de negócios**: O objetivo ou contexto do modelo pode mudar, requerendo uma atualização ou re-treinamento do modelo.

## Data Drift (ou "Desvio de Dados"):

Refere-se a mudanças na distribuição dos dados de entrada que alimentam o modelo. Existem dois tipos principais de Data Drift:

- **Covariate Drift:** Mudanças na distribuição das features (variáveis independentes). Por exemplo, se um modelo foi treinado com dados onde a média de uma feature era A, mas agora a média dessa feature é B, isso pode afetar a performance do modelo.

- **Label Drift:** Mudanças na distribuição dos labels (variáveis dependentes). Isso é especialmente relevante em problemas de classificação, onde a proporção de classes pode mudar ao longo do tempo.

Detectar e corrigir Model Drift e Data Drift é importante para garantir a eficácia contínua dos modelos de Machine Learning. Estratégias comuns incluem:

- Monitoramento contínuo da performance do modelo.

- Re-treinamento periódico do modelo com dados mais recentes.

- Implementação de pipelines de dados que permitam uma atualização automática dos dados usados para treinar o modelo.

> Manter os modelos atualizados e os dados representativos é essencial para evitar problemas de drift e garantir que os modelos continuem a fornecer insights precisos e valiosos.

## Importância de Model e Data Drift no Contexto de Machine Learning

Em um ambiente de Machine Learning, os dados utilizados para treinar e validar modelos são geralmente uma amostra do comportamento passado de um sistema ou processo. No entanto, os sistemas e processos são dinâmicos e podem mudar devido a uma variedade de fatores, resultando em um desvio entre os dados usados no treinamento do modelo e os dados que o modelo encontra após ser colocado em produção.

Model Drift refere-se à degradação da performance do modelo ao longo do tempo. Isso pode ocorrer quando os padrões nos dados mudam, quando surgem novas variáveis que não estavam presentes no treinamento inicial ou quando os objetivos de negócios evoluem. A degradação na performance do modelo pode levar a previsões imprecisas e a decisões baseadas em insights desatualizados, o que pode ter um impacto negativo em operações e estratégias de negócios. Manter o modelo atualizado e re-treiná-lo regularmente com dados novos é essencial para assegurar que o modelo continue a fornecer resultados precisos e úteis.

Data Drift, por outro lado, refere-se a mudanças na distribuição dos dados de entrada que alimentam o modelo. Isso pode acontecer devido a mudanças sazonais, tendências de mercado, mudanças no comportamento do usuário ou qualquer outro fator que altere a natureza dos dados. Quando ocorre Data Drift, as previsões do modelo podem se tornar menos precisas porque o modelo foi treinado em dados que não são mais representativos da realidade atual. Detectar e responder a Data Drift é fundamental para manter a eficácia dos modelos de Machine Learning. Isso pode envolver monitorar continuamente os dados de entrada para identificar mudanças significativas e ajustar os modelos conforme necessário.

A identificação e a mitigação de Model Drift e Data Drift são essenciais para garantir que os modelos de Machine Learning permaneçam relevantes e precisos em um ambiente de dados em constante mudança. Isso envolve a implementação de práticas de monitoramento contínuo, a reavaliação periódica da performance do modelo e o ajuste ou re-treinamento dos modelos com dados atualizados. Ignorar esses aspectos pode levar a decisões empresariais baseadas em dados incorretos, resultando em perda de eficiência, aumento de custos e potencialmente perda de vantagem competitiva. Portanto, a gestão proativa de Model Drift e Data Drift é um componente vital de qualquer estratégia eficaz de Machine Learning.

## Técnicas e Métricas Para Identificar e Monitorar Data Drift

Para identificar e monitorar Data Drift, existem várias técnicas e métricas que podem ser aplicadas. Essas abordagens ajudam a detectar mudanças na distribuição dos dados de entrada, garantindo que os modelos de Machine Learning continuem a fornecer previsões precisas e confiáveis.


Uma das técnicas mais comuns para identificar Data Drift é o **monitoramento de distribuições estatísticas**. Comparar a distribuição dos dados atuais com a distribuição dos dados de treinamento pode revelar desvios significativos. Isso pode ser feito através de histogramas, gráficos de densidade ou box plots. Visualmente, essas ferramentas podem mostrar se há mudanças na média, variância ou forma geral dos dados.

Outra técnica é o uso de **testes estatísticos**. Testes como o Kolmogorov-Smirnov (KS), o Chi-Squared (Qui-Quadrado) e o Wasserstein Distance (também conhecido como Earth Mover's Distance) são úteis para comparar distribuições. O teste KS, por exemplo, mede a distância entre duas distribuições cumulativas, enquanto o Chi-Squared compara distribuições categóricas. O Wasserstein Distance é especialmente útil para dados contínuos, medindo a "quantidade de trabalho" necessária para transformar uma distribuição na outra.

**Métricas baseadas em Machine Learning** também podem ser empregadas para monitorar Data Drift. Uma abordagem comum é treinar um classificador para distinguir entre dados de treinamento e dados recentes. Se o classificador conseguir diferenciar facilmente entre os dois conjuntos de dados, isso indica a presença de drift. A acurácia desse classificador serve como uma métrica: uma acurácia alta sugere um Data Drift significativo.

Outra métrica útil é o **PSI** (Population Stability Index), que é amplamente utilizado no setor financeiro para monitorar mudanças na distribuição das variáveis ao longo do tempo. O PSI compara a distribuição de uma variável em um período com a distribuição em outro período. Um valor de PSI alto indica uma mudança significativa na distribuição da variável.

**Ferramentas de visualização** como dashboards podem ser configuradas para exibir métricas de drift em tempo real. Além disso, alertas automáticos podem ser configurados para notificar os analistas quando as métricas de drift ultrapassam certos limiares.

Em termos práticos, a **implementação de pipelines automatizados** que coletam, analisam e relatam data drift pode ser extremamente eficaz. Esses pipelines podem incluir a extração de amostras de dados recentes, a aplicação de técnicas e métricas de detecção de drift, e a geração de relatórios ou alertas para os stakeholders.

## Impactos do Model Drift

Model Drift pode impactar negativamente a eficácia de modelos de Machine Learning de várias maneiras. Aqui estão alguns dos principais impactos:

**Redução na Precisão**: A acurácia e outras métricas de desempenho do modelo podem diminuir ao longo do tempo se o modelo não for atualizado para refletir novas tendências e padrões nos dados.

**Aumento de Erros de Previsão**: O modelo pode começar a fazer previsões incorretas com maior frequência, levando a decisões erradas baseadas nessas previsões.

**Perda de Confiabilidade**: Usuários e stakeholders podem perder a confiança no modelo se perceberem que suas previsões não são mais confiáveis.

**Desempenho de Negócio Prejudicado**: Decisões de negócio baseadas em modelos desatualizados podem resultar em perda de receita, aumento de custos ou outras consequências negativas para o negócio.

**Risco Regulatório e de Compliance**: Em setores regulamentados, usar modelos que não estão mais precisos pode levar a violações de conformidade e regulamentação, resultando em multas ou outras penalidades.

**Desperdício de Recursos**: Manter e operar modelos que não estão mais precisos pode resultar em desperdício de recursos, tanto em termos de tempo quanto de dinheiro.

**Experiência do Cliente Prejudicada**: Modelos desatualizados podem impactar negativamente a experiência do cliente, por exemplo, em sistemas de recomendação, atendimento automatizado ou personalização de ofertas.

> Mitigar esses impactos envolve a implementação de estratégias de monitoramento contínuo, re-treinamento regular dos modelos e adaptação às mudanças nos dados e no ambiente de negócio.

## Mitigação de Model Drift

Mitigar o Model Drift pode envolver a implementação de várias estratégias para garantir que os modelos de Machine Learning permaneçam precisos e relevantes ao longo do tempo. Aqui estão algumas das principais estratégias:

### Monitoramento Contínuo

Monitoramento de Desempenho: Acompanhar continuamente métricas de desempenho do modelo, como acurácia, precisão, recall e F1-score, para detectar quaisquer degradações.

Monitoramento de Dados: Monitorar as distribuições dos dados de entrada e saída para identificar mudanças significativas nos padrões dos dados.

### Re-Treinamento Regular

Agendado: Re-treinar o modelo em intervalos regulares, como semanalmente ou mensalmente.

Baseado em Desempenho: Re-treinar o modelo quando as métricas de desempenho caírem abaixo de um certo limiar.

### Atualização de Dados

Incorporação de Novos Dados: Incorporar novos dados no conjunto de treinamento para refletir as mudanças nos padrões dos dados.

Amostragem Temporal: Usar amostragem temporal para garantir que os dados mais recentes sejam representados no treinamento.

### Modelos de Ensemble

Utilizar técnicas de ensemble, como bagging, boosting e voting, para combinar previsões de múltiplos modelos, o que pode ajudar a mitigar o impacto do drift.

### Ajuste de Hiperparâmetros

Regularmente ajustar hiperparâmetros do modelo para garantir que ele permaneça otimizado para os dados atuais.

### Validação Cruzada Contínua

Implementar validação cruzada contínua para avaliar o desempenho do modelo em diferentes subconjuntos de dados ao longo do tempo.

### Estratégias de Amostragem

Sobreamostragem e Subamostragem: Aplicar técnicas de sobreamostragem (como SMOTE) e subamostragem para lidar com desbalanceamentos de dados que podem surgir ao longo do tempo.

Amostragem Adaptativa: Ajustar dinamicamente a amostragem de dados com base nas mudanças observadas nas distribuições de dados.
Feature Engineering Dinâmico

Atualizar regularmente as features usadas pelo modelo para garantir que elas reflitam as mudanças nos dados e no contexto do problema.

### Implementação de Feedback Loop

Incorporar feedback contínuo dos usuários e do ambiente de produção para ajustar e melhorar o modelo.

### Deploy de Modelos de Backup

Manter modelos de backup prontos para serem implementados caso o modelo principal apresente desempenho insatisfatório.

### Utilização de Técnicas de Detecção de Drift

Implementar algoritmos específicos de detecção de drift, como KS Test, ADWIN ou DDM (Drift Detection Method), para identificar automaticamente mudanças nos dados.

## Ferramentas de Monitoramento

Existem várias ferramentas disponíveis para monitorar o desempenho e a integridade dos modelos de Machine Learning, ajudando a detectar e mitigar o Model Drift. Aqui estão algumas das principais ferramentas:

- Evidently AI
- Neptune.ai
- Arize AI
- Fiddler AI
- Seldon Deploy
- WhyLabs
- Prometheus + Grafana
- AWS SageMaker Model Monitor

## Links
What is model drift?
https://www.ibm.com/topics/model-drift

What is data drift?
https://www.softwareag.com/en_corporate/resources/data-integration/article/data-drift.html