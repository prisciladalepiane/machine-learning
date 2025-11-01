use std::fs::File;
use std::io::{self, Read, Write};
use std::fs; // Para manipulação de arquivos

fn create_file(file_path: &str, content: &str) -> Result<(), io::Error> {
    let mut file = File::create(file_path)?; // Cria o arquivo
    file.write_all(content.as_bytes())?; // Escreve o conteúdo no arquivo
    Ok(())
}

fn read_file_content(file_path: &str) -> Result<String, io::Error> {
    let mut file = File::open(file_path)?; // Abre o arquivo
    let mut content = String::new(); // Cria uma string para armazenar o conteúdo
    file.read_to_string(&mut content)?; // Lê o conteúdo do arquivo para a string
    Ok(content) // Retorna o conteúdo lido
}

fn delete_file(file_path: &str) -> io::Result<()> {
    fs::remove_file(file_path); // Remove o arquivo
    Ok(())
} 

fn main() -> io::Result<()> {
    let filename = "exemplo.txt"; // Nome do arquivo a ser criado

    // Cria o arquivo com algum conteúdo
    create_file(filename, "Olá, Mundo!")?;
    println!("Arquivo '{}' criado com sucesso.", filename);

    // Lê o conteúdo do arquivo
    let contents = read_file_content(filename)?;
    println!("Conteúdo do arquivo '{}': {}", filename, contents);

    // Deleta o arquivo
    delete_file(filename)?;
    println!("Arquivo '{}' deletado com sucesso.", filename);

    Ok(())
}