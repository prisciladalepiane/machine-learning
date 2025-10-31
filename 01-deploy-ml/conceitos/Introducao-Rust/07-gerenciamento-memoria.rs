// Gerenciamento de Memória com Rust

fn main() {

    /* -------- PARTE 1: Propriedade -------- */

    // Criando uma nova string e atribuindo-a a s1
    let s1 = String::from("Este era o valor de s1.");

    // Movendo a propriedade de s1 para s2, s1 não é mais válido
    // Em Rust, quando a propriedade de um valor é movida de uma variável para outra, a variável original perde a validade 
    // e não pode mais ser usada. 
    let s2 = s1;

    // Tentativa de uso de s1 causaria um erro de compilação
    // println!("{}", s1);

    // Imprimindo o valor de s2, que agora possui a string
    println!("{}", s2);

    /* -------- PARTE 2: Empréstimo de Referências -------- */

    // Criando uma nova string e atribuindo-a a s3
    let s3 = String::from("Priscila Gonçalves Dalepiane");

    // Emprestando s3 de forma imutável para a função calcula_comprimento
    // A referência imutável permite que a função acesse
    // os dados da string sem ter a capacidade de modificá-los, 
    let len = calcula_comprimento(&s3);

    // Imprimindo o comprimento de s3
    println!("O comprimento de '{}' é {}.", s3, len);

    /* -------- PARTE 3: Mutabilidade e Referências Mutáveis -------- */
    
    // Criando uma nova string mutável e atribuindo-a a s4
    let mut s4 = String::from("Hello");

    // Uma referência mutável da string s4 é passada para a função que modifica o conteúdo da string original. 
    altera_string(&mut s4);
    
    // Após a modificação, o novo valor da string é impresso, demonstrando como referências mutáveis permitem 
    // que funções externas alterem o estado dos dados.
    println!("A string s4 era Hello e agora é: {}", s4);
}

// Função que empresta uma referência imutável de uma string e retorna seu comprimento
fn calcula_comprimento(s: &String) -> usize {
    s.len()
}

// Função que empresta uma referência mutável de uma string e a modifica
fn altera_string(s: &mut String) {
    s.push_str(", World");
}
