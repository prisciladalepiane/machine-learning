# Engenharia de Atributos

## O Que é Engenharia de Atributos?

Engenharia de atributos, ou feature engineering, trata-se da técnica de usar o conhecimento do domínio para selecionar, modificar ou criar novos atributos (também chamados de features) a partir dos dados brutos, com o objetivo de melhorar o desempenho dos modelos de aprendizado de máquina.

Essa prática é importante porque a qualidade e a relevância dos atributos inseridos em um modelo têm um impacto significativo na capacidade do modelo de aprender e fazer previsões ou classificações precisas.

Por vezes, dados brutos não estão imediatamente prontos para serem eficazmente utilizados por modelos de aprendizado de máquina, seja devido à presença de ruído, valores faltantes ou simplesmente porque a informação relevante não está sendo apresentada de uma forma que os modelos possam facilmente aproveitar.

A engenharia de atributos envolve várias técnicas, como:

**Seleção de Atributos:** Identificar e selecionar as variáveis mais relevantes para o problema em questão.

**Transformação de Atributos:** Aplicar transformações matemáticas ou estatísticas para alterar a escala ou a distribuição dos dados.

**Criação de Atributos:** Derivar novos atributos a partir dos existentes, por exemplo, combinando duas colunas de dados para criar uma nova que capture uma interação relevante.

**Codificação de Variáveis Categóricas:** Converter variáveis categóricas, como gênero ou país, em uma forma numérica que os modelos de aprendizado de máquina possam processar, utilizando técnicas como codificação one-hot ou ordinal.

**Normalização ou Padronização:** Ajustar a escala dos atributos para que tenham uma distribuição mais uniforme, o que pode ajudar na convergência dos algoritmos de aprendizado.

A engenharia de atributos é frequentemente vista como uma arte tanto quanto uma ciência, pois requer intuição, criatividade e um profundo entendimento dos dados, além de um conhecimento sólido dos algoritmos de aprendizado de máquina a serem aplicados.

É um processo iterativo e pode consumir uma grande parte do tempo em um projeto de aprendizado de máquina, mas é essencial para construir modelos eficazes e precisos.

## Técnicas de Engenharia de Atributos

As técnicas de engenharia de atributos podem ser amplamente categorizadas com base em seu propósito e na natureza dos dados com os quais estão lidando.

Detalhamos a seguir algumas das técnicas mais comuns utilizadas na engenharia de atributos:

### 1. Seleção de Atributos
**Filtragem:** Usa estatísticas para selecionar atributos baseando-se em seu relacionamento com a variável alvo.

**Wrapper methods:** Usam um modelo preditivo para avaliar a importância dos atributos, selecionando aqueles que melhoram a performance do modelo.

**Embedded methods:** Integram a seleção de atributos como parte do processo de treinamento do modelo, como é o caso de modelos que utilizam regularização.

### 2. Extração e Criação de Atributos
**Análise de Componentes Principais (PCA):** Reduz a dimensionalidade dos dados ao transformá-los em um conjunto menor de variáveis sumárias (componentes) que retêm a maior parte da variabilidade original dos dados.


**Engenharia de Atributos Temporais:** Derivação de novos atributos a partir de variáveis de tempo, como hora do dia, dia da semana, diferenças de tempo entre eventos etc.

**Combinação e Transformação de Atributos:** Criação de novos atributos por meio da combinação ou transformação de atributos existentes, como somar, subtrair, multiplicar ou dividir duas ou mais colunas.

### 3. Tratamento de Dados Categóricos

**Codificação One-Hot:** Transforma variáveis categóricas em uma forma que possa ser fornecida aos algoritmos de ML, criando uma nova coluna binária para cada categoria.

**Codificação de Frequência:** Substitui as categorias pela frequência (ou porcentagem) de sua ocorrência nos dados.

**Codificação Target (Mean encoding):** Substitui a categoria pelo valor médio da variável alvo para essa categoria.

### 4. Normalização e Padronização
**Normalização (Min-Max Scaling)**: Escala os atributos para que fiquem dentro de um intervalo específico, geralmente entre 0 e 1.

**Padronização (Z-score normalization):** Transforma os atributos para que tenham média 0 e desvio padrão 1.

### 5. Tratamento de Dados Faltantes

**Imputação:** Substituição de valores faltantes por um valor estimado com base em outras observações.
**Indicadores de Dados Faltantes:** Criação de novos atributos que indicam a presença de dados faltantes em outros atributos.

### 6. Tratamento de Dados Desbalanceados
**Sobreamostragem (Oversampling) ou Subamostragem (Undersampling):** Ajusta o balanceamento das classes alvo por meio da replicação de exemplos da classe minoritária ou remoção de exemplos da classe majoritária.

**SMOTE**: Técnica de sobreamostragem que cria exemplos sintéticos da classe minoritária.

### 7. Detecção e Tratamento de Outliers
**Métodos estatísticos:** Uso de scores Z ou intervalos interquartis (IQR) para identificar outliers.

**Truncamento ou Capping**: Limitação de valores extremos a um certo limite definido.

Cada uma dessas técnicas pode ser aplicada conforme necessário, dependendo do conjunto de dados específico e do problema que está sendo resolvido.

A escolha e aplicação eficaz dessas técnicas podem significativamente melhorar a qualidade do modelo de aprendizado de máquina, impactando diretamente seu desempenho e precisão.


## Importância da Qualidade dos Atributos

A qualidade dos atributos é fundamental no aprendizado de máquina porque determina a capacidade dos modelos de aprender padrões significativos nos dados e fazer previsões ou classificações precisas.

A seleção, criação e otimização de bons atributos são etapas essenciais que podem impactar diretamente o sucesso ou fracasso de um projeto de aprendizado de máquina.

Vejamos a seguir  os principais motivos que tornam a qualidade dos atributos tão importante:

### 1. Melhora o Desempenho do Modelo

Atributos de alta qualidade fornecem informações claras e relevantes que facilitam a tarefa do modelo em identificar padrões.
Modelos alimentados com dados bem preparados tendem a alcançar uma precisão mais alta, menor taxa de erro e melhor generalização para dados não vistos.

### 2. Facilita a Convergência do Modelo
Atributos bem selecionados e adequadamente preparados ajudam a otimizar o processo de treinamento, permitindo que o modelo alcance a convergência mais rapidamente.

Isso é particularmente importante em modelos complexos, onde o custo computacional do treinamento pode ser significativo.

### 3. Reduz a Complexidade do Modelo
A eliminação de atributos irrelevantes ou redundantes através de técnicas de seleção de atributos pode reduzir a complexidade do modelo.

Modelos mais simples são geralmente mais rápidos para treinar, mais fáceis de interpretar e manter, e menos propensos ao overfitting.

### 4. Melhora a Interpretabilidade
Modelos construídos com atributos de alta qualidade e bem entendidos são mais fáceis de interpretar.

Isso é essencial para aplicações em que a tomada de decisões precisa ser explicada ou justificada, como em contextos financeiros, médicos ou jurídicos.

### 5. Adequação aos Diferentes Tipos de Dados e Modelos
Cada modelo de aprendizado de máquina tem suas próprias exigências quanto ao tipo, escala e distribuição dos atributos de entrada.
A qualidade dos atributos influencia diretamente a compatibilidade com diferentes algoritmos, maximizando a eficácia do modelo escolhido.

### 6. Gestão de Dados Faltantes e Outliers
O tratamento cuidadoso de dados faltantes e outliers é parte da engenharia de atributos.
Atributos de qualidade são aqueles que foram devidamente tratados para minimizar distorções e viéses no modelo causados por anomalias nos dados.

### 7. Adaptação a Mudanças nos Dados
Em ambientes dinâmicos, onde os padrões de dados podem mudar com o tempo (drift de conceito), atributos de alta qualidade permitem uma melhor adaptação a essas mudanças, mantendo a precisão do modelo ao longo do tempo.

A qualidade dos atributos é um dos pilares mais importantes do aprendizado de máquina, impactando diretamente a eficácia, eficiência, e aplicabilidade dos modelos gerados.

Investir tempo e recursos na engenharia de atributos é fundamental para o sucesso de qualquer projeto de aprendizado de máquina.

## Seleção de Atributos

A seleção de atributos, também conhecida como seleção de variáveis ou seleção de características, é um processo crítico na preparação de dados para modelagem de aprendizado de máquina.

Seu objetivo é identificar e selecionar os atributos (ou variáveis) mais relevantes para a tarefa preditiva, removendo os dados irrelevantes ou redundantes.

Isso não apenas pode melhorar o desempenho do modelo, mas também tornar o modelo mais eficiente, reduzindo o tempo de treinamento e simplificando o modelo, o que, por sua vez, pode facilitar a interpretação.

### Por que é Seleção de Atributos é Importante?

**Reduz a Complexidade do Modelo**: Diminuir o número de atributos pode simplificar o modelo, tornando-o mais rápido para treinar e mais fácil de entender e interpretar.

**Melhora o Desempenho**: Remover dados irrelevantes ou redundantes pode melhorar a precisão do modelo, pois o modelo não é mais distraído por ruídos nos dados.

**Previne Overfitting:** Menos atributos significam menos oportunidades para o modelo aprender o ruído nos dados de treinamento como se fossem padrões significativos, o que pode melhorar a capacidade do modelo de generalizar para novos dados.

Reduz o Tempo de Treinamento: Menos dados significam que os algoritmos de aprendizado de máquina podem processar mais rápido, reduzindo o tempo necessário para treinar os modelos.


### Técnicas Comuns de Seleção de Atributos

#### 1. Métodos de Filtragem (Filter Methods)
Essas técnicas aplicam um critério estatístico para avaliar a relação entre cada atributo e a variável alvo, independentemente do modelo.

Exemplos incluem:

* **Correlação**: Seleciona atributos com base na força da correlação (positiva ou negativa) com a variável alvo.

* **Testes estatísticos:** Chi-quadrado, testes ANOVA, etc., para avaliar a importância dos atributos.



#### 2. Wrapper Methods
Esses métodos avaliam subconjuntos de atributos, criando modelos usando esses subconjuntos e calculando a qualidade do modelo para determinar a importância dos atributos.

Exemplos incluem:

* **RFE** (Recursive Feature Elimination): Iterativamente constrói modelos e remove o pior ou os piores atributos, continuando este processo até que o número desejado de atributos seja alcançado.

* Métodos de **busca sequencial**: Como busca sequencial para frente (forward selection) e busca sequencial para trás (backward elimination).


#### 3. Embedded Methods
Integram a seleção de atributos como parte do processo de treinamento do modelo e são específicos para determinados tipos de modelos. Esses métodos aproveitam a penalização (como L1/Lasso e L2/Ridge) para adicionar custos aos atributos, efetivamente realizando seleção de atributos enquanto o modelo é treinado.

Exemplos incluem:

* Modelos baseados em penalidades: Lasso (L1), que pode reduzir os coeficientes de alguns atributos para zero, efetivamente selecionando um subconjunto de atributos úteis.

* Árvores de decisão e modelos baseados em árvores: Como Random Forests e Gradient Boosting, que podem avaliar a importância dos atributos com base na sua contribuição para a melhoria do modelo.

A escolha da técnica de seleção de atributos depende do tipo de dados, do problema específico e do tipo de modelo que se pretende utilizar.

Em muitos casos, uma combinação de métodos pode ser usada para alcançar os melhores resultados.

A seleção de atributos é um passo iterativo e primordial no processo de modelagem de aprendizado de máquina, que pode significativamente impactar o sucesso do projeto.

# Feature Store em Machine Learning

Uma Feature Store é um componente vital no ecossistema de Machine Learning (ML), projetado para abordar desafios comuns na engenharia de atributos (features) ao desenvolver e implantar modelos de ML.

Ela serve como um repositório centralizado para armazenar, gerenciar e servir atributos usados para treinamento de modelos e inferência em produção. A introdução deste conceito veio da necessidade de harmonizar o processo de engenharia de atributos entre as equipes de dados e a produção, melhorando a eficiência, a consistência e a qualidade dos modelos de ML.

## Benefícios de uma Feature Store

**Eficiência Operacional**: Reduz a complexidade e o tempo necessário para preparar e servir atributos, acelerando o desenvolvimento de modelos de ML.

**Consistência de Dados**: Assegura que o mesmo processo de transformação de dados seja aplicado durante o treinamento e a inferência, melhorando a precisão e a confiabilidade dos modelos.

**Colaboração**: Incentiva a colaboração entre cientistas de dados, engenheiros de dados e engenheiros de ML, através do compartilhamento e reutilização de atributos.

**Escalabilidade e Desempenho:** Projetada para lidar com grandes volumes de dados e requisitos de desempenho, permitindo escalabilidade horizontal e processamento eficiente.

A implementação de uma feature store pode variar desde soluções personalizadas construídas in-house até plataformas comerciais e open-source. Alguns exemplos populares incluem Tecton, Feast e Hopsworks.
A escolha da solução certa depende das necessidades específicas da organização, incluindo escalabilidade, complexidade dos atributos e integração com o ecossistema de dados existente.

## Operações Em Uma Feature Store

As operações realizadas em uma Feature Store abrangem a gestão do ciclo de vida das features, desde a sua criação até a sua utilização em modelos de Machine Learning, tanto em ambientes de treinamento quanto de inferência. 

Etapas Para Categorizar Operações em Feature Store:

### 1. Definição e Criação de Features

Defina e especifique novas features, incluindo sua lógica de cálculo, fontes de dados necessárias e metadados associados (como tipo de dado, frequência de atualização, etc.).
Faça o desenvolvimento de pipelines de ETL (Extract, Transform, Load) para extrair dados brutos, transformá-los na feature desejada e carregá-los na feature store.

### 2. Armazenamento e Versionamento

Atente-se para o armazenamento seguro das features definidas, juntamente com seus metadados. A feature store deve ser capaz de armazenar dados em diferentes granularidades temporais e versões.
Mantenha a gestão de diferentes versões das features para suportar experimentação e mudanças nos processos de cálculo ou nas fontes de dados.

### 3. Transformações em Tempo Real e em Lote

Realize o processamento de grandes volumes de dados para atualizar as features armazenadas, geralmente em um ciclo regular (por exemplo, diariamente).
Faça os cálculo de features em tempo real, normalmente para casos de uso de inferência onde a latência é crítica.

### 4. Descoberta e Reutilização

Use uma interface de usuário ou API que permite aos usuários pesquisar e descobrir features existentes, promovendo a reutilização e evitando o trabalho duplicado.
Compartilhe ferramentas que facilitam o compartilhamento de features entre equipes, incluindo a documentação e os exemplos de uso.

### 5. Serviço de Features para Treinamento e Inferência

Assegure o fornecimento de conjuntos de dados de features consistentes e prontos para uso para treinar modelos de Machine Learning.
Atente-se ao fornecimento de features em tempo real ou quase real para aplicações de inferência, garantindo baixa latência.

### 6. Monitoramento e Governança

Monitore e  verifique a qualidade e da integridade das features armazenadas, incluindo a detecção de dados ausentes ou anômalos.
Faça a implementação de controles de acesso, auditoria de uso e conformidade com políticas de privacidade e segurança de dados.

### 7. Atualização e Manutenção

Crie processo para atualizar ou depreciar features, garantindo que o catálogo reflita as necessidades atuais dos usuários.
Manutenção a atualização e otimização dos pipelines de ETL conforme necessário para garantir eficiência e precisão.

> A Feature Store, portanto, atua como uma peça central na infraestrutura de Machine Learning, abordando desafios de engenharia de dados, governança e operacionalização de modelos, e facilitando a colaboração entre diferentes equipes.


## Versionamento e Governança de Atributos

O versionamento e a governança de atributos são aspectos críticos na gestão de uma Feature Store, essenciais para garantir a integridade, a reprodutibilidade e a conformidade dos processos de Machine Learning (ML).

Esses conceitos desempenham papéis fundamentais no ciclo de vida dos atributos, desde a sua criação até a sua utilização em modelos de ML, tanto em ambientes de desenvolvimento quanto de produção.

### Versionamento de Atributos

O versionamento de atributos refere-se à prática de manter diferentes versões de um atributo ao longo do tempo. Isso é importante por várias razões, as quais destacamos:

**Reprodutibilidade**: Permite que modelos de ML sejam re-treinados ou validados com exatamente os mesmos dados utilizados anteriormente, assegurando a reprodutibilidade dos resultados.

**Experimentação**: Facilita a experimentação com diferentes versões de atributos para avaliar o impacto no desempenho do modelo.

**Atualizações e Correções**: Quando a lógica de processamento de um atributo muda ou erros são corrigidos, o versionamento permite que essas alterações sejam implementadas sem perder o acesso às versões anteriores.

### Governança de Atributos
A governança de atributos abrange um conjunto de políticas, procedimentos e controles destinados a gerenciar o acesso, a qualidade, a segurança e a conformidade dos dados ao longo de seu ciclo de vida. Ela é fundamental para:

**Segurança e Privacidade:** Assegurar que os dados sejam acessados e utilizados de forma segura, em conformidade com regulamentações de privacidade de dados como GDPR e CCPA.

**Controle de Acesso**: Definir quem tem permissão para criar, acessar, modificar ou excluir atributos, garantindo que apenas usuários autorizados possam realizar essas ações.

**Qualidade de Dados**: Implementar mecanismos para monitorar e manter a alta qualidade dos atributos, incluindo a precisão, a completude e a atualidade dos dados.

**Auditoria e Conformidade**: Registrar o acesso e o uso dos atributos para fins de auditoria, facilitando a análise de como os dados são utilizados e por quem, além de garantir a conformidade com políticas internas e regulamentações externas.

> O versionamento e a governança de atributos são fundamentais para o sucesso de projetos de ML, pois garantem que os dados utilizados sejam precisos, consistentes, seguros e em conformidade com as regulamentações aplicáveis.

## Integração da Feature Store com Pipelines de Machine Learning

A integração de uma Feature Store com pipelines de Machine Learning (ML) é um passo essencial para otimizar o ciclo de vida de desenvolvimento e implantação de modelos de ML.

Esta integração permite uma gestão eficaz das features (atributos) usadas nos modelos, melhorando a eficiência, a consistência e, em última análise, a performance dos modelos de ML.

Segue abaixo alguns dos aspectos fundamentais desta integração:

### 1. Centralização de Features

A Feature Store atua como um repositório central para armazenar e gerenciar features, o que facilita a reutilização de features entre diferentes modelos e projetos de ML. Isso reduz significativamente o trabalho redundante de engenharia de features e assegura a consistência dos dados usados durante o treinamento e a inferência.

### 2. Padronização dos Processos de Engenharia de Features

Integrar a Feature Store com pipelines de ML padroniza o processo de criação, transformação, e armazenamento de features. Isso garante que as features sejam criadas de maneira uniforme, utilizando as mesmas fontes de dados e lógicas de transformação, independente do modelo ou projeto.

### 3. Automatização da Atualização de Features

A integração permite a automatização das atualizações de features, assegurando que os modelos de ML sempre tenham acesso às versões mais recentes e relevantes dos atributos. Isso é particularmente importante em ambientes dinâmicos, onde os dados podem mudar frequentemente.

### 4. Facilidade de Acesso para Treinamento e Inferência

Uma integração eficaz permite que os pipelines de ML acessem facilmente as features armazenadas, tanto para treinamento quanto para inferência, através de interfaces de programação de aplicativos (APIs) ou bibliotecas cliente. Isso simplifica o processo de alimentação dos modelos com os dados necessários, independente de estarem em ambientes de desenvolvimento, teste ou produção.

### 5. Monitoramento e Governança

Integrar a Feature Store com os pipelines de ML facilita o monitoramento do uso das features e a aplicação de políticas de governança de dados. Isso inclui controle de acesso, auditoria de modificações, e acompanhamento da performance das features em termos de impacto nos modelos de ML.

> Ao integrar de forma eficiente a Feature Store com os pipelines de ML, as organizações podem acelerar o desenvolvimento de modelos, melhorar a qualidade e a consistência das previsões e facilitar a colaboração entre as equipes de dados e ML.

## Casos de Uso e Benefícios da Feature Store

As Feature Stores desempenham um papel essencial na simplificação e na otimização dos pipelines de Machine Learning (ML), trazendo uma série de benefícios que se estendem por diversas aplicações e casos de uso.

### Sistemas de Recomendação
**Descrição:** Sistemas de recomendação personalizam a experiência do usuário ao sugerir produtos, serviços ou conteúdos com base no comportamento passado e preferências do usuário.

**Benefício:** Centraliza as features de interação do usuário e de produtos para garantir recomendações consistentes e atualizadas em tempo real.

### Manutenção Preditiva
**Descrição**: Monitora equipamentos ou sistemas para prever falhas antes que ocorram, permitindo manutenção preventiva.

**Benefício:** Armazena históricos de dados de sensor e padrões de uso para treinar modelos que preveem falhas, melhorando a eficiência operacional.

### Personalização de Conteúdo
**Descrição**: Adapta o conteúdo digital (como notícias, feeds de redes sociais, ou resultados de pesquisa) aos interesses e ao histórico de interação do usuário.

**Benefício**: Agrega e disponibiliza features relacionadas ao comportamento do usuário e à interação com o conteúdo, permitindo personalizações mais precisas.

### Previsão de Demanda
**Descrição**: Estima a demanda futura por produtos ou serviços, ajudando na otimização do estoque e na gestão da cadeia de suprimentos.

**Benefício**: Facilita a modelagem preditiva ao prover features históricas de vendas, tendências de mercado e dados sazonais de forma centralizada e consistente.

> A implementação de uma Feature Store oferece uma infraestrutura robusta que suporta as necessidades de desenvolvimento de modelos de ML de ponta a ponta, desde a criação de features até a implantação e monitoramento em produção, em uma variedade de aplicações e indústrias.

---

What Is a Feature Store?
https://www.tecton.ai/blog/what-is-a-feature-store/

O Que São Feature Stores e Por Que São Essenciais na Escalabilidade em Data Science?
https://www.cienciaedados.com/o-que-sao-feature-stores-e-por-que-sao-essenciais-na-escalabilidade-em-data-science/