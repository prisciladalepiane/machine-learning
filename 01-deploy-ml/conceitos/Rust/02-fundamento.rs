// Fundamentos da Linguagem Rust

// Importa a biblioteca de entrada/saída do Rust.
use std::io;

// Função principal que é o ponto de entrada do programa.
// fn = function, main = principal
fn main() {

    // Pede ao usuário para digitar um número.
    // println! é uma macro que imprime texto no terminal.
    println!("Digite Um Número:");

    // Cria uma variável mutável para armazenar a entrada do usuário como texto.
    // String::new() cria uma nova string vazia.
    // mut = mutável
    // let = declara uma variável
    let mut num = String::new();

    // Lê uma linha do terminal e armazena na variável `num`.
    // io::stdin() obtém a entrada padrão (teclado).
    // read_line() lê a linha e armazena na variável passada por referência (&mut num).
    // expect() trata erros, se houver.
    io::stdin()
        .read_line(&mut num)
        .expect("Falha ao ler o input");

    // Imprime o valor que o usuário digitou.
    println!("Você Digitou: {}", num);
}