# Deep Learning para aplicações Biomédicas

## Redes Neurais Artificiais

Redes Neurais Artificiais (RNAs) são modelos computacionais inspirados pelo funcionamento do cérebro humano, projetadas para reconhecer padrões complexos e fazer previsões baseadas em grandes conjuntos de dados.

Elas consistem em camadas de nós, ou "neurônios", que são conectados de maneira semelhante às sinapses no cérebro. Cada conexão tem um peso associado que é ajustado durante o treinamento para minimizar o erro nas previsões do modelo.

As RNAs são particularmente úteis em tarefas onde as relações entre as variáveis de entrada e saída não são lineares ou facilmente modeladas por algoritmos tradicionais.

> O treinamento de uma rede neural envolve a alimentação de dados de entrada através da rede e a comparação da saída prevista com a saída desejada. Este processo, conhecido como retropropagação, ajusta os pesos das conexões para reduzir o erro.

O algoritmo de aprendizado mais comum utilizado nesse processo é o gradiente descendente, que atualiza iterativamente os pesos na direção que minimiza o erro.

A complexidade das RNAs permite que elas capturem padrões sutis e complexos nos dados, tornando-as extremamente poderosas para tarefas como reconhecimento de imagem, processamento de linguagem natural e diagnóstico médico.


As aplicações biomédicas das RNAs são amplas e impactantes. Em diagnósticos médicos, por exemplo, elas podem analisar imagens médicas, como radiografias e ressonâncias magnéticas, para identificar anomalias que poderiam passar despercebidas ao olho humano.

Além disso, RNAs são usadas para prever a progressão de doenças, personalizar tratamentos baseados no perfil genético do paciente e até descobrir novos medicamentos.

O uso de RNAs em biomedicina não só aumenta a precisão e eficiência dos diagnósticos e tratamentos, mas também abre novas fronteiras na compreensão e combate a doenças complexas.

## Arquiteturas de Deep Learning

Arquiteturas de Deep Learning, ou Aprendizado Profundo, referem-se a configurações específicas de redes neurais profundas projetadas para lidar com diferentes tipos de dados e tarefas.

Entre as arquiteturas mais conhecidas estão: 

- **Redes Neurais Convolucionais (CNNs):** são amplamente utilizadas para tarefas de visão computacional, como <u> reconhecimento de imagem e detecção de objetos</u>. Elas são compostas por camadas convolucionais que aplicam filtros a pequenas regiões da imagem de entrada, permitindo a extração de características locais, como bordas e texturas. Estas camadas são seguidas por camadas de pooling, que reduzem a dimensionalidade dos dados, e camadas totalmente conectadas, que realizam a classificação final. A capacidade das CNNs de capturar padrões espaciais hierárquicos as torna extremamente eficazes em tarefas que envolvem dados visuais.

- **Redes Neurais Recorrentes (RNNs):** são projetadas para lidar com <u> dados sequenciais </u>, como texto e séries temporais. As RNNs têm a capacidade de manter informações sobre estados anteriores através de laços internos em seus neurônios, o que lhes permite capturar dependências temporais e contextuais nos dados. No entanto, as RNNs tradicionais podem enfrentar problemas de longo prazo devido ao desaparecimento do gradiente. Para mitigar isso, arquiteturas avançadas como LSTMs (Long Short-Term Memory) e GRUs (Gated Recurrent Units) foram desenvolvidas, permitindo a modelagem de dependências de longo alcance de maneira mais eficaz.

- **Redes Generativas Adversariais (GANs):** representam outra arquitetura inovadora em Deep Learning, composta por duas redes neurais que competem entre si: uma rede geradora e uma rede discriminadora. A rede geradora cria novos exemplos de dados, enquanto a rede discriminadora avalia a autenticidade desses exemplos, diferenciando entre dados reais e gerados. Esse processo de competição resulta em melhorias contínuas em ambas as redes, levando a uma geração de dados sintéticos extremamente realista. As GANs têm sido aplicadas em uma variedade de campos, incluindo geração de imagens, síntese de voz e criação de conteúdo artístico, demonstrando seu <u> potencial para inovar na criação de novos dados e soluções </u>.

Arquiteturas de Deep Learning continuam a evoluir, com pesquisas contínuas explorando novas maneiras de melhorar a eficiência e a capacidade de generalização desses modelos.

Novas arquiteturas, como Transformadores, têm ganhado destaque especialmente em processamento de linguagem natural, devido à sua capacidade de modelar relações de longo alcance nos dados sem as limitações das RNNs tradicionais.

O desenvolvimento de arquiteturas híbridas que combinam diferentes abordagens também está se tornando cada vez mais comum, oferecendo soluções mais robustas e versáteis para uma ampla gama de problemas complexos.


### Redes Neurais Convolucionais em Imagens Médicas

Redes Neurais Convolucionais (CNNs) têm se mostrado extremamente eficazes na análise de imagens médicas devido à sua capacidade de extrair características relevantes automaticamente.

As CNNs aplicam filtros convolucionais às imagens de entrada, detectando padrões como bordas, texturas e formas que são essenciais para a interpretação médica. Esses filtros são ajustados durante o processo de treinamento, permitindo que a rede aprenda a identificar anomalias específicas em diferentes tipos de exames, como radiografias, tomografias e ressonâncias magnéticas.

Essa habilidade de automação na extração de características permite que as CNNs sejam aplicadas em diagnósticos e tratamentos médicos de forma eficiente.

Na prática, as CNNs são usadas para uma variedade de tarefas em imagens médicas, incluindo a segmentação de tecidos, a detecção de tumores e a classificação de doenças. Por exemplo, na detecção de câncer, as CNNs podem analisar mamografias para identificar a presença de microcalcificações ou massas suspeitas, auxiliando radiologistas na identificação precoce da doença.

Além disso, em exames de ressonância magnética cerebral, as CNNs podem segmentar diferentes regiões do cérebro e identificar áreas afetadas por doenças neurodegenerativas, como Alzheimer, ajudando a monitorar a progressão da doença e a avaliar a eficácia de tratamentos.

A adoção de CNNs em imagens médicas não apenas aumenta a precisão dos diagnósticos, mas também contribui para a padronização e a velocidade do processo.

As CNNs reduzem a variabilidade entre diferentes especialistas e podem processar grandes volumes de dados rapidamente, permitindo análises mais abrangentes e detalhadas.

Assim,  essas redes são continuamente aprimoradas através de grandes conjuntos de dados anotados por especialistas, melhorando sua capacidade de generalização e adaptabilidade a novos casos. Dessa forma, as CNNs estão transformando a prática médica, proporcionando ferramentas avançadas para apoiar decisões clínicas e melhorar os resultados dos pacientes.

### Redes Neurais Recorrentes em Dados Sequenciais

Redes Neurais Recorrentes (RNNs) são projetadas para lidar com dados sequenciais, tornando-as ideais para tarefas onde a ordem e a dependência temporal dos dados são importantes.

Isso é possível porque as RNNs possuem laços internos que permitem a retenção de informações de estados anteriores, facilitando a captura de padrões ao longo de uma sequência.

Essa característica torna as RNNs particularmente úteis em áreas como processamento de linguagem natural, análise de séries temporais e modelagem de dados temporais em diversas aplicações.

Em processamento de linguagem natural, as RNNs são amplamente utilizadas para tarefas como tradução automática, geração de texto e reconhecimento de fala. Elas podem analisar sentenças inteiras, levando em consideração a dependência entre palavras para entender contextos e significados.

No caso de traduções, as RNNs conseguem mapear frases de uma língua para outra, mantendo a coerência e a fluidez do texto. 

Em reconhecimento de fala, as RNNs processam sequências de áudio para converter discurso falado em texto, levando em conta as variações temporais na fala humana.


As RNNs também são aplicadas em análise de séries temporais, onde a previsão de valores futuros depende de informações passadas. 

Por exemplo, em finanças, RNNs são usadas para prever preços de ações baseados em dados históricos, enquanto em meteorologia, elas podem prever condições climáticas futuras com base em registros anteriores.

Entretanto, RNNs tradicionais enfrentam desafios com dependências de longo prazo devido ao problema de desvanecimento do gradiente.

Para resolver isso, variantes como LSTMs (Long Short-Term Memory) e GRUs (Gated Recurrent Units) foram desenvolvidas, proporcionando melhor desempenho ao capturar dependências de longo alcance e melhorando significativamente a eficácia dessas redes em diversas aplicações temporais.

## Autoencoders em Redução de Dimensão

Autoencoders são redes neurais projetadas para aprender representações eficientes dos dados, tornando-os particularmente úteis para a redução de dimensão. Eles funcionam através de uma arquitetura composta por duas partes: um codificador e um decodificador.

O codificador mapeia os dados de entrada para uma representação de menor dimensão, enquanto o decodificador reconstrói os dados de entrada a partir dessa representação compacta.

Esse processo de compressão e descompressão permite que os autoencoders capturem as características mais importantes dos dados, descartando informações redundantes.

Na prática, os autoencoders são usados em várias aplicações onde a redução de dimensão é benéfica. Em processamento de imagem, por exemplo, eles podem ser utilizados para reduzir o número de pixels, mantendo apenas as informações essenciais necessárias para a reconstrução da imagem original.

Isso além de facilitar o armazenamento e a transmissão de dados, também melhora o desempenho de algoritmos de aprendizado subsequentes, eliminando ruído e simplificando as entradas.

Além disso, em processamento de dados genômicos, os autoencoders podem ajudar a identificar padrões em grandes conjuntos de dados genéticos, permitindo uma análise mais eficiente e focada.

Outra aplicação significativa dos autoencoders é na detecção de anomalias. Ao treinar um autoencoder em dados normais, ele aprende a reconstruir esses dados com alta precisão.

No entanto, quando apresentado com dados anômalos, a reconstrução tende a ser pobre, pois o autoencoder não foi treinado para essas variações. Essa discrepância pode ser usada para identificar anomalias em diversos contextos, como detecção de fraudes em transações financeiras e monitoramento de sistemas industriais.

A capacidade dos autoencoders de reduzir dimensões e capturar a essência dos dados os torna uma ferramenta poderosa para análise e processamento de dados complexos.

## Arquitetura de Transformadores, Módulo de Auto Atenção e LLMs

A arquitetura de Transformadores revolucionou o campo do processamento de linguagem natural (PLN) ao introduzir uma maneira eficiente de lidar com dependências de longo alcance nos dados sequenciais.

Diferente das Redes Neurais Recorrentes (RNNs), que processam dados em ordem sequencial, os Transformadores utilizam um mecanismo de atenção que permite o processamento paralelo de todos os tokens de entrada.

Essa abordagem reduz significativamente o tempo de treinamento e melhora a capacidade de modelar relações complexas entre palavras em um texto.

> O módulo de Auto-Atenção é o componente central dos Transformadores. Ele funciona calculando a atenção que cada token da sequência deve dar a todos os outros tokens. 

Esse cálculo é feito através de três vetores: chave, consulta e valor. A consulta de um token é comparada com as chaves de todos os tokens para determinar o quanto deve ser "atento" a cada um deles, resultando em pesos de atenção.

Esses pesos são então aplicados aos valores para gerar uma representação ponderada da sequência, permitindo que a rede capture dependências contextuais sem a necessidade de processamento sequencial.

Modelos de Linguagem de Grande Escala (LLMs) são baseados na arquitetura de Transformadores e se destacam por suas capacidades impressionantes em diversas tarefas de PLN.

Esses modelos são treinados em vastos corpora de texto, permitindo-lhes aprender representações profundas e contextuais da linguagem.

LLMs podem ser usados para tarefas como tradução automática, resumo de texto, resposta a perguntas e geração de texto.
A flexibilidade e eficiência dos Transformadores, combinadas com a capacidade de lidar com grandes quantidades de dados, fazem dos LLMs ferramentas poderosas para avançar o estado da arte em processamento de linguagem natural e outras aplicações de Inteligência Artificial.

Transformers têm duas partes principais: o codificador e o decodificador. O codificador analisa o texto de entrada, capturando suas relações internas, enquanto o decodificador gera a saída (como uma tradução, por exemplo), usando informações do codificador e ajustando-as com base no contexto. A arquitetura também usa mecanismos como multi-head attention e camadas feed-forward para melhorar o aprendizado e a captura de padrões complexos. Além disso, camadas de normalização e conexões residuais ajudam a estabilizar o treinamento e a manter o desempenho.

Os elementos principais da arquitetura Transformers são:

**Self-Attention:** Este mecanismo permite que o modelo analise cada palavra (token) em relação a todas as outras palavras da entrada, ajudando a identificar quais palavras são mais relevantes para cada uma. Isso é essencial para capturar contextos e dependências entre palavras em uma frase.

**Multi-Head Attention**: Para melhorar o poder de análise do self-attention, o modelo utiliza várias "cabeças" de atenção. Cada uma delas captura diferentes aspectos das relações entre as palavras. As informações obtidas por essas várias cabeças são então combinadas, enriquecendo a representação contextual.

**Camadas Feed-Forward**: Cada bloco de Transformer possui uma rede neural densa totalmente conectada que processa os dados de forma independente para cada posição. Essas camadas ajudam a refinar e transformar as representações aprendidas na camada de atenção.

**Positional Encoding**: Como o Transformer não possui uma estrutura recorrente, ele usa codificações posicionais para fornecer uma noção de ordem ao modelo, adicionando vetores que indicam a posição de cada palavra na sequência.

**Normas e Conexões Residuais**: Cada subcamada é seguida por uma camada de normalização (normalização por camada) e uma conexão residual. A normalização ajuda a manter os valores em uma faixa estável, facilitando o treinamento, enquanto as conexões residuais ajudam a prevenir o problema de dissipação do gradiente (comum em redes profundas) e melhoram a fluidez do aprendizado.

**Codificador e Decodificador:** No Transformer original, o codificador recebe o texto de entrada e gera representações contextuais, enquanto o decodificador usa essas representações para gerar a saída (por exemplo, a tradução). O codificador é composto de várias camadas que incluem multi-head attention, camadas feed-forward e normalização, e o decodificador também possui essas camadas, além de uma atenção cruzada para capturar informações do codificador.

Esses elementos formam a base da arquitetura Transformer, que se tornou a base para modelos avançados de linguagem, como o BERT e o GPT, usados em uma ampla gama de tarefas de PLN (Processamento de Linguagem Natural).

## Estratégia de Transfer Learning (Transferência de Aprendizado)

Transfer Learning é uma estratégia poderosa no campo de aprendizado de máquina que aproveita modelos pré-treinados em grandes conjuntos de dados para resolver problemas em novos domínios com dados limitados.

A ideia central é reutilizar o conhecimento adquirido por um modelo em uma tarefa anterior para uma nova tarefa, reduzindo a necessidade de treinar um modelo do zero.

Isso é bem vantajoso quando os dados disponíveis para a nova tarefa são escassos ou quando o treinamento completo de um modelo seria computacionalmente caro e demorado.

> Uma aplicação comum de Transfer Learning é em visão computacional, onde modelos pré-treinados em grandes bases de dados, como ImageNet, são adaptados para tarefas específicas, como classificação de imagens médicas ou detecção de objetos. 

O processo geralmente envolve a utilização das camadas iniciais do modelo pré-treinado, que capturam características genéricas das imagens, e o ajuste das camadas finais para a tarefa específica.

Esse ajuste pode ser realizado através de técnicas como fine-tuning, onde as últimas camadas são re-treinadas com os novos dados, enquanto as camadas iniciais são mantidas congeladas ou parcialmente ajustadas.

Em processamento de linguagem natural, Transfer Learning tem sido aplicado com grande sucesso através de modelos como BERT e GPT.

Esses modelos são inicialmente pré-treinados em grandes corpora de texto para aprender representações linguísticas ricas e contextuais. Posteriormente, são finamente ajustados para tarefas específicas, como análise de sentimentos, tradução de idiomas ou resposta a perguntas, usando conjuntos de dados menores e específicos para essas tarefas.

A reutilização de modelos pré-treinados não só acelera o processo de desenvolvimento, mas também frequentemente resulta em melhor desempenho, aproveitando o conhecimento acumulado em grandes quantidades de dados diversos.

## Otimização de Hiperparâmetros

A otimização de hiperparâmetros é um processo em aprendizado de máquina que envolve a seleção dos valores ideais para os parâmetros que controlam o comportamento dos algoritmos de treinamento.

Diferente dos parâmetros aprendidos durante o treinamento, como os pesos de uma rede neural, os hiperparâmetros são definidos antes do treinamento e influenciam diretamente a eficiência e a precisão do modelo.

Exemplos comuns de hiperparâmetros incluem: a taxa de aprendizado, o número de neurônios em cada camada, a taxa de regularização e o número de épocas de treinamento.

Existem várias técnicas para a otimização de hiperparâmetros, cada uma com suas próprias vantagens. A busca em grade (grid search) é uma abordagem exaustiva que testa todas as combinações possíveis de hiperparâmetros dentro de um espaço predefinido.

Embora essa técnica garanta a exploração completa do espaço de busca, pode ser computacionalmente intensiva e demorada.

A busca aleatória (random search), por outro lado, amostra aleatoriamente combinações de hiperparâmetros, muitas vezes resultando em uma solução eficiente com menos recursos computacionais.

Métodos mais avançados, como otimização bayesiana, utilizam modelos probabilísticos para guiar a busca, focando em áreas promissoras do espaço de hiperparâmetros com base em resultados anteriores.

A escolha adequada dos hiperparâmetros pode ter um impacto significativo no desempenho do modelo. Hiperparâmetros mal ajustados podem levar a modelos subótimos, com desempenho inferior em termos de precisão e generalização.

Por outro lado, uma otimização eficaz dos hiperparâmetros pode melhorar substancialmente a capacidade do modelo de capturar padrões nos dados e generalizar para novos exemplos.
Técnicas como validação cruzada são frequentemente usadas em conjunto com a otimização de hiperparâmetros para assegurar que os modelos não sejam apenas bem ajustados aos dados de treinamento, mas também mantenham um bom desempenho em dados não vistos.

## GNNs (Graph Neural Networks) 

Graph neural networks: A review of methods and applications
https://arxiv.org/pdf/1812.08434

**Graph Neural Networks (GNNs)** são uma classe de modelos de aprendizado profundo projetada para operar em dados que podem ser representados como grafos. Grafos são estruturas compostas por nós (ou vértices) e arestas que conectam esses nós.

GNNs são particularmente úteis para tarefas onde os dados têm uma natureza relacional complexa e podem ser representados de forma mais natural como grafos. Alguns exemplos de tais dados incluem redes sociais, moléculas químicas, rotas de transporte e interações de proteínas.

As principais características e componentes das GNNs incluem:

**Representação de Grafos**: Um grafo G é representado por um conjunto de nós V e um conjunto de arestas E. Cada nó pode ter atributos (como características ou features) e cada aresta pode ter pesos ou rótulos.

**Propagação de Mensagens (Message Passing)**: O processo central das GNNs envolve a propagação de informações entre nós através das arestas. Cada nó atualiza seu estado (ou representação) com base nas informações recebidas dos nós vizinhos. Esse processo é iterado várias vezes, permitindo que a informação se propague pelo grafo.

**Agregação de Informações**: Durante a propagação de mensagens, cada nó coleta informações de seus vizinhos. Essa agregação pode ser feita de várias maneiras, como soma, média, ou através de redes neurais mais complexas.

**Atualização de Estados**: Após a agregação, cada nó atualiza seu estado (ou embedding) usando uma função de atualização, que geralmente é uma rede neural. Esse novo estado reflete a informação agregada dos vizinhos.

**Leitura (Readout)**: Após várias iterações de propagação e atualização, as representações dos nós podem ser usadas para tarefas específicas, como classificação de nós, previsão de links (arestas), ou classificação de grafos inteiros. A leitura pode envolver agregações globais das representações dos nós para obter uma representação do grafo inteiro.

A força das GNNs reside em sua capacidade de capturar e utilizar a estrutura topológica e as relações entre os dados de uma maneira que modelos tradicionais de aprendizado profundo não conseguem fazer. Isso as torna uma ferramenta poderosa para uma ampla gama de problemas complexos e interconectados.

### Logits

Logits são os valores brutos (ou não normalizados) produzidos pela camada final de um modelo de classificação, antes de serem transformados em probabilidades. Em um modelo de rede neural a última camada geralmente gera esses logits, que representam a "força" ou "confiança" do modelo em relação a cada classe.

Esses valores ainda não são probabilidades, pois podem estar em qualquer faixa de números reais (positivos ou negativos). Para converter os logits em probabilidades, usa-se uma função de ativação, como a softmax ou sigmóide, que normaliza os logits para que se transformem em uma distribuição de probabilidades (valores entre 0 e 1 que somam 1). A classe com a maior probabilidade será a previsão final do modelo.

### Backpropagation

O **backpropagation** é um algoritmo usado para treinar redes neurais artificiais. Ele ajusta os pesos das conexões entre os neurônios para minimizar o erro entre as previsões da rede e os valores reais. O processo funciona assim:

- A rede faz uma previsão com base em uma entrada.

- Calcula-se o erro comparando a previsão com o valor esperado.

- Esse erro é "retropropagado" pela rede, ou seja, o erro é distribuído de trás para frente, camada por camada, ajustando os pesos de cada conexão.

- O ajuste é feito usando o gradiente descendente, que otimiza os pesos para reduzir o erro na próxima iteração.

Esse processo é repetido até que o erro seja minimizado, e a rede esteja devidamente treinada.

### Gradientes

Os **gradientes** no treinamento de modelos de Machine Learning, especialmente redes neurais, são <u> vetores que indicam a direção e a magnitude da mudança necessária nos pesos do modelo para minimizar o erro </u> (ou a função de perda). Eles representam a taxa de variação da função de perda em relação a cada peso do modelo.

Durante o treinamento, o algoritmo calcula o gradiente da função de perda em relação aos pesos (ou parâmetros) da rede. Esse gradiente indica como ajustar os pesos para reduzir o erro na próxima iteração.

O processo ocorre assim:

- **Cálculo da perda**: A rede faz uma previsão para uma amostra de dados e calcula a diferença (erro ou perda) entre a previsão e o valor real.

- **Retropropagação (backpropagation)**: O erro é retropropagado pelas camadas da rede, e o gradiente da perda é calculado em relação a cada peso do modelo. Isso é feito aplicando a regra da cadeia (derivadas parciais) em cada camada.

- **Atualização dos pesos**: Os pesos são ajustados na direção oposta ao gradiente, usando o gradiente descendente. Esse ajuste é controlado por uma taxa de aprendizado (learning rate), que define o tamanho do passo a ser dado na direção sugerida pelo gradiente.

Os gradientes são fundamentais para orientar a rede neural a modificar seus pesos de forma a minimizar a função de perda, permitindo que o modelo aprenda e melhore sua performance ao longo do tempo.