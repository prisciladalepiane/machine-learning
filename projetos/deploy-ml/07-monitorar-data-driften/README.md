# Projeto 7 - Monitoramento, Identificação e Mitigação de Model e Data Drift

Este  projeto  tem  como  objetivo  desenvolver  um  sistema  para  monitorar,  identificar  e mitigar  Model  Drift  e  Data  Drift  em  modelos  de  Machine  Learning.  Serão  implementadas estratégias de mitigação, incluindo  o retreinamentodos  modelos  com dados atualizados. 

Os dados usados no projeto foram extraídos do link:

https://archive.ics.uci.edu/dataset/109/wine


Abra o terminal ou prompt de comando, navegue até a pasta com os arquivos 

```bash
    cd projetos/deploy-ml/07-monitorar-data-driften
```

execute o comando abaixo para criar um ambiente virtual:

```bash
conda create --name .venv7 python=3.13
```

Ative o ambiente:

```bash
conda activate venv7 (ou: source activate venv7)
```

# Instale o pip e as dependências:

```bash
conda install pip
pip install -r requirements.txt 
```
Execute:

```bash
python parte1.py
```

Use os comandos abaixo para desativar o ambiente virtual e remover o ambiente (opcional):

```bash
conda deactivate
conda remove --name venv7 --all
```