# Frameworks e Ferramentas para construir modelos de Deep Learning

Modelos de Deep Learning podem ser criados a partir do zero via programação ou através de frameworks. Só vale a pena constrir do zero se há necessidade de muitas customizações. 

Seguem alguns frameworks que foram descontinuados:

- Theano (deu origem aos principais frameworks da atualidade)
- Chainer 
- Microsoft CNTK
- Caffe e Caffe2

Principais Frameworks da atualidade (Python e C++):

- PyTorch: Excelente em visão computacional
- TensorFlow 
- Keras: Criado para simplificar o TensorFlow, hoje faz parte do mesmo.

Alternativas:

- MxNet
- JAX
- Open Neural Network Exchange (ONNX)

Bibliotecas para C++:

- Armadillo
- MLPack

## Criação de Ambientes virtuais em python

Um ambiente virtual Python é um isolamento controlado do interpretador Python e seus pacotes, criado para que você possa trabalhar em um projeto sem interferir nos pacotes globais do sistema ou em outros projetos.

Imagine dois projetos: \
-Projeto A precisa do pandas na versão 1.5.\
-Projeto B precisa do pandas na versão 2.3.

Se você instalar  ambos  no sistema, um sobrescreve o outro. Ambientes virtuais evitam esse conflito, permitindo que cada projeto tenha suas próprias dependências e versões.O que ele contém:

- Uma cópia (ou link) do interpretador Python.
- Um diretório separado com todos os pacotes instalados para aquele ambiente. 
- Scripts de ativação e desativação do ambiente.

O _conda env_ é um recurso do Conda (gerenciador de pacotes e ambientes) que permite criar ambientes isolados com versões específicas de Python, bibliotecas e dependências. O conda env é um comando que gerencia ambientes virtuais no Conda, garantindo que diferentes  projetos  possam  usar  configurações e versões de pacotes independentes uns dosoutros.Benefícios:

-Isolamento total: evita conflitos de dependências entre projetos. \
-Reprodutibilidade: facilita replicar ambientes em outras máquinas \
-Compatibilidade: permite testar códigos com diferentes versões dos pacotes.\
-Gerenciamento  centralizado:  integra  pacotes  Python,  R,  C/C++,  etc.,  em  um  só ambiente.Abaixo alguns exemplos de uso.

Criação:
```bash
conda create --name meu_ambiente python=3.13
```

Instalação de pacotes(um dos 2 comandos abaixo):
```bash
conda install numpy pandas
pip install -r requirements.txt
```
Exportação:
```bash
conda env export > environment.yml
```
Recriação do ambiente
```bash
conda env create -f environment.yml
```
Remoção:
```bash
conda remove --name meu_ambiente --all
```