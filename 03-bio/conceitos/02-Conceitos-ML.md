# Paradigmas clássicos de aprendizado de máquina

### Aprendizado supervisionado

o modelo aprende com dados rotulados

exemplos: regressão, classificação.

### Aprendizado não supervisionado

os dados não possuem rótulos

o modelo busca padrões nos dados

exemplos: clustering, redução de dimensionalidade.

### Aprendizado por reforço

o agente aprende por tentativa e erro,
recebe recompensas ou penalidades

usado em jogos, robótica e controle.

# Data Leakage 

## O que é Data Leakage (Vazamento de Dados)?

Data Leakage (Vazamento de Dados) é um termo utilizado em Data Science e aprendizado de máquina para descrever uma situação em que informações de fora do conjunto de dados de treinamento são inadvertidamente incorporadas ao modelo.

Isso pode ocorrer de diversas maneiras e geralmente resulta em uma avaliação superestimada do desempenho do modelo, pois ele pode parecer funcionar excepcionalmente bem durante a fase de teste, mas falhar ao ser aplicado em dados do mundo real.

Existem dois tipos principais de vazamento de dados:

**Vazamento de dados de teste para treinamento**: Isso ocorre quando informações do conjunto de dados de teste, que deveria ser desconhecido pelo modelo, são utilizadas durante o treinamento. Isso pode acontecer, por exemplo, se os conjuntos de dados de treinamento e teste são divididos sem cuidado, permitindo que algumas das informações do teste se infiltrem no treinamento.

**Vazamento de recursos futuros**: Isso acontece quando o modelo tem acesso a informações que não estariam disponíveis no momento da previsão na aplicação real. Por exemplo, usar como recurso (feature) um evento que só ocorre após o resultado que está sendo previsto.

Prevenir o vazamento de dados é importante para desenvolver modelos que funcionarão bem na prática. Algumas estratégias para evitar o vazamento de dados incluem:

- Cuidadosa separação dos conjuntos de dados de treinamento e teste, assegurando que não compartilhem informações.
- Utilização de técnicas de validação cruzada para avaliar o desempenho do modelo de forma mais realista.
- Revisão e limpeza dos dados para garantir que os recursos (features) utilizados para treinamento sejam apropriados e não contenham informações futuras ou de fora do domínio de aplicação.
- Monitoramento e teste contínuos do modelo em novos dados, para identificar possíveis problemas de vazamento de dados que não foram detectados inicialmente.