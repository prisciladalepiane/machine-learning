# Descrevendo o Processo de Construção de Modelos de Machine Learning:

## Processos:

### Entendimento do Domínio:
O processo de construção de modelos ml começa com entendimento profundo do domínio ou do do campo de estudo em questão. Isso envolve um mergulho nas especificidades da área. Este passo é fundamental pois fornece o contexto necessário para as decisões posteriores no ciclo de vida do projeto.

### Coleta e Preparação dos dados:
Coletar e preparar os dados que alimentarão o modelo.
Trabalho as vezes de um engenheiro de dados. 
Isso envolve identificar as fontes de dados, reunir os conjuntos necessários e realizar tarefas de limpeza e pré-processamento para garantir que os dados sejam consistentes e çivres de erros ou ruídos

O Aramazenamento de dados de forma bem estruturada é importante.
[Exemplo de uma modelagem de banco de dados](https://github.com/prisciladalepiane/banco_de_dados/blob/main/Atividades/Atividade_e_DER_telemedicina.pdf)

### Exploração e Análise de Dados
Explorar e analisar os dados para entender a estrutura, distribuição e padrões. Pode envolver visualização, cálculos de estatísticas descritivas e a identificação de possíveis anomalias ou *outliers*.
Pode ser feito por um analista ou cientista de dados.

### Seleção e Engenharia de Atributos
Nem todas as características dos dados podem ser relevantes ou úteis para a modelagem. A seleção de atributos envolve escolher os atributos que são mais informativos.
A engenharia de atributos envolve criar novos atributos a partir dos existentes para melhor representar os padrões nos dados.
Geralmente trabalho de um cientista de dados.

### Construção e Avaliação de Modelos
Os modelos de ML são construídos usando os dados preparados. É avaliado o desempenho em um conjunto de dados de teste para entender sua precisão, robustez e generalização.
Escolher o algoritmo ideal para o problema definido, experimentando vários métodos possíveis para resolver o problema. 
Escolher o modelo mais próximo do ideal.

### Otimização de Hiperparâmetros
Parâmetros (coeficientes) são aprendidos pelo modelo durante o treinamento do modelo. 
Hiperâmetros (parâmetros de funções em programação) ajudam o modelo no processo de treinamento e precisam ser definidos previamente. 
A otimização de hiperparâmetros  envolve experimentar diferentes valores para encontrar a combinação que produz o melhor desempenho do modelo.

### Validação Cruzada 
Avalia a capacidade de generalização de um modelo.
Divide o conjunto de dados em partições, treina e testa o modelo em diferentes combinações dessas partições para garantir que o modelo funciona em em dados novos.
Se o modelo não performar bem no conjunto de teste podemos
ter um problema de underfitting ou overfitting.

### Deploy do Modelo
Geralmente atribuição para um engenheiro de Machine Learning ou engenheiro de IA.
Implementação do modelo que já foi finalizado e otimizado.
O modelo é disponibilizado em um ambiente onde pode receber novos dados, processá-los e fornecer previsões em tempo real.

### Iteração e Melhoria Contínua
O padrão dos dados pode mudar (*data drift*), por isso pode ser necessário revisitar e reavaliar o modelo. Se necessário refinar ou reconstruir o modelo para que ele permaneça relevante e eficaz.

## Exemplo de Processo para a área de logística:

Problema: Uma  das  questões  cruciais  enfrentadas  pelas  empresas  de  logística  é  a  identificação rápida e precisa do conteúdo das embalagens, para garantir que sejam manuseadas de maneira adequada, evitando danos. Muitas vezes, as embalagens externas não dão indicaçõesclaras sobre o seu conteúdo, o que pode levar a tratamentos inadequados e, consequentemente, a custos adicionais e insatisfação do cliente. 

Solução Proposta: Desenvolver um modelo de Machine Learning que, com base em duas variáveis simples: o peso do pacote e o tipo de embalagem, seja capaz de prever o produto eletrônico contido dentro  da  embalagem.  Este  modelo  permitirá  que  os  funcionários  do  centro  logístico rapidamente identifiquem e classifiquem os pacotes, garantindo que cada produto receba o tratamento adequado durante o processo logístico.

Coleta de dados: Será essencial coletar dados sobre o peso e tipo de embalagem de diferentes produtos eletrônicos. Esse dataset será a base para o treinamento do modelo.

Desenvolvimento  do  Modelo:  Utilizando  técnicas  modernas  de  Machine  Learning,  o modelo será treinado para correlacionar peso e tipo de embalagem com o produto eletrônico específico.

Avaliação e Otimização: Uma vez treinado, o modelo será avaliado em sua capacidade de prever  com  precisão  o  conteúdo  das  embalagens  em  um  conjunto  de  dados  de  teste. Dependendo dos resultados, ajustes e otimizações podem ser necessários.

Deploy: Com o modelo treinado e otimizado, ele será implantado em uma aplicação web, permitindo que os funcionários do centro logístico insiram o peso e o tipo de embalagem e recebam uma previsão do conteúdo da embalagem em tempo real.
