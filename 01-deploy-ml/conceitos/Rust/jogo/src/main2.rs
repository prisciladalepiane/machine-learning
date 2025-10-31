// Fundamentos da Linguagem Rust

// Importa a biblioteca de entrada/saída do Rust.
use std::io;

// Importa a biblioteca rand para geração de números aleatórios.
use rand::Rng;

fn main() {
    
    // Gera um número aleatório entre 1 e 100 e armazena em `secret_number`.
    // declarada uma constante
    let secret_number = rand::rng().random_range(1..=100);

    // Imprime o número secreto 
    println!("O número aleatório é: {}", secret_number);

    // Solicita ao usuário para digitar um número.
    println!("Digite Um Número:");

    // Cria uma variável mutável para armazenar a entrada do usuário como texto.
    let mut num = String::new();

    // Lê uma linha do terminal e armazena na variável `num`.
    // &mut num passa a variável por referência mutável.
    io::stdin()
        .read_line(&mut num)
        .expect("Falha ao ler o input");

    // Imprime o valor que o usuário digitou.
    println!("Você Digitou: {}", num);
}
