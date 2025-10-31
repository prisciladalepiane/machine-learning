// Fundamentos da Linguagem Rust

// Importa a funcionalidade de geração de números aleatórios do pacote `rand`.
use rand::Rng;

// Importa a funcionalidade para comparar valores.
use std::cmp::Ordering;

// Importa a biblioteca de entrada/saída do Rust.
use std::io;

// Função principal que é o ponto de entrada do programa.
fn main() {

    // Imprime uma mensagem de boas-vindas na tela.
    println!("Jogo de Adivinhação!");
    
    let secret_number = rand::rng().random_range(1..=100);

    // Mostra o número secreto na tela. Útil para depuração.
    println!("O número secreto é: {}", secret_number);

    println!("Consegue Adivinhar o Número Secreto?");
    // Inicia um loop infinito para repetir o jogo até que o usuário acerte o número.
    loop {
        
        // Pede ao usuário para adivinhar o número secreto.
        println!("Digite um número:");

        // Declara uma variável mutável `dsanum` para armazenar a entrada do usuário.
        let mut dsanum = String::new();

        // Lê uma linha do terminal e armazena na variável `dsanum`.
        io::stdin()
            .read_line(&mut dsanum)
            .expect("Falha ao ler o input");

        // Tenta converter a entrada em um número inteiro de 32 bits. Em caso de falha, pede uma nova entrada.
        let dsanum: u32 = match dsanum.trim().parse() {
            Ok(num) => num, // Se a conversão for bem-sucedida, prossegue com o número convertido.
            Err(_) => {
                println!("Valor Inválido."); // Informa ao usuário sobre a entrada inválida.
                continue; // Continua o loop, solicitando uma nova entrada.
            },
        };

        // Compara o palpite com o número secreto e imprime uma mensagem correspondente.
        match dsanum.cmp(&secret_number) {
            Ordering::Less => println!("Você digitou um número menor que o número secreto!"), // Informa se o palpite foi baixo.
            Ordering::Greater => println!("Você digitou um número maior que o número secreto!"), // Informa se o palpite foi alto.
            Ordering::Equal => {
                println!("Você Adivinhou o Número. Você Venceu!!!"); // Parabeniza o usuário se ele acertar o número.
                break; // Sai do loop se o usuário acertar o número.
            }
        }
    }
}
