// Concorrência e Paralelismo

// Importando o módulo thread da biblioteca padrão para manipulação de threads
use std::thread;

// Importando o módulo mpsc (multiple producer, single consumer) para canais de comunicação entre threads
use std::sync::mpsc;

// Importando o módulo Duration da biblioteca padrão para manipulação de duração de tempo
use std::time::Duration;

fn main() {

    // Criando um canal para comunicação entre threads
    let (tx, rx) = mpsc::channel();

    // Criando um vetor para armazenar os handles das threads
    let mut handles = vec![];

    // Loop para criar 5 threads
    for i in 0..5 {

        // Clonando o transmissor para cada thread
        let tx = tx.clone();

        // Criando uma nova thread
        let handle = thread::spawn(move || {

            // Criando uma mensagem com o número da thread
            let message = format!("Thread {} está processando!", i);

            // Enviando a mensagem pelo canal
            tx.send(message).unwrap();

            // Fazendo a thread dormir por 1 segundo
            thread::sleep(Duration::from_secs(1));
        });

        // Adicionando o handle da thread ao vetor
        handles.push(handle);
    }

    // Loop para receber mensagens de cada thread
    for _ in 0..5 {

        // Recebendo a mensagem pelo canal
        let received = rx.recv().unwrap();
        
        // Imprimindo a mensagem recebida
        println!("{}", received);
    }

    // Esperando todas as threads terminarem
    for handle in handles {
        handle.join().unwrap();
    }

    // Imprimindo uma mensagem final
    println!("Todas as threads foram processadas.");
}