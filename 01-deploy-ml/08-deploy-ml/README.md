**Deploy de Modelo de Classificação Através de API em Linguagem Rust**

- Acesse o terminal ou prompt de comando, acesse a pasta onde colocou os arquivos e execute o comando abaixo para criar o projeto Rust

```bash
cargo new projeto8
```

- Acesse a pasta do projeto:

```bash
cd projeto8
```

- Coloque o arquivo dados.csv na pasta do projeto

- Edite o arquivo Cargo.toml e adicione o bloco abaixo:

```
[dependencies]
rocket = { version = "0.5.0-rc.2", features = ["json"] }
linfa = { version = "0.7.0", features = ["serde"] }
linfa-logistic = { version = "0.7.0", features = ["serde"] }
ndarray = "0.15.4"
csv = "1.1"
bincode = "1.3"
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

- Via terminal ou prompt de comando, na pasta do projeto, execute o comando abaixo para criar a versão release do projeto (versão final)

```bash
cargo build --release
```

- Na mesma pasta anterior, execute o comando abaixo.
Isso vai treinar o modelo, salvar em disco, carregar e disponibilizar via API

```bash
./target/release/projeto8
```

- Abra outro terminal ou prompt e execute o comando abaixo para enviar dados para a API e testar o modelo
 Se for usuário Windows, instale o curl: https://curl.se/

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"features": [1.0, 0.0]}'
```