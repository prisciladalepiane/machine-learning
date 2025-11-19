# Arquiteturas de modelos Deep Learning
As arquiteturas de modelos de Deep Learning evoluíram rapidamente ao longo dos anos, adaptando-se a diferentes tarefas e desafios. ALgumas das arquiteturas mais notáveis e amplamente usadas incluem:

- Redes Neurais Densamente Conectadas (DNNs)
- Redes Neurais Convolucionais (CNNs)
- Redes Neurais Recorrentes (RNNs)
- Autoencoders
- Redes Adversarias Generativas (GANs)
- Redes Siamesas
- Modelos de Capsule
- Modelos de Atenção e Transformadores

1. **Redes Neurais Densamente Conectadas (DNNs)**

Cada neurônio de uma camada está conectado a todos os da próxima. É o tipo mais básico de rede neural profunda.

Uso comum:
Classificação de dados tabulares ou previsão de valores contínuos.

Exemplo:
Prever o preço de casas com base em variáveis como tamanho, localização e número de quartos.

2. **Redes Neurais Convolucionais (CNNs)**

Usam camadas convolucionais que detectam padrões locais (bordas, formas, texturas), muito eficazes em dados com estrutura espacial.

Uso comum:
Visão computacional — reconhecimento de imagens, detecção de objetos.

Exemplo:
Identificar se uma imagem contém um gato ou um cachorro.

3. **Redes Neurais Recorrentes (RNNs)**

Processam sequências, mantendo uma “memória” do que já foi visto por meio de conexões recorrentes.

Uso comum:
Modelagem de séries temporais e processamento de linguagem natural.

Exemplo:
Prever a próxima palavra em uma frase ou prever o preço de ações baseado em dias anteriores.

4. **Autoencoders**

Aprendem a comprimir (codificar) e reconstruir (decodificar) dados, buscando representar informações de forma compacta.

Uso comum:
Redução de dimensionalidade, remoção de ruído, detecção de anomalias.

Exemplo:
Reduzir o número de variáveis de uma imagem mantendo suas características principais.

5. **Redes Adversárias Generativas (GANs)**

O que são:
Formadas por duas redes, um gerador e um discriminador, que competem entre si: o gerador cria dados falsos e o discriminador tenta distinguir os reais dos falsos.

Uso comum:
Geração de imagens, vídeos e vozes sintéticas realistas.

Exemplo:
Criar rostos humanos inexistentes com aparência real.

6. **Redes Siamesas**

O que são:
Usam duas (ou mais) redes idênticas com pesos compartilhados para comparar a similaridade entre entradas.

Uso comum:
Reconhecimento de assinaturas, faces ou textos semelhantes.

Exemplo:
Verificar se duas fotos pertencem à mesma pessoa (autenticação facial).

7. **Modelos de Capsule (CapsNet)**

Agrupam neurônios em “cápsulas” que preservam relações espaciais entre partes de um objeto, superando limitações das CNNs.

Uso comum:
Reconhecimento de padrões complexos com diferentes orientações e posições.

Exemplo:
Identificar um rosto mesmo se estiver parcialmente rotacionado ou inclinado.

8. **Modelos de Atenção e Transformadores**

Utilizam mecanismos de atenção para focar nas partes mais relevantes da entrada, permitindo paralelização e aprendizado de dependências de longo alcance.

Uso comum:
Tradução automática, chatbots, modelos de linguagem (como GPT e BERT).

Exemplo:
ChatGPT — que entende e gera texto com base em grandes quantidades de contexto.


## Redes Neurais Convolucionais (CNNs) e Redes Neurais Recorrentes (RNNs)

Redes Neurais Convolucionais (CNNs) e Redes Neurais Recorrentes (RNNs) são duas arquiteturas fundamentais de redes neurais profundas que se destacam em diferentes tipos de tarefas de aprendizado de máquina. 

As CNNs são particularmente eficazes no processamento de dados que possuem uma grade espacial, como imagens, onde a localização relativa de características é essencial para a realização de tarefas como classificação e detecção de objetos. 

A arquitetura de uma CNN é caracterizada por camadas convolucionais que aplicam filtros aos dados de entrada, capturando assim características locais. Estes filtros são pequenos em termos de largura e altura, mas se estendem por toda a profundidade do volume de entrada.

Após cada camada convolucional, normalmente há uma camada de pooling, que serve para reduzir as dimensões espaciais e agrupar características importantes. No final da CNN, há camadas densamente conectadas que interpretam as características de alto nível extraídas pelas camadas convolucionais e de pooling para fazer previsões ou classificações.

A arquitetura CNN surgiu no final da década de 80, mas ganhou impulso nos anos 2000. Técnicas modernas atuais, como os Vision Transformers, usam camadas convolucionais ou redes convolucionais inteiras como backbone (parte central da arquitetura), como aliás veremos aqui neste curso. 

As RNNs são especialmente adequadas para dados sequenciais, como linguagem natural ou séries temporais, onde a ordem e o contexto são importantes. A propriedade distintiva das RNNs é a sua capacidade de manter um estado ou memória ao longo do tempo, usando suas conexões recorrentes, onde saídas de etapas anteriores são utilizadas como entrada juntamente com novos dados de entrada. 

Isso permite que as RNNs formem uma espécie de memória sobre os elementos anteriores na sequência, o que é crucial para a compreensão do contexto e a geração de previsões. Contudo, aarquiteturaRNN padrão muitas vezes tem dificuldadespara aprender dependências de longo prazo devido a problemas como o desaparecimento ou a explosão do gradiente. Para superar os problemas da RNN padrão, variações como LSTM (Long Short-Term Memory) e GRU (Gated Recurrent Units) foram desenvolvidas. Estas estruturas utilizam portões especiais para controlar o fluxo de informações, permitindo que a rede retenha seletivamente ou descarte informações ao longo do tempo, facilitando a aprendizagem de dependências de longo prazo.

A arquitetura LSTM, que surgiu em 1997, foi um dos maiores avanços em Deep Learning e a arquitetura Transformer nasceu exatamente para tentar melhorar essa arquiteturaem tarefas de PLN. E conseguiu!Enquanto as CNNs impõem uma estrutura hierárquica local para o reconhecimento de padrões, as RNNs abordam a sequencialidade e a temporalidade dos dados. 

Ambas as arquiteturas revolucionaramcampos como Visão Computacional e Processamento de Linguagem Natural, respectivamente, e continuam a ser áreas de pesquisa intensa para melhorar a capacidade das máquinas de aprender e interpretar dados complexos.


Redes Neurais Generativa

Redes Neurais Generativas são algoritmos deaprendizado de máquina que permitem a geração de novos dados que são semelhantes aos dados em que foram treinadas. Ao contrário das  redes  neurais  discriminativas  (como  CNNs  e  RNNs),  que  aprendem  a  mapear  dados  de entrada em categorias, as redes generativas são capazes de gerar dados novos, criando amostras plausíveis a partir do mesmo espaço de distribuição dos dados de treino.Uma  das  arquiteturas  mais  conhecidas  dentro  das  Redes  Neurais  Generativas  são  as Redes Adversariais Generativas (GANs). As GANs são compostas por duas redes neurais que são treinadas simultaneamente: o gerador e o discriminado