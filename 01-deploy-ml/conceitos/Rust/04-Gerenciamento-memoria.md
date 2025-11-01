### Gerenciamento de Memória com Rust

O script em Rust `07-gerenciamento-memoria.rs` exemplifica conceitos essenciais de gerenciamento de memória, como **propriedade**, **empréstimo de referências** e **mutabilidade**.

1. **Propriedade**: No início do código, uma string é criada e atribuída a uma variável, e então essa propriedade é transferida para outra variável. Em Rust, quando a propriedade de um valor é movida de uma variável para outra, a variável original perde a validade e não pode mais ser usada. Isso é demonstrado quando a primeira variável é movida para a segunda, tornando a primeira inválida.

2. **Empréstimo de referências** Em seguida, outra string é criada e, dessa vez, uma referência imutável a essa string é passada para uma função que calcula e retorna o comprimento da string. A referência imutável permite que a função acesse os dados da string sem ter a capacidade de modificá-los, garantindo assim a integridade dos dados originais.

3. **mutabilidade** Mais adiante, o script cria uma nova string, mas dessa vez a string é mutável, ou seja, pode ser modificada após a sua criação. Uma referência mutável dessa string é então passada para uma função que modifica o conteúdo da string original. Após a modificação, o novo valor da string é impresso, demonstrando como referências mutáveis permitem que funções externas alterem o estado dos dados.

O código ilustra como Rust gerencia a memória de forma segura, prevenindo acessos inválidos e modificações indesejadas, ao mesmo tempo em que fornece mecanismos para controlar a propriedade e a mutabilidade dos dados.

### wnership, Borrowing, Mutable Borrowing e Contagem de Referência 

O script `08-gerenciamento-memoria-2.rs` demonstra conceitos de gerenciamento de memória, como propriedade, empréstimo (borrowing) de referências, empréstimo mutável e contagem de referências, utilizando diferentes mecanismos como referências simples, Box e Rc (Reference Counted).

O script começa com a definição de duas funções simples. A primeira função aceita uma referência imutável para um valor i32 e imprime esse valor. A segunda função aceita uma referência mutável para um i32 e incrementa o valor que está sendo referenciado. No corpo principal do código, um valor inteiro é criado e uma referência imutável a ele é passada para a função de impressão, demonstrando como referências podem ser usadas para acessar dados sem transferir propriedade.

Em seguida, o script demonstra o uso de uma referência mutável. Um valor inteiro mutável é criado e uma referência mutável a ele é passada para a função de incremento. Depois disso, o valor atualizado é impresso, ilustrando como Rust permite modificar os dados quando se usa uma referência mutável.

O script então apresenta o uso de Box, um tipo inteligente que aloca valores na heap em vez da stack. Um valor inteiro é armazenado em uma Box e uma referência a este valor é passada para a função de impressão. Isso demonstra como Box pode ser utilizado para alocação dinâmica de memória, embora o conceito de propriedade e empréstimo ainda se aplique.

Por fim, o script utiliza Rc, um tipo inteligente que permite a contagem de referências para gerenciar múltiplas referências imutáveis a um valor alocado na heap. Um valor inteiro é armazenado em um Rc e o código então cria clones do Rc, aumentando a contagem de referências. O script imprime o valor armazenado no Rc original e no seu clone, assim como a contagem de referências, demonstrando como Rc permite compartilhar a propriedade de dados entre diferentes partes do programa. Dentro de um escopo interno, outro clone do Rc é criado, e a contagem de referências é impressa novamente, ilustrando como a contagem aumenta com cada clone adicional. Quando o escopo interno termina, a contagem de referências é novamente impressa para mostrar que ela diminui conforme os clones saem de escopo e são descartados.

Este script exemplifica como Rust gerencia a memória de maneira eficiente e segura, utilizando diferentes abordagens para lidar com a propriedade, empréstimos mutáveis e a necessidade de compartilhar dados entre múltiplas partes de um programa sem risco de concorrência ou erros de memória.

No contexto da Linguagem Rust, os termos heap e stack referem-se a duas regiões de memória onde os dados podem ser alocados durante a execução de um programa. Eles funcionam de maneiras diferentes e entender como Rust gerencia essa alocação de memória é essencial para compreender o desempenho e o gerenciamento de recursos no código. Vamos explorar o significado de heap e stack, especialmente no uso de Box em Rust.

#### Stack

A stack (pilha) é uma região de memória de acesso rápido e de tamanho fixo, usada principalmente para armazenar dados locais de uma função, como variáveis de escopo. A memória é alocada e liberada automaticamente à medida que as funções entram e saem do escopo.

A alocação na stack é muito eficiente, pois segue o princípio LIFO (Last In, First Out), o que significa que a última variável alocada é a primeira a ser desalocada.

No entanto, a stack tem um tamanho limitado, o que significa que grandes blocos de dados, como estruturas complexas ou arrays grandes, geralmente não são armazenados nela.

#### Heap

A heap é uma região de memória maior e de acesso mais lento, onde os dados podem ser alocados dinamicamente durante a execução do programa. Ao contrário da stack, a heap permite a alocação de grandes quantidades de memória que podem persistir além do escopo de uma função.

A alocação e a desalocação na heap não seguem uma ordem específica e, por isso, requerem um gerenciamento mais complexo, normalmente com o uso de ponteiros para acessar os dados.

Em Rust, a alocação dinâmica de memória na heap é gerenciada manualmente com tipos inteligentes, como Box, Rc e Arc, que garantem o gerenciamento de memória seguro e eficiente.


#### Uso de Box em Rust

O Box é um tipo inteligente que permite alocar um valor na heap em vez da stack. Ao usar Box, o valor não é armazenado diretamente na stack, mas sim na heap e o Box mantém um ponteiro para esse valor.

Exemplo: Quando você coloca um valor em uma Box, como let x = Box::new(5);, o valor 5 é armazenado na heap e x contém uma referência (ponteiro) para essa localização na heap.

Mesmo quando se usa Box para alocação dinâmica na heap, as regras de propriedade e empréstimo de Rust ainda se aplicam: O valor na heap ainda tem um único proprietário, que é o Box. Quando o Box sai do escopo, o valor é desalocado automaticamente, garantindo que não haja vazamentos de memória.

Você pode "emprestar" o valor contido na Box usando referências (& ou &mut), respeitando as regras de segurança de memória de Rust (um único empréstimo mutável ou múltiplos empréstimos imutáveis).

Os valores apresentados na parte final do script refletem a forma como o tipo Rc (Reference Counted) gerencia a contagem de referências em Rust. Vamos analisar cada um desses valores:

Contagem de Referência Rc: 2

Quando você cria um Rc inicial (rc_value) e, em seguida, faz um clone dele (rc_clone), ambos compartilham a propriedade do mesmo valor alocado na heap. Cada vez que você clona um Rc, a contagem de referências aumenta, porque agora há mais um proprietário do valor. Neste ponto, como você tem o rc_value original e o rc_clone, a contagem de referências é 2.

Contagem de Referência Rc no escopo interno: 3

Dentro do bloco de código delimitado por chaves {}, um novo clone de rc_value é criado, chamado _outro_rc_clone. Este clone também compartilha a propriedade do valor, aumentando a contagem de referências para 3. Dentro deste escopo, como você tem rc_value, rc_clone e _outro_rc_clone, a contagem de referências reflete esses três donos.

Contagem de Referência Rc após o escopo interno: 2

Quando o bloco de código interno é finalizado, _outro_rc_clone sai de escopo e é descartado. Como resultado, a contagem de referências diminui, voltando para 2. Neste momento, restam apenas rc_value e rc_clone como donos do valor, e a contagem de referências reflete isso.

Portanto, os valores exibidos mostram como o Rc ajusta dinamicamente a contagem de referências conforme clones são criados e descartados, garantindo que o valor na heap só seja desalocado quando a contagem de referências chegar a zero, ou seja, quando não houver mais donos do valor.