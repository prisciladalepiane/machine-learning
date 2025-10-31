
use rand::Rng; // Importa a funcionalidade de geração de números aleatórios do pacote `rand`.

use std::cmp::Ordering; // Importa a funcionalidade para comparar valores.

use std::io; 

fn main() {

    println!("Jogo de Adivinhação!");
    
    let secret_number = rand::rng().random_range(1..=100);

    println!("O número secreto é: {}", secret_number);

    println!("Consegue Adivinhar o Número Secreto?");
    println!("Digite Um Número:");

    let mut num = String::new();

    io::stdin()
        .read_line(&mut num)
        .expect("Falha ao ler o input");

    // Tenta converter a entrada em um número inteiro de 32 bits.
    let num: u32 = num.trim().parse().expect("Digite Um Número!");

    // Compara o palpite com o número secreto e imprime uma mensagem correspondente.
    match num.cmp(&secret_number) {
        
        // Caso o palpite seja menor que o número secreto, informa ao usuário que seu palpite foi baixo.
        Ordering::Less => println!("Você digitou um número menor que o número secreto!"),
        
        // Caso o palpite seja maior que o número secreto, informa ao usuário que seu palpite foi alto.
        Ordering::Greater => println!("Você digitou um número maior que o número secreto!"),
        
        // Caso o palpite seja igual ao número secreto, parabeniza o usuário por ganhar.
        Ordering::Equal => println!("Você Adivinhou o Número. Você Venceu!!!"),
    }
}
