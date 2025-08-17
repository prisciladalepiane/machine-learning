# Docker
Docker é uma plataforma que permite criar, empacotar e executar aplicações de forma isolada e consistente em qualquer ambiente, usando imagens e containers.

## Imagem Docker

- O que é:
Uma imagem é como um molde ou modelo de um sistema.
Ela contém tudo que é necessário para rodar um aplicativo: sistema operacional base, bibliotecas, dependências, variáveis de ambiente e o próprio código.

- Características:

    - É imutável (não muda depois de criada).

    - É versionada (você pode ter várias versões da mesma imagem).

    - É criada a partir de um Dockerfile, que descreve passo a passo o que a imagem deve conter.

## Container Docker

- O que é:
Um container é uma instância em execução de uma imagem.
É a imagem viva, com processos ativos e seu próprio ambiente isolado.

- Características:

    - É efêmero (pode ser criado, parado, reiniciado ou apagado facilmente).

    - Pode ter arquivos gravados durante a execução, mas essas mudanças não alteram a imagem original.

    - Vários containers podem ser criados a partir da mesma imagem.

# Dockerfile

Um **Dockerfile** é um arquivo de texto que contém instruções para o Docker construir uma **imagem**.  
Ele descreve passo a passo o ambiente necessário (SO base, bibliotecas, dependências, código, variáveis, etc.).


## Estrutura Básica do Dockerfile

### 1. FROM
Define a imagem base.
```dockerfile
FROM python:3.11
```

### 2. WORKDIR
Define o diretório de trabalho dentro do container.  
```dockerfile
WORKDIR /app
```

### 3. COPY
Copia arquivos do host para dentro do container.
```dockerfile
COPY requirements.txt .
COPY . .
```

### 4. RUN
Executa comandos no momento de build da imagem.
```dockerfile
RUN pip install -r requirements.txt
```

### 5. CMD
Define o comando padrão quando o container roda.
```dockerfile
CMD ["python", "app.py"]
```

### 6. ENTRYPOINT
Similar ao CMD, mas fixa um comando principal.

```dockerfile
ENTRYPOINT ["python", "app.py"]
```

### 7. EXPOSE

Indica a porta que o container usará.
```dockerfile
EXPOSE 5000
```

### 8. ENV

Define variáveis de ambiente.
```dockerfile
ENV APP_ENV=production
```

### Exemplo Simples de Dockerfile (Flask app em Python)

```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

### Principais Comandos do Docker

Criar imagem a partir de um Dockerfile
```bash
DOCKER BUILD -T MINHA-IMAGEM:1.0 .
```

Rodar um container da imagem
```bash
DOCKER RUN -D -P 5000:5000 MINHA-IMAGEM:1.0
```

Listar containers rodando
```bash
DOCKER PS
```

Listar todas as imagens
```bash
DOCKER IMAGES
```

Parar container
```bash
DOCKER STOP <ID_CONTAINER>
```

Remover container
```bash
DOCKER RM <ID_CONTAINER>
```

Remover imagem

```bash
DOCKER RMI MINHA-IMAGEM:1.0
```