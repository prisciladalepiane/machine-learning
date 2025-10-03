// Trabalhando com Structs, Enums e Traits

/*             --------   TRAITS   ----------             */
// Definindo o trait Description
trait Description {

    // Declarando um método describe que retorna uma String
    fn describe(&self) -> String;
}

/* 
Em Rust, &self é uma referência imutável ao objeto atual sobre o qual um método está sendo chamado. 

Ou seja, &self é uma referência imutável ao próprio objeto. Isso significa que o método pode ler os dados do objeto, 
mas não pode modificá-los.

Usar &self é equivalente a passar &self explicitamente como argumento para o método. Por exemplo, se você tem um método 
describe em um trait, o compilador entende que você está passando uma referência ao objeto atual.

Quando você define um método em um trait ou em uma implementação de struct, geralmente o primeiro parâmetro é &self. 
Isso permite que o método acesse os dados do objeto sobre o qual ele está sendo chamado.

*/

/*      --------   STRUCTS   ----------             */
// Definindo o struct Person com dois campos: name e age
struct Person {
    name: String,
    age: u32,
}

/*    --------   IMPLEMENTAÇÕES DE TRAITS   ----------             */
// Implementando o trait Description para o struct Person
impl Description for Person {

    // Definindo o método describe para Person
    fn describe(&self) -> String {

        // Retornando uma string formatada com os campos name e age
        format!("Nome: {}, Idade: {}", self.name, self.age)
    }
}

/*      --------   ENUMS   ----------             */
// Definindo o enum Job com duas variantes: Employed e Unemployed
enum Job {
    Employed(String),  // A variante Employed contém uma String
    Unemployed,        // A variante Unemployed não contém dados
}

// Implementando o trait Description para o enum Job
impl Description for Job {

    // Definindo o método describe para Job
    fn describe(&self) -> String {

        // Usando uma expressão match para retornar a descrição apropriada
        match self {
            Job::Employed(position) => format!("Empregado como {}", position),
            Job::Unemployed => String::from("Desempregado"),
        }
    }
}

// Função principal
fn main() {
    
    // Criando uma instância de Person
    let person = Person {
        name: String::from("Bob"),
        age: 30,
    };

    // Criando duas instâncias de Job
    let job1 = Job::Unemployed;
    let job2 = Job::Employed(String::from("Engenheiro de Machine Learning"));

    // Imprimindo as descrições das instâncias de Person e Job
    println!("Pessoa --> {}", person.describe());
    println!("Job 1: {}", job1.describe());
    println!("Job 2: {}", job2.describe());
}