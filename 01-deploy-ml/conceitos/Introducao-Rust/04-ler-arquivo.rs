// Modulos necessários para manipulação de arquivos e entrada/saída
use std::fs::File; // Para manipulação de arquivos
use std::io::{self, Read}; // Para entrada e leitura de arquivos
use std::num::ParseIntError; // Para tratar erros de parsing

// Função para ler o conteúdo de um arquivo e retornar como String
fn read_file_content(file_path: &str) -> Result<String, io::Error> {

    let mut file = File::open(file_path)?; // Abre o arquivo
    let mut content = String::new(); // Cria uma string para armazenar o conteúdo
    file.read_to_string(&mut content)?; // Lê o conteúdo do arquivo para a string
    Ok(content) // Retorna o conteúdo lido
}

fn parce_string_to_int(s: &str) -> Result<i32, ParseIntError> {
    s.trim().parse::<i32>() // Tenta converter a string para um inteiro
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    
   let filename = "numero.txt"; // Nome do arquivo a ser lido

    let contents = read_file_content(filename)?; // Lê o conteúdo do arquivo

    let number = parce_string_to_int(&contents)?; // Converte o conteúdo para um inteiro

    println!("O número lido do arquivo é: {}", number); // Imprime o número lido

    Ok(()) // Retorna Ok se tudo correr bem
}