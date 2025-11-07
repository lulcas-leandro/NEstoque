# NEstoque - Sistema de Gerenciamento de Estoque

Sistema web para controle de estoque desenvolvido com Flask, permitindo cadastro de produtos, controle de movimentações (entradas e saídas) e autenticação de usuários.

## Tecnologias Utilizadas

- **Python 3.11**
- **Flask** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **Flask-Login** - Gerenciamento de autenticação
- **Flask-Migrate** - Migrações de banco de dados
- **Flask-WTF** - Formulários e validação
- **PostgreSQL** - Banco de dados (produção)
- **SQLite** - Banco de dados (desenvolvimento)
- **Docker & Docker Compose** - Containerização
- **Gunicorn** - Servidor WSGI

## Funcionalidades

- Autenticação de usuários (login/logout/registro)
- Cadastro, edição e exclusão de produtos
- Controle de estoque com SKU único
- Registro de movimentações (entradas e saídas)
- Histórico completo de movimentações por produto
- Validação de quantidade disponível em saídas
- Interface responsiva e intuitiva

## Estrutura do Projeto

```
nestoque/
├── app/
│   ├── auth/              # Módulo de autenticação
│   │   ├── forms.py       # Formulários de login/registro
│   │   └── routes.py      # Rotas de autenticação
│   ├── models/            # Modelos de dados
│   │   ├── user.py        # Modelo de usuário
│   │   └── stock.py       # Modelos de produto e movimentação
│   ├── stock/             # Módulo de estoque
│   │   ├── forms.py       # Formulários de produtos
│   │   └── routes.py      # Rotas de estoque
│   ├── static/            # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/         # Templates HTML
│   ├── config.py          # Configurações da aplicação
│   ├── extensions.py      # Extensões Flask
│   └── __init__.py        # Factory da aplicação
├── migrations/            # Migrações do banco de dados
├── instance/              # Banco de dados SQLite (dev)
├── docker-compose.yml     # Configuração Docker Compose
├── Dockerfile             # Imagem Docker
├── requirements.txt       # Dependências Python
├── run.py                 # Ponto de entrada da aplicação
└── .env.example           # Exemplo de variáveis de ambiente
```

## Instalação e Configuração

### Pré-requisitos

- Python 3.11+
- pip
- virtualenv (opcional, mas recomendado)
- Docker e Docker Compose (para execução em container)

### Instalação Local

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nestoque.git
cd nestoque
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
# Copie o arquivo de exemplo
cp .env.example .env
```

Edite o arquivo `.env` e configure:
- **SECRET_KEY**: Gere uma chave secreta forte com:
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- **DATABASE_URL**: Para desenvolvimento, mantenha SQLite:
  ```
  DATABASE_URL=sqlite:///nestoque.db
  ```
  Para produção com PostgreSQL:
  ```
  DATABASE_URL=postgresql://usuario:senha@host:5432/nome_db
  ```

5. Inicialize o banco de dados:
```bash
flask db upgrade
```

6. Execute a aplicação:
```bash
python run.py
```

A aplicação estará disponível em `http://localhost:5000`

### Execução com Docker

1. Configure as variáveis de ambiente no arquivo `.env`

2. Inicie os containers:
```bash
docker-compose up -d
```

3. Execute as migrações:
```bash
docker-compose exec web flask db upgrade
```

A aplicação estará disponível em `http://localhost:5008`


## Uso

1. Acesse a aplicação e crie uma conta
2. Faça login com suas credenciais
3. Cadastre produtos com SKU, nome e descrição
4. Registre entradas e saídas de estoque
5. Visualize o histórico de movimentações


## Variáveis de Ambiente

O projeto utiliza as seguintes variáveis de ambiente:

**SECRET_KEY**: Chave secreta para sessões Flask. Gere uma chave forte com:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**DATABASE_URL**: URL de conexão com o banco de dados.
- Desenvolvimento (SQLite): `sqlite:///nestoque.db`
- Produção (PostgreSQL): `postgresql://usuario:senha@host:5432/nome_db`

**DB_PASSWORD**: Senha do PostgreSQL (usado apenas no Docker Compose)

## Docker

O projeto inclui configuração completa para containerização:

**Dockerfile**: Imagem baseada em Python 3.11-slim com Gunicorn rodando na porta 5000.

**docker-compose.yml**: Orquestração de dois serviços:
- **web**: Aplicação Flask (acessível na porta 5008 do host)
- **db**: PostgreSQL 15-alpine com healthcheck e persistência de dados

**Recursos**:
- Volumes persistentes para dados do banco
- Restart automático dos containers
- Network isolada para comunicação entre serviços
- Healthcheck no PostgreSQL

## Segurança

- Senhas criptografadas com Werkzeug
- Proteção CSRF em formulários
- Rotas protegidas com @login_required
- Validação de dados no backend

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
