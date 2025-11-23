#  MLflow

https://mlflow.org/

MLflow é uma plataforma open source para gerenciar o ciclo de vida completo de Machine Learning. Ele resolve um problema comum: quando você começa a criar muitos modelos, testar combinações, ajustar hiperparâmetros e fazer deploy, rapidamente tudo vira um caos. O MLflow organiza esse caos.

Aqui está uma explicação objetiva e clara, ponto a ponto.

## O que o MLflow faz

Ele possui quatro módulos principais.

### 1. MLflow Tracking

É o "coração" do MLflow. Serve para registrar e comparar experimentos.

Você pode salvar automaticamente:

- métricas (accuracy, RMSE, loss, etc.)
- parâmetros dos modelos
- artefatos (gráficos, arquivos, modelos exportados)
- versão do código
- tempo de execução

Depois você acessa uma interface web (mlflow ui) para comparar tudo.

É como um histórico organizado das suas execuções de ML.

### 2. MLflow Projects

Padroniza a forma como projetos são executados.

Define dependências

Define comandos de execução

Permite reprodutibilidade

Serve para rodar o mesmo experimento em outra máquina sem precisar “gambiarra”.

### 3. MLflow Models

É o módulo que padroniza como salvar e carregar modelos.

Modelos podem ser exportados nos formatos:

scikit-learn, xgboost, pytorch, tensorflow, modelos genéricos (PythonFunction)

E podem ser servidos diretamente via API:

`mlflow models serve -m path_do_modelo`

### 4. MLflow Model Registry

É um repositório central para controle de versões de modelos.

Cada modelo pode ter estados:

- Staging
- Production
- Archived

Serve para controlar modelos em produção de forma organizada.

## Para que serve no MLOps

MLflow é essencial em:

- experiment tracking
- reprodutibilidade de modelos
- deploy de modelos
- versionamento de modelos
- monitoramento básico

Ele permite que equipes trabalhem como se estivessem versionando código, mas agora versionando modelos de ML.