# Projeto Ryno

Este é projeto de um site que serve como intermediario entre cliente e profissionaus chamado Ryno.

## Pré-requisitos

Certifique-se de ter o Pytho instalado, as bibliotecas necessária e configurado na sua máquina.

[python](https://www.python.org/downloads/)

Para Instalar as bibliotecas necessárias, use o seguinte comando ápos fazer o clone do repositório para sua máquina

```bash
pip install -r requirements.txt
```

## Configuração

### Clonar o Repositório

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/Yoriel-silva/Ryno
cd Ryno
```

### Execute o app.py
```bash
python main.py
```

O servidor FastAPI será iniciado e estará acessível em http://127.0.0.1:7777.

### Acessar o Projeto

Home: http://127.0.0.1:7777

Cadastro: http://127.0.0.1:7777/cadastro

Login: http://127.0.0.1:7777/login

Perfil: http://127.0.0.1:7777/perfil

Profissionais: http://127.0.0.1:7777/profissionais

## Estrutura do Projeto
main.py: Configuração do FastAPI, definição de rotas e inicialização do servidor.

Models/: Definição dos modelos de dados utilizando SQLAlchemy.

CRUD/: Operações de criação, leitura, atualização e exclusão (CRUD) no banco de dados.

Templates/: Templates HTML usando Jinja2 para renderização dinâmica.

static/: Arquivos estáticos como CSS, imagens, etc.

requirements.txt: Lista de dependências Python necessárias para o projeto.

## Contribuição
Esse projeto foi desenvolvido durante o curso de Analise e Desenvolvimento de Sistemas, para a disciplina do Projeto Integrador
Os participantes desse projeto são : Amanda Mafra, Artur Pereira, Giovanne Galleti, Gustavo Henrique e Yoriel Silva.