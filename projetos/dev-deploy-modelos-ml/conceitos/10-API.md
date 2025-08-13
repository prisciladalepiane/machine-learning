# O que é API?

**API** significa *Interface de Programação de Aplicações* (em inglês, *Application Programming Interface*).  
É um conjunto de regras e padrões que permite a comunicação entre diferentes programas de computador.  
Pense nela como um intermediário, facilitando a troca de informações entre sistemas de forma segura e eficiente.


## Exemplo prático

Imagine um restaurante:  
- Você faz o pedido ao **garçom** (API)  
- Ele leva sua solicitação para a **cozinha** (sistema)  
- O garçom te traz a **comida** (resposta)  

A API não precisa saber como a cozinha prepara a comida, assim como o programador não precisa se preocupar com os detalhes internos do sistema com o qual ele se comunica.

## Uso no dia a dia

As APIs estão por trás de muitos dos recursos que usamos diariamente:  
- Ao verificar a **previsão do tempo** em um aplicativo, ele usa uma API para buscar dados de um serviço meteorológico.  
- Ao fazer compras online, o site usa APIs para se comunicar com o banco e processar o pagamento.

## Áreas de utilização

As APIs são amplamente utilizadas em diversos setores da tecnologia:

- Integração de serviços web  
- Desenvolvimento de aplicativos móveis  
- Desenvolvimento de aplicativos web  
- Integração de plataformas  
- Desenvolvimento de software  
- Internet das Coisas (IoT)  
- Integração de dados  
- Automação de processos  

## APIs e Machine Learning

As APIs tornam a vida dos programadores mais fácil e possibilitam a criação de aplicativos mais complexos e integrados.  
Hoje, são cada vez mais usadas para o **deploy de modelos de Machine Learning**, permitindo que modelos treinados sejam disponibilizados e consumidos por outros sistemas de forma prática e escalável.

# O que é REST API?

Uma **REST API** (*Representational State Transfer Application Programming Interface*) é um tipo de API baseada nos princípios da arquitetura REST.  
Também conhecida como **API RESTful**, ela define um conjunto de diretrizes para a comunicação entre sistemas de forma padronizada e eficiente pela web.

Uma API RESTful bem projetada é:
- Fácil de usar
- Flexível
- Escalável  
E torna a vida dos programadores mais simples.


## Pontos-chave sobre APIs REST

- **Uso de verbos HTTP**:  
  - `GET` → Recuperar dados  
  - `POST` → Criar novos dados  
  - `PUT` → Atualizar dados existentes  
  - `DELETE` → Remover dados  

- **Foco em recursos**:  
  Um recurso pode ser um usuário, produto, pedido, etc., exposto por meio de **URLs**.

- **Stateless**:  
  Cada requisição deve conter todas as informações necessárias para ser processada.  
  O servidor **não mantém estado** entre as solicitações.


## Onde as REST APIs são utilizadas

- **Aplicativos web e móveis**: Comunicação com servidores e bancos de dados para recuperar, enviar e manipular dados.  
- **Integração de sistemas heterogêneos**: Comunicação entre diferentes componentes de software em arquiteturas distribuídas.  
- **Microsserviços**: Interação entre serviços independentes de uma aplicação.  
- **Internet das Coisas (IoT)**: Coleta e compartilhamento de dados entre dispositivos conectados.  
- **Integração com serviços de terceiros**: Acesso a funcionalidades e dados externos.  
- **APIs públicas**: Empresas disponibilizam APIs para que desenvolvedores criem integrações com seus