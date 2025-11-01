// Ownership, Borrowing, Mutable Borrowing e Contagem de Referência 

// Importando Rc (Reference Counted) da biblioteca padrão para contagem de referências
use std::rc::Rc;

// Função que imprime o valor de uma referência imutável a um i32
fn imprime_valor(value: &i32) {
    println!("Valor: {}", value);
}

// Função que incrementa o valor de uma referência mutável a um i32
fn incrementa_valor(value: &mut i32) {
    *value += 1;
}

fn main() {

    
    // 1. Gerenciamento de memória com referências  
    // Um valor inteiro é criado em x e uma referência imutável a ele é passada para a função de impressão, 
    // demonstrando como referências podem ser usadas para acessar dados sem transferir propriedade.
    let x = 10;
    imprime_valor(&x); 

    // Isso não é permitido em Rust
    // incrementa_valor(&x); 

    // 2. Gerenciamento de memória com referências mutáveis
    // Um valor inteiro mutável é criado em y e uma referência mutável a ele é passada para a função de incremento. 
    // Depois disso, o valor atualizado é impresso, ilustrando como Rust permite modificar os dados quando se usa uma referência mutável.
    let mut y = 20;
    incrementa_valor(&mut y); 
    imprime_valor(&y); 

    // 3. Gerenciamento de memória com Box
    // Aqui temos o uso de Box, um tipo inteligente que aloca valores na heap em vez da stack. 
    // Um valor inteiro é armazenado em uma Box e uma referência a este valor é passada para a função de impressão. 
    // Isso demonstra como Box pode ser utilizado para alocação dinâmica de memória, embora o conceito de propriedade e empréstimo ainda se aplique.
    let boxed_value = Box::new(30);
    imprime_valor(&boxed_value); 

    // Isso não é permitido em Rust:
    // incrementa_valor(&boxed_value); 

    // 4. Gerenciamento de memória com Rc (contagem de referência)
    // Aqui utilizamos Rc, um tipo inteligente que permite a contagem de referências para gerenciar múltiplas referências imutáveis a um valor 
    // alocado na heap. Um valor inteiro é armazenado em um Rc e o código então cria clones do Rc, aumentando a contagem de referências. 
    let rc_value = Rc::new(40);
    let rc_clone = Rc::clone(&rc_value); // Clona o Rc, aumentando a contagem de referência

    println!("Valor Rc: {}", rc_value);    // Imprime o valor do Rc original
    println!("Clone do Rc: {}", rc_clone); // Imprime o valor do Rc clonado
    println!("Contagem de Referência Rc: {}", Rc::strong_count(&rc_value)); // Imprime a contagem de referência do Rc

    {
        let _outro_rc_clone = Rc::clone(&rc_value); // Clona o Rc dentro de um escopo interno
        println!("Contagem de Referência Rc no escopo interno: {}", Rc::strong_count(&rc_value)); // Imprime a contagem de referência do Rc no escopo interno
    }

    println!("Contagem de Referência Rc após o escopo interno: {}", Rc::strong_count(&rc_value)); // Imprime a contagem de referência do Rc após o escopo interno
}

// Este script exemplifica como Rust gerencia a memória de maneira eficiente e segura, utilizando diferentes abordagens 
// para lidar com a propriedade, empréstimos mutáveis e a necessidade de compartilhar dados entre múltiplas partes de um programa 
// sem risco de concorrência ou erros de memória.