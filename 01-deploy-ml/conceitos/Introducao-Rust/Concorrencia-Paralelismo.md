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

### [./06-concorrencia-paralelismo.rs](./06-concorrencia-paralelismo.rs)

O script em Rust acima utiliza concorrência e paralelismo para criar e gerenciar múltiplas threads que executam tarefas simultaneamente.

Primeiramente, ele importa módulos necessários da biblioteca padrão para manipulação de threads (`std::thread`), comunicação entre threads (`std::sync::mpsc`), e manipulação de duração de tempo (`std::time::Duration`). No início da função `main`, um canal de comunicação é criado usando `mpsc::channel()`, que retorna um transmissor (`tx`) e um receptor (`rx`).

O script então cria o vetor handles para armazenar os identificadores das threads. Em seguida, um loop for é utilizado para criar 5 threads. Dentro do loop, o transmissor `tx` é clonado para cada thread. Cada thread é criada utilizando thread::spawn, onde uma mensagem é formatada com o número da thread e enviada através do canal utilizando `tx.send(message).unwrap()`. A thread então dorme por 1 segundo utilizando `thread::sleep(Duration::from_secs(1))`.

Após a criação das threads, outro loop for é utilizado para receber e imprimir mensagens de cada thread. As mensagens são recebidas pelo canal usando `rx.recv().unwrap()` e impressas na tela.

Finalmente, um último loop for espera que todas as threads terminem a execução usando `handle.join().unwrap()`, garantindo que o programa principal só finalize após todas as threads terem concluído suas tarefas.

Ao final, uma mensagem é impressa para indicar que todas as threads foram processadas com sucesso.

## Mutex (Mutual Exclusion)

Mutex (Mutual Exclusion) é um mecanismo de sincronização utilizado em programação para garantir que somente uma thread ou processo possa acessar um recurso compartilhado por vez.

Em outras palavras, ele é usado para evitar condições de corrida (race conditions) quando múltiplas threads tentam ler e escrever em um recurso compartilhado simultaneamente. Aqui estão algumas características principais do mutex:

- **Exclusividade**: Um mutex garante que uma thread que possua o "lock" tenha acesso exclusivo ao recurso compartilhado.
- **Bloqueio**: Quando uma thread tenta adquirir um mutex que já está bloqueado por outra thread, ela será bloqueada até que o mutex seja liberado.
- **Liberação**: Uma vez que a thread que possui o mutex termine de usar o recurso compartilhado, ela deve liberar o mutex para permitir que outras threads adquiram o lock.

## Arc (Atomic Reference Counted)

Arc (Atomic Reference Counted) é uma estrutura de dados em Rust que permite que múltiplas threads compartilhem a propriedade de um valor.

Arc é uma forma segura e eficiente de gerenciar memória compartilhada entre threads, garantindo que o valor compartilhado seja desalocado apenas quando não houver mais referências a ele. Aqui estão algumas características principais do Arc:

- **Contagem de Referências Atômica**: Arc mantém uma contagem de referência atômica, garantindo que incrementos e decrementos na contagem de referência sejam realizados de forma segura entre múltiplas threads.
- **Imutabilidade**: Os dados gerenciados por Arc são imutáveis por padrão. Se for necessário modificar os dados, é comum combinar Arc com estruturas como Mutex para permitir mutabilidade segura.
- **Compartilhamento Seguro**: Arc permite que múltiplas threads possuam e acessem os mesmos dados de forma segura e eficiente, sem a necessidade de gerenciamento manual de memória.

