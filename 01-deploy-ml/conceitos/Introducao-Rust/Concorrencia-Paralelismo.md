## Concorrência

Concorrência em programação de computadores refere-se à capacidade de um sistema para lidar com múltiplas tarefas em andamento, aparentemente ao mesmo tempo. Essa ilusão de simultaneidade é geralmente conseguida por meio de um agendamento eficiente, onde o processador alterna entre diferentes tarefas rapidamente. Em sistemas com um único processador, isso significa que o processador está alternando entre as tarefas, executando pequenos pedaços de cada uma em um dado tempo. A concorrência é essencial para sistemas que precisam gerenciar múltiplas operações simultaneamente, como servidores web que atendem a diversas requisições de clientes ao mesmo tempo. Ferramentas e técnicas como threads, corrotinas e loops de eventos são comuns para implementar concorrência.

## Paralelismo

Paralelismo, por outro lado, é a execução simultânea de múltiplas tarefas ou partes de uma tarefa em diferentes processadores ou núcleos de processamento. Enquanto a concorrência foca em estruturar um sistema para lidar com múltiplas tarefas, o paralelismo se aproveita do hardware para realmente executar várias tarefas ao mesmo tempo. Isso é possível em sistemas com múltiplos núcleos de CPU ou múltiplas CPUs, onde cada núcleo pode executar uma tarefa diferente ao mesmo tempo. O paralelismo é frequentemente utilizado em computação de alto desempenho, onde grandes problemas computacionais são divididos em partes menores e distribuídas por várias unidades de processamento para acelerar o tempo de execução. Frameworks como OpenMP, MPI e ferramentas de programação GPGPU são comuns nesse contexto.

## thread

Uma thread, em termos de computação, é a menor unidade de processamento que pode ser gerenciada pelo sistema operacional. Cada thread é parte de um processo e pode executar tarefas de forma independente, permitindo que várias operações ocorram simultaneamente dentro do mesmo processo. Aqui estão alguns pontos chave sobre threads:

**Execução Paralela**: Várias threads podem rodar ao mesmo tempo, melhorando a eficiência de programas que realizam múltiplas tarefas.

**Compartilhamento de Recursos**: Threads dentro do mesmo processo compartilham os mesmos recursos, como memória e arquivos, o que facilita a comunicação e a sincronização entre elas.

**Leveza**: Threads são mais leves que processos porque criar uma nova thread dentro de um processo existente consome menos recursos do que criar um novo processo.

**Sincronização**: Como threads compartilham recursos, é essencial gerenciar o acesso a esses recursos para evitar condições de corrida e outros problemas de sincronização.

