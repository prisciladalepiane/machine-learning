# Engenharia de Machine Learning

Na Ciência de Dados, o foco principal é extrair insights e conhecimentos a partir de dados brutos, usando estatística, análise exploratória e modelos preditivos. Essa etapa é fundamental para entender os padõres, tendências e relações nos dados, fornecendo a base para decisões informadas.

No entanto, a aplicação prática desses insights em produtos ou serviços requer uma transformação desses modelos analíticos em componentes integrados de sistema de software funcionais e escaláveis. É nesse ponto que a **Engenharia de Machine Learning** entra em cena, marcando a transição para uma fase onde a viabilidade tecnológica se torna protagonista.

A engenharia de ML envolve práticas de engenharia de software aplicada ao ciclo de vida dos modelos de ML, incluindo versionamento de código, testes, integração e entrega contínua e gerenciamento de infraestrutura. Essas práticas são essenciais para assegurar os testes, mas também se mantenham eficazes e confiáveis quando implementados em ambientes de produção reais, onde enfrentarão dados em constante evolução e condições imprevistas.

## Definição de MLOps

MLOps, ou MAchine Learning Operation, é  uma prática interdisciplinar que visa operacionalizar o aprendizado de máquina para simplificar e acelerar a implantação de modelos de ML em produção de forma escalávels e confiável.

Essa prática é uma extensão da metodologia DevOps, aplicada especificamente ao contexto de desenvolvimento e operacionalização de sistemaas de aprendizado de máquina.

6 Fatotes que ajudam a explicar a importância do MLOps:

1. **Aceleração do cliclo de vida de modelos de ML**
MLOps permite uma transição mais rápida de modelos de ML do desenvolvimento para a produção.
Em ambientes de negócio onde a velocidade de implantação pode ser um diferencial competitivo, isso é essencial.
O modelo de ML é um arquivo em disco, recheado de números, que deve ser carregado na memória do computador.

2. **Garantia de qualidade e confiabilidade**
Ao incorporar práticas de operações, como integração contínua (CI) e entrega contínua (CD), MLOps ajuda a garantir que os modelos sejam robustos, seguros e performáticos antes de serem lançados em ambientes de produção.

3. **Escalabilidade e gerenciamento de recursos**
Facilita o gerenciamento de recursos computacionais e a escalabilidade de soluções de ML. Com práticas de MLOps, organizações podem gerenciar melhor os custos e a complexidade operacional à medida que suas soluções de ML crescem em escala.

4. **Monitoramento e Manutenção de modelos**
Uma vez em produção os modelos de ML precisam ser continuamente monitorados para garantir que permaneçam eficazes a medida que os padrões de dados mudam. MLOps inclui práticas e ferramentas para o monitoramento contínuo e manutenção de modelos de ML, permitindo ajustes e atualizações rápidas conforme necessário.

5. **Colaboração com equipes** 
MLOps promove uma colaboração mais estreita entre cientista de dados, engenheiros de ML e proficionais de operação, ajudando a quebrar silos e melhorar a comunicação. Isso é fundamental para alinhar esforços de desenvolvimento de ML com os objetivos de negócio e as necessidades operacionais. 

6. **Governança e conformidade** 
Também aborda aspectos de governança, privancidade e conformidade regulatória dos modelos de ML que são críticos em muitos setores, como saúde, finanças e serviços públicos. 

MLOps é fundamental em empresas que desejam aproveitar ao máximo o pontencial do machine learning, assegurando que seus investimentos em IA/ML sejam traduzidos em valor real de negócios de maneira  eficiente, segura e sustentavel. 

## End-to-End Machine Learning Workflow

End-to-end no contexto de um workflow de Machine Learning refere-se ao processo completo de desenvolvimento de um modelo, desde a concepção inicial até a sua implantação e uso prático. 

A abordagem end-to-end visa criar um pipeline automatizado e otimizado que minimiza a intervenção manual e maximiza a eficácia e eficiência do modelo em produção, facilitando a aplicação direta de insights derivados dos dados para resolver problemas reais.

Visão geral das etapas end-to-end ML Workflow:

1. Definição do Problema: Identificar claramente o problema que precisa ser solucionado.


2. Coleta de Dados: Obter dados necessários de diversas fontes.

3. Limpeza e Preparação dos Dados: Processar os dados para remover inconsistências, tratar valores ausentes e formatar os dados adequadamente para análise.

4. Análise Exploratória de Dados (EDA): Usar visualizações e estatísticas para explorar os dados e identificar padrões ou insights.

5. Engenharia de Features: Modificar ou criar novas features para melhorar a performance do modelo.

6. Divisão dos Dados: Separar os dados em conjuntos de treinamento, validação e teste.

7. Seleção e Treinamento de Modelos: Escolher o algoritmo adequado e treinar o modelo com o conjunto de treinamento.

8. Avaliação do Modelo: Usar o conjunto de validação para ajustar os hiperparâmetros e verificar se o modelo está superajustando (overfitting).

9. Teste do Modelo: Testar o modelo final com o conjunto de teste para avaliar sua performance com dados novos.

10. Implantação: Colocar o modelo em um ambiente de produção para que possa fazer previsões em tempo real.

11. Monitoramento e Manutenção: Monitorar o desempenho do modelo para garantir que continue eficiente e fazer ajustes conforme necessário.

12. Atualização do Modelo: Reavaliar e atualizar o modelo periodicamente para incluir novos dados ou adaptar-se a mudanças no ambiente.

## O que signivica "Ops" em MLOps

O termo "Ops" em MLOps deriva de "operations" (operações) e refere-se a todos os processos operacionais envolvidos na preparação, teste, implantação, monitoramento e manutenção de sistemas de Machine Learning em ambientes de produção.

O objetivo é facilitar a colaboração entre Cientistas de Dados e equipes de operações, melhorar a qualidade e consistência dos modelos implementados, e acelerar o ciclo de vida do desenvolvimento de modelos de Machine Learning.

Aspectos Principais de "Ops" em MLOps:

1. Integração e Entrega Contínua (CI/CD):


Integração Contínua (CI): Automatiza a integração de código e modelos para validar sua qualidade através de testes automáticos.
Entrega Contínua (CD): Automatiza o lançamento de modelos validados para ambientes de teste e produção, garantindo que as versões possam ser implantadas a qualquer momento.

2. Monitoramento e Manutenção:

Monitorar o desempenho do modelo para detectar e corrigir degradações ou mudanças nos padrões de dados.
Manter e atualizar os sistemas conforme necessário para garantir a precisão e eficiência contínuas.

3. Gestão de Configuração e Infraestrutura:

Configurar e gerenciar a infraestrutura necessária para treinar e servir modelos em escala.
Gerenciar as configurações dos sistemas para garantir consistência e reprodutibilidade.

4. Gestão de Dados:

Gerenciar pipelines de dados para garantir a qualidade e a disponibilidade dos dados usados para treinamento e inferência.
Implementar práticas de governança de dados para manter a integridade e a segurança dos dados.

5. Controle de Versão e Artefatos:

Manter o controle de versão de modelos, dados e códigos para permitir a rastreabilidade e facilitar rollbacks se necessário.
Gerenciar os artefatos de Machine Learning, incluindo modelos treinados e componentes associados.

6. Colaboração entre Equipes:

Facilitar a colaboração eficaz entre cientistas de dados, engenheiros de software, e equipes de operações.
Promover uma cultura de compartilhamento de conhecimento e melhores práticas.


> MLOps é vital para implementar práticas de Machine Learning que são sustentáveis, eficientes e que maximizam o retorno sobre o investimento em iniciativas de dados e AI.
Ele além de melhorar a velocidade e a qualidade do desenvolvimento de modelos, também garante que esses modelos permaneçam válidos e úteis no ambiente em constante mudança de uma aplicação de negócios real.