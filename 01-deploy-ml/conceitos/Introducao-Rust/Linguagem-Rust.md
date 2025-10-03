# Linguagem RUST

https://rust-lang.org/pt-BR/

Rust é uma linguagem de programação moderna, projetada para fornecer segurança, desempenho e concorrência sem a necessidade de um coletor de lixo. Rust rapidamente ganhou popularidade por seu enfoque em segurança de memória, eficiência e funcionalidades modernas.
Seu sistema de gerenciamento de memória, baseado em "ownership", "borrowing" e "lifetimes", é projetado para prevenir uma série de bugs comuns em outras linguagens que gerenciam memória manualmente, como C e C++.

O compilador Rust, conhecido como rustc, desempenha um papel importante na garantia de segurança de memória, rejeitando programas que podem resultar em acessos de memória inseguros.
Isso ajuda a prevenir problemas como "race conditions", "buffer overflows"e "use-after-free", que são fontes comuns de vulnerabilidades em software. 

Além disso, Rustsuporta abstrações de alto nível com desempenho comparável ao de código de baixo nível, permitindo que os desenvolvedores escrevam código expressivo e eficiente sem sacrificar a velocidade de execução.

A biblioteca padrão da Linguagem Rust é minimalista, mas a comunidade Rust contribui para um ecossistema rico de "crates" (pacotes) disponíveis através do gerenciador de pacotes Cargo. Cargo facilita a compilação de projetos, gerenciamento de dependências e publicação de crates no site crates.io, o registro de pacotes Rust. Este ecossistema permite aos desenvolvedores compartilhar e reutilizar código facilmente, potencializando a colaboração e inovação.

https://docs.rs/cargo/latest/cargo/

Rust é ideal para desenvolvimento de sistemas, programação de aplicativos, desenvolvimento de jogos e especialmente para software que requer alto desempenho e segurança. 

Com uma comunidade ativa e crescente, Rust continua a evoluir, com frequentes atualizações que refinam a linguagem e expandem suas capacidades, tornando-a cada vez mais uma escolha atraente para diversos tipos de projetos de software, incluindo Machine Learning

## Como compilar

Compila
```bash
rust main.rs
```
EXecuta o programa
```bash
./main
```

## Compilar com cargo

Criar cargo
```bash
cargo new projeto
```

Entra na pasta
```bash
cd projeto
```

Executa o programa
```bash
cargo run
```
Para limpar a memória e recompilar
```bash
cargo clean
```
Instala os pacotes e dependencias, testa o programa
```bash
cargo build
```

Versão final do programa
```bash
cargo build --release
```

## Estrutura de Repetição

Rust oferece várias estruturas de loop para controle de fluxo, cada uma adequada para diferentes situações de programação:

**Loop**: Este é o tipo mais simples de loop, que continua a executar o bloco de código dentro dele indefinidamente até que seja explicitamente interrompido por uma instrução de saída, como break. É útil quando o número de iterações não é conhecido antes de o loop começar ou quando o loop deve continuar até que uma condição externa seja atendida. É similar ao While, porém mais básico.

```rust
loop{

}
```

**While**: Este tipo de loop executa repetidamente um bloco de código enquanto uma condição especificada é verdadeira. Antes de cada iteração, a condição é avaliada e o loop continua até que a condição se torne falsa. É útil quando você precisa continuar a executar um loop até que uma condição externa mude, mas onde essa condição é verificada antes de cada iteração.


**For**: O loop for em Rust é frequentemente usado para iterar sobre elementos de uma coleção, como arrays, vetores ou outras estruturas. Este loop itera sobre cada elemento da coleção, executando o bloco de código para cada elemento. É especialmente útil quando você conhece o conjunto de itens que deseja iterar, tornando o código mais seguro e conciso ao evitar erros comuns, como acessar índices fora dos limites da coleção.