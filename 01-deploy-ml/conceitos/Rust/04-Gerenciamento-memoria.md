### Gerenciamento de Memória com Rust

O script em Rust `07-gerenciamento-memoria.rs` exemplifica conceitos essenciais de gerenciamento de memória, como **propriedade**, **empréstimo de referências** e **mutabilidade**.

1. **Propriedade**: No início do código, uma string é criada e atribuída a uma variável, e então essa propriedade é transferida para outra variável. Em Rust, quando a propriedade de um valor é movida de uma variável para outra, a variável original perde a validade e não pode mais ser usada. Isso é demonstrado quando a primeira variável é movida para a segunda, tornando a primeira inválida.

2. **Empréstimo de referências** Em seguida, outra string é criada e, dessa vez, uma referência imutável a essa string é passada para uma função que calcula e retorna o comprimento da string. A referência imutável permite que a função acesse os dados da string sem ter a capacidade de modificá-los, garantindo assim a integridade dos dados originais.

3. **mutabilidade** Mais adiante, o script cria uma nova string, mas dessa vez a string é mutável, ou seja, pode ser modificada após a sua criação. Uma referência mutável dessa string é então passada para uma função que modifica o conteúdo da string original. Após a modificação, o novo valor da string é impresso, demonstrando como referências mutáveis permitem que funções externas alterem o estado dos dados.

O código ilustra como Rust gerencia a memória de forma segura, prevenindo acessos inválidos e modificações indesejadas, ao mesmo tempo em que fornece mecanismos para controlar a propriedade e a mutabilidade dos dados.
