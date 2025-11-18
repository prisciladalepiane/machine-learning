# DOCKER

Docker é uma plataforma que permite criar, empacotar e executar aplicações em ambientes isolados chamados containers.

Documentação: https://docs.docker.com/get-started/get-docker/

## Explorando a Interface:

### _Images_ (Imagem)

Uma **imagem Docker** é um pacote imutável que reúne tudo o que uma aplicação precisa para rodar: sistema base, dependências, bibliotecas, arquivos e configurações. Ela funciona como uma receita pronta: a partir dela o Docker cria containers, que são instâncias em execução dessa imagem. Como a imagem não muda, ela garante que o software rode sempre da mesma forma em qualquer ambiente, seja no seu computador, em um servidor ou na nuvem.

As imagens Docker ficam armazenadas em registries, que são repositórios próprios para distribuir imagens. O mais comum é o [**Docker Hub**](hub.docker.com), que é público e gratuito para a maioria dos usos. Lá encontra-se imagens oficiais como python, ubuntu, postgres e também imagens criadas pela comunidade.
Além do Docker Hub, existem registries privados e de nuvem como GitHub Container Registry, AWS ECR, Google Artifact Registry e Azure Container Registry, onde empresas e desenvolvedores guardam suas próprias imagens. Você também pode criar suas imagens localmente e listá-las com o comando `docker images`.

### _Conteiners_
Um container é um ambiente isolado onde uma aplicação roda com tudo o que ela precisa, sem interferir no sistema operacional principal e sem depender do que está instalado na máquina. Ele é criado a partir de uma imagem e funciona como uma instância leve e rápida, oferecendo isolamento de dependências, reprodutibilidade e portabilidade. Em prática, um container garante que a aplicação rode exatamente igual em qualquer lugar, seja no seu computador, em um servidor ou na nuvem. É por isso que containers são usados em desenvolvimento, deploy, MLOps e microserviços.

### _Builds_

É o processo de **construir uma imagem** a partir de um Dockerfile. Quando você faz um build, o Docker lê cada instrução do Dockerfile, cria as camadas, instala dependências, copia arquivos e monta o ambiente final que será usado nos containers. Em resumo, o build transforma o Dockerfile em uma imagem pronta para rodar.