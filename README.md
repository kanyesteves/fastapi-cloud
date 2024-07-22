# API REST VOLATEX

## Introdução
Bem-vindo à documentação da API REST VOLATEX. Esta API permite fazer todas as validações dos dados que serão registrados no banco de dados do sistema de controle interno de produção para a empresa Volatex. Abaixo estão os detalhes sobre como utilizar os endpoints disponíveis.

## Configurando ambiente

###  Clonar o repositório do projeto
Rode o comando abaixo para clonar o projeto em sua máquina

    $ git clone git@github.com:kanyesteves/fastapi-cloud.git

###  Criar ambiente virtal
Crie um ambiete virtual para rodar as dependências necessárias para rodar o projeto

    $ python3 -m venv fastapicloud && source fastapicloud/bin/activate

### Atualize o gerenciador de pacotes (pip)

    $ pip install --upgrade pip

### Instale todas as dependências que serão utilizadas no projeto

    $ pip install -r requirements.txt


## Acessando a API

### Inicie a API com o comando abaixo

    $ uvicorn run:app

### Visualize a documentação de todos os endpoints pela URL

    $ http://localhost:8000/docs