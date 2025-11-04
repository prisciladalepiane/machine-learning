# API e REST API

## O que é API?

**API** significa *Interface de Programação de Aplicações* (em inglês, *Application Programming Interface*).  
É um conjunto de regras e padrões que permite a comunicação entre diferentes programas de computador.  
Pense nela como um intermediário, facilitando a troca de informações entre sistemas de forma segura e eficiente.


### Exemplo prático

Imagine um restaurante:  
- Você faz o pedido ao **garçom** (API)  
- Ele leva sua solicitação para a **cozinha** (sistema)  
- O garçom te traz a **comida** (resposta)  

A API não precisa saber como a cozinha prepara a comida, assim como o programador não precisa se preocupar com os detalhes internos do sistema com o qual ele se comunica.

### Uso no dia a dia

As APIs estão por trás de muitos dos recursos que usamos diariamente:  
- Ao verificar a **previsão do tempo** em um aplicativo, ele usa uma API para buscar dados de um serviço meteorológico.  
- Ao fazer compras online, o site usa APIs para se comunicar com o banco e processar o pagamento.

### Áreas de utilização

As APIs são amplamente utilizadas em diversos setores da tecnologia:

- Integração de serviços web  
- Desenvolvimento de aplicativos móveis  
- Desenvolvimento de aplicativos web  
- Integração de plataformas  
- Desenvolvimento de software  
- Internet das Coisas (IoT)  
- Integração de dados  
- Automação de processos  

### APIs e Machine Learning

As APIs tornam a vida dos programadores mais fácil e possibilitam a criação de aplicativos mais complexos e integrados.  
Hoje, são cada vez mais usadas para o **deploy de modelos de Machine Learning**, permitindo que modelos treinados sejam disponibilizados e consumidos por outros sistemas de forma prática e escalável.

## O que é REST API?

Uma **REST API** (*Representational State Transfer Application Programming Interface*) é um tipo de API baseada nos princípios da arquitetura REST, ou seja, uma API com regras.  
Também conhecida como **API RESTful**, ela define um conjunto de diretrizes para a comunicação entre sistemas de forma padronizada e eficiente pela web.

Uma API RESTful bem projetada é:
- Fácil de usar
- Flexível
- Escalável  
- Torna a vida dos programadores mais simples.

O Rest delimita algumas obrigações nas transferências de dados. 
Dados são chamados de resources, qeu pode ser uma entidade ou um objeto.

Ser RESTful é cumprir os padrões REST.

### Necessidades (constraints) para ser RESTful:

- _Client-server_: Separação cliente servidor.

- _Stateless_: Cada requisição (REQUEST) que o cliente faz para o servidor, deverá conter todas as informações necessárias para o servidor entender e responder (RESPONSE). O servidor não pode armazenar estados entre as solicitações. 

- _Cacheable_: As respostas para uma requisição, deverão ser explicitas ao dizer se aquela requisição, pode ou não ser cacheada pelo cliente.

- _Layered System_: O cliente acessa a um endpoint sem precisar saber da complexidade.

- _Code on demand_: Opcional, envia pro cliente algun script.

### Pontos-chave sobre APIs REST

- **Uso de verbos HTTP**:  
  - `GET` → Recuperar dados  
  - `POST` → Criar novos dados  
  - `PUT` → Atualizar dados existentes  
  - `DELETE` → Remover dados  

- **Foco em recursos**:  
 REST foca em recursos. Um recurso pode ser um usuário, produto, um pedido ou qualquer outra entidade relevante no sistema, exposto por meio de **URLs**.

- **Stateless**:  
  Cada requisição deve conter todas as informações necessárias para ser processada.  
  O servidor **não armazena nenhum estado** entre as solicitações.


### Onde as REST APIs são utilizadas

- **Aplicativos web e móveis**: Comunicação com servidores e bancos de dados para recuperar, enviar e manipular dados.  
- **Integração de sistemas heterogêneos**: Comunicação entre diferentes componentes de software em arquiteturas distribuídas.  
- **Microsserviços**: Interação entre serviços independentes de uma aplicação.  
- **Internet das Coisas (IoT)**: Coleta e compartilhamento de dados entre dispositivos conectados.  
- **Integração com serviços de terceiros**: Acesso a funcionalidades e dados externos.  
- **APIs públicas**: Empresas disponibilizam APIs para que desenvolvedores criem integrações com seus

## Consumo da API

Para consumir uma API criada para o deploy de um modelo de Machine Learning, você pode utilizar várias ferramentas e linguagens de programação. Aqui estão algumas opções:

_Python Requests_: Biblioteca popular para fazer requisições HTTP de forma simples e eficiente.

_Postman_: Ferramenta gráfica para testar e automatizar chamadas de API, visualizando respostas em tempo real.

_cURL_: Ferramenta de linha de comando para fazer requisições HTTP, ideal para scripts e automações.

_JavaScript Fetch API_: Utilizada em aplicativos web para fazer chamadas HTTP de forma assíncrona.

Essas opções cobrem uma variedade de linguagens e ferramentas, permitindo a integração com APIs de Machine Learning em diversos ambientes de desenvolvimento.

## APIs RESTful Para Modelos de Machine Learning

APIs RESTful (Representational State Transfer) são amplamente utilizadas para expor modelos de Machine Learning como serviços acessíveis via HTTP, permitindo que aplicações externas façam previsões ou utilizem funcionalidades de aprendizado de máquina em tempo real. A criação de uma API RESTful para um modelo de Machine Learning envolve vários aspectos, desde a implementação até a segurança e escalabilidade.

### Benefícios de Usar APIs RESTful para Modelos de Machine Learning

**Facilidade de Integração**: APIs RESTful são baseadas em HTTP e utilizam formatos de dados comuns como JSON, o que facilita a integração com uma ampla variedade de clientes, incluindo aplicativos web, móveis e outras APIs.

**Escalabilidade**: APIs podem ser facilmente escaladas horizontalmente para lidar com um grande número de requisições simultâneas, tornando-as ideais para aplicações de Machine Learning em produção.

**Desacoplamento**: A separação entre o cliente e o servidor facilita a manutenção e a evolução do sistema. A lógica de aprendizado de máquina pode ser atualizada ou substituída sem impactar os clientes que consomem a API.

**Flexibilidade**: APIs RESTful permitem o uso de múltiplos métodos HTTP (GET, POST, PUT, DELETE), o que pode ser útil para expor diferentes funcionalidades, como fazer previsões, atualizar modelos, ou gerenciar dados.

### Como Criar uma API RESTful para um Modelo de Machine Learning

Existem várias opções para criar APIs RESTful, dependendo do ambiente e da linguagem de programação:

**Flask/Django (Python)**: Muito populares para criar APIs em Python, especialmente quando o modelo de Machine Learning é desenvolvido em frameworks como TensorFlow, PyTorch ou scikit-learn.

**FastAPI (Python)**: Ganha popularidade devido à sua performance e suporte a validação de dados com base em tipo, além de ser altamente otimizada para uso com Python moderno (asyncio).

**Express.js (Node.js)**: Comum para APIs JavaScript, pode ser usado quando a aplicação cliente também é baseada em JavaScript.

**Rust com Actix ou Rocket**: Para quem busca alta performance e segurança, essas bibliotecas são ideais para APIs em Rust.