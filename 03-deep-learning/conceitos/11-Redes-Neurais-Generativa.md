# Redes Neurais Generativa

Redes Neurais Generativas são algoritmos deaprendizado de máquina que permitem a geração de novos dados que são semelhantes aos dados em que foram treinadas. Ao contrário das redes neurais discriminativas (como CNNs e RNNs), que aprendem a mapear dados de entrada em categorias, as redes generativas são capazes de gerar dados novos, criando amostras plausíveis a partir do mesmo espaço de distribuição dos dados de treino.Uma das arquiteturas mais conhecidas dentro das Redes Neurais Generativas são as Redes Adversariais Generativas (GANs). As GANs são compostas por duas redes neurais que são treinadas simultaneamente: o gerador e o discriminado.

O gerador produz dados novos a partir de ruído aleatório, enquanto o discriminador avalia esses dados tentando distinguir entre amostras geradas (fake) e dados reais. O treinamento dessas redes ocorre em um cenário de jogo de soma zero, onde o gerador tenta maximizar a probabilidade de o discriminador cometer erros e o discriminador tenta se tornar melhor em distinguir o real do falso. Esse processo de treinamento adversarial continua até que o gerador se torne suficientemente bom para produzir dados que o discriminador não consegue diferenciar dos reais.Outro tipo de rede neural generativa é o Modelo Autorregressivo, como a rede PixelRNN, que gera dados sequencialmente, um componente por vez. Eles são treinados para prever o próximo elemento da sequência, dado os elementos anteriores, e utilizam essa capacidade para gerar novas sequências, preenchendo uma etapa de cada vez, o que pode ser usado para gerar imagens pixel a pixel ou música nota a nota.


As redes neurais generativas também incluem as Redes Geradoras de Momento Variacional (Variational Autoencoders -VAEs), que são baseadas na ideia de aprender a distribuição latente dos dados de entrada e, em seguida, amostrar dessa distribuição para gerarnovos dados. VAEs consistem em um codificador, que mapeia os dados de entrada para uma representação latente e um decodificador que reconstrói os dados a partir dessa representação. Eles são treinados para maximizar a verossimilhança dos dados reconstruídos, ao mesmo tempo em que mantêm a distribuição latente próxima a uma distribuição priori, normalmente uma gaussiana.

As redes neurais generativas têm uma ampla gama de aplicações, desde a criação de arte, música e textos até a geração de modelos 3D. Sua capacidade de gerar dados novos e diversos, que são ao mesmo tempo únicos e semelhantes aos dados originais, abre novoscaminhos na exploração da criatividade assistida por máquina e na resolução de problemas complexos em diversos campos da ciência e engenharia.

https://www.deeplearningbook.com.br/algoritmo-backpropagation-parte-2-treinamento-de-redes-neurais/

https://epoch.ai/blog/backward-forward-FLOP-ratio
 
