# Procedimento manual para Deploy na AWS

# Deploy Local 

Abra o terminal ou prompt de comando, navegue até a pasta com os arquivos e execute o comando abaixo para criar um ambiente virtual:

```
conda create --name deployml3 python=3.13
```

Ative o ambiente:

```
conda activate deployml3 (ou: source activate deployml3)
```

Instale o pip e as dependências:

```
conda install pip
pip install -r requirements.txt 
```

Execute o comando abaixo para acessar o jupyter notebook e treinar o modelo:

Modo de Desenvolvimento:
```
flask run
```

Modo de Produção (Threads):
```
gunicorn -w 4 app:app
```

Use os comandos abaixo para desativar o ambiente virtual e remover o ambiente (opcional):

```
conda deactivate
```
```
conda remove --name dsadeploymlp3 --all
```

## Deploy na AWS

Download do Miniconda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Instalação dos pacotes
```bash
pip install -r requirements.txt
```

Inicializa
```bash
gunicorn -w 4 app:app
gunicorn --bind 0.0.0.0:8000 app:app
```

Acessa (coloque aqui o endereço da sua instância EC2)
```bash
http://ec2-52-15-145-226.us-east-2.compute.amazonaws.com:8000
```

Criando Serviço

Verifica usuário e grupo
```bash
id -un
id -gn
```

Cria o arquivo de serviço
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Conteúdo do arquivo de serviço

```
[Unit]
Description=Gunicorn instance to serve application
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/home/ec2-user/Cap07
Environment="PATH=/home/ec2-user/miniconda3/bin"
ExecStart=/home/ec2-user/miniconda3/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

Gerencia o serviço
```bash
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
sudo systemctl restart gunicorn
sudo systemctl stop gunicorn
journalctl -u gunicorn
```