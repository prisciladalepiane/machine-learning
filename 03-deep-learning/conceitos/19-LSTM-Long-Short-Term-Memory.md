# Conhecendo a Arquitetura LSTM (Long Short-Term Memory)

A arquitetura LSTM (Long Short-Term Memory) é uma forma avançada de redes neurais recorrentes (RNNs), projetada especificamente para lidar com sequências de dados e abordar o problema do desaparecimento do gradiente que é comum em RNNs tradicionais.

LSTM é poderosa e versátil, e tem sido utilizada em uma ampla gama de aplicações, desde a geração automática de texto até a previsão do mercado de ações.

Seguem alguns aspectos chave da arquitetura LSTM:

Estrutura Básica: Uma rede LSTM é composta por uma série de células LSTM, cada uma das quais é responsável por manter um estado ao longo do tempo. Cada célula tem três portões: o portão de entrada (input gate), o portão de esquecimento (forget gate) e o portão de saída (output gate).

Portão de Entrada (Input Gate): Este portão decide quais novas informações serão adicionadas ao estado da célula. Ele consiste em duas partes: uma sigmóide, que decide quais valores serão atualizados, e uma função tanh, que cria uma nova matriz de candidatos a serem adicionados ao estado.

Portão de Esquecimento (Forget Gate): Este portão decide quais informações devem ser descartadas do estado da célula. Ele olha para o estado anterior ($h_{t-1}$) e a entrada atual ($x_t$), e gera um número entre 0 e 1 para cada número no estado da célula. Um 1 significa “manter completamente” e um 0 significa “esquecer completamente”.

Atualização do Estado da Célula: O estado antigo da célula ($C_{t-1}$) é atualizado para o novo estado da célula ($C_t$). Para fazer isso, multiplicamos o estado antigo pelo output do portão de esquecimento (esquecendo as coisas que decidimos esquecer anteriormente) e então somamos isso com o produto do output do portão de entrada e a nova matriz de candidatos.

Portão de Saída (Output Gate): Este portão decide o que será a próxima saída. Primeiro, uma função sigmóide decide quais partes do estado da célula vai colocar para output. Depois, o estado da célula passa por uma função tanh (para colocar os valores entre -1 e 1) e multiplica-se pelo output da sigmóide.

A característica mais importante das LSTMs é a sua habilidade de manter informações importantes e esquecer informações não relevantes através de longas sequências de dados, o que as torna particularmente eficazes para tarefas de processamento de linguagem natural e previsão de séries temporais.