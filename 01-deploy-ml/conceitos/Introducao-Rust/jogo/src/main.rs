// Importa a funcionalidade de geração de números aleatórios do pacote `rand`.
use rand::Rng;

// Importa a funcionalidade para comparar valores.
use std::cmp::Ordering;

use std::io;

// Função principal que é o ponto de entrada do programa.
fn main() {

    // Imprime uma mensagem de boas-vindas na tela.
    println!("Jogo de Adivinhação!");
    println!("Tente adivinhar o número de 1 a 100. Você tem 5 tentativas.");
    
    let secret_number = rand::rng().random_range(1..=100);

    // Loop para dar ao usuário exatamente 5 tentativas para adivinhar o número.
    for tentativa in 1..=5 {
        
        // Informa ao usuário o número da tentativa atual.
        println!("Tentativa {}/5. Digite Um Número:", tentativa);

        // Declara uma variável mutável `dsanum` para armazenar a entrada do usuário.
        let mut dsanum = String::new();

        // Lê uma linha do terminal e armazena na variável `dsanum`.
        io::stdin()
            .read_line(&mut dsanum)
            .expect("Falha ao ler o input");

        // Tenta converter a entrada em um número inteiro de 32 bits.
        let dsanum: u32 = match dsanum.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Valor Inválido. Por favor, digite um número válido.");
                continue;
            },
        };

        // Compara o palpite com o número secreto e imprime uma mensagem correspondente.
        match dsanum.cmp(&secret_number) {
            Ordering::Less => println!("Você digitou um número menor que o número secreto!"),
            Ordering::Greater => println!("Você digitou um número maior que o número secreto!"),
            Ordering::Equal => {
                println!("Você Adivinhou o Número. Você Venceu!!!");
                return; // Sai do programa completamente se o usuário acertar o número.
            }
        }
    }

    // Informa ao usuário que ele esgotou suas 5 tentativas após o loop terminar.
    println!("Você esgotou suas 5 tentativas! O número secreto era: {}", secret_number);
}
