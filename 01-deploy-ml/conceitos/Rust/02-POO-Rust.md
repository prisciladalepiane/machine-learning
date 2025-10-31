# Programação Orientada a Objetos e Estruturada

A Programação Orientada a Objetos (POO) e a Programação Estruturada são paradigmas de programação que abordam a organização e estruturação de código de diferentes maneiras. Vamos explorar cada um deles em detalhes:

## Programação Estruturada


A Programação Estruturada é um paradigma que enfatiza a linearidade e o uso de estruturas de controle claras, como loops, condicionais e sub-rotinas (funções e procedimentos). Esse paradigma busca melhorar a clareza, qualidade e tempo de desenvolvimento do software. Principais Características:


### Modularidade:

- Divide o programa em módulos ou funções menores que realizam tarefas específicas.
- Facilita a manutenção e o entendimento do código.

### Estruturas de Controle:

- Utiliza estruturas de controle como if, else, while, for para controlar o fluxo do programa.
- Promove a utilização de blocos de código claros e bem definidos.


### Sequencialidade:

- O programa é executado de forma sequencial, linha por linha.
- As funções podem ser chamadas para executar tarefas específicas e retornar ao ponto de chamada.


### Escopo de Variáveis:

As variáveis têm escopo local e global, o que controla onde elas podem ser acessadas e modificadas.


**Vantagens**

- Facilidade de leitura e compreensão.
- Menor complexidade de controle do fluxo de execução.
- Debugging e testes mais simples.


**Desvantagens**

- Menor capacidade de reutilização de código em comparação com POO.
- Pode levar a códigos mais longos e difíceis de manter em projetos grandes.


## Programação Orientada a Objetos (POO)

A Programação Orientada a Objetos é um paradigma que organiza o código em torno de "objetos" que combinam dados e comportamento. Esse paradigma é projetado para lidar com a complexidade de sistemas grandes e promover a reutilização de código. Principais Características:


### Classes e Objetos:

- Classe: Define a estrutura e o comportamento de um tipo de objeto.
- Objeto: Instância de uma classe, contendo dados e métodos definidos pela classe.

### Encapsulamento:

- Esconde os detalhes internos de um objeto e expõe apenas uma interface controlada.
- Protege o estado interno do objeto contra modificações não autorizadas.

### Herança:

- Permite que uma classe derive de outra classe, herdando seus atributos e métodos.
- Facilita a criação de hierarquias de classes e reutilização de código.

### Polimorfismo:

- Permite que diferentes classes tratem as mesmas operações de maneiras diferentes.
- Facilita a extensão e a manutenção do código.

### Abstração:

- Simplifica a complexidade ao permitir que os desenvolvedores trabalhem em um nível de abstração mais alto.
- Foca nos aspectos essenciais de um objeto, ignorando os detalhes irrelevantes.

**Vantagens**

- Maior reutilização de código através de herança e polimorfismo.
- Melhoria na organização e estrutura do código, facilitando a manutenção.
- Capacidade de modelar problemas do mundo real de forma mais intuitiva.

**Desvantagens**

- Pode introduzir uma complexidade adicional, especialmente em sistemas pequenos.
- Requer um entendimento mais profundo dos conceitos de POO.

---

# Trabalhando com Structs, Enums e Traits

Tipo de dados personalizados.

## Structs 

Structs (estruturas) são tipos personalizados que agrupam diferentes valores. 
O tipo de dados sempre tem aqueles atributos.


**Quando Usar Structs**

- Use struct quando você tiver um conjunto de dados que sempre tem os mesmos campos. Cada campo na struct deve ser sempre presente e ter um tipo específico.

- Agrupamento de dados relacionados: Quando você quer agrupar vários valores que estão logicamente relacionados.

- Dados com uma identidade clara: Quando o dado representa uma entidade com uma identidade clara e persistente, como uma Pessoa, Carro, etc.

**Exemplo**
Toda pessoa tem nome e idade.

```rust
struct Pessoa {
    nome: String,
    idade: u32,
}
```
> Struct = “um objeto de dados com campos”.

## Enums

Enums (enumeradores) permitem a definição de um tipo que pode ser um de diversos valores variantes. São úteis para representar estados ou tipos de dados que podem assumir várias formas.

**Quando Usar Enum**

 - Use enum quando você precisa representar um valor que pode estar em um de vários estados possíveis, cada um possivelmente contendo dados diferentes.

 - Estados de um sistema: Quando você está modelando estados que um sistema ou um processo pode assumir.

- Diversas variantes exclusivas: Quando cada variante de um tipo de dado é exclusiva e você deseja manipular cada variante de maneira diferente.

**Exemplo**

Emprego tem duas variantes, ou tem um atributo, ou tem outro.

```rust
enum Emprego {
    Empregado(String),
    Desempregado,
}
```

> Enum = “um valor que pode ser de um tipo ou de outro”.

## Traits

Traits são semelhantes a interfaces em outras linguagens. Eles definem funcionalidades que um tipo deve implementar. Um trait pode ter métodos com implementações padrão ou métodos sem implementação, que devem ser definidos pelo tipo que implementa o trait. Definem funcionalidades compartilhadas que podem ser implementadas por diferentes tipos.

**Quando usar traits**

- Para criar uma especificação única e implementa de acordo com o tipo de dado.

**Exemplo**

Define uma única interface para implementar a função de acordo com o tipo de dado.

```rust
trait Description {
    fn describe(&self) -> String;
}
```