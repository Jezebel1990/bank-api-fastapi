# API Bancária Assíncrona com FastAPI

Uma API RESTful assíncrona desenvolvida com **FastAPI** para gerenciar operações bancárias de depósitos e saques vinculadas a contas correntes. Esta aplicação backend moderna e eficiente utiliza autenticação JWT e segue boas práticas de design de APIs.

---

## 🚀 Objetivos e Funcionalidades

A API foi desenvolvida para fornecer funcionalidades essenciais de um sistema bancário, incluindo:

- **Cadastro de Transações**  
  Permite registrar transações bancárias, como depósitos e saques, vinculadas a contas correntes.

- **Exibição de Extrato**  
  Endpoint para exibir o extrato de uma conta, listando todas as transações realizadas.

- **Autenticação com JWT**  
  Garantia de que apenas usuários autenticados possam acessar endpoints protegidos usando **JSON Web Tokens**.

- **Validação de Operações**  
  - Não permite depósitos ou saques com valores negativos.  
  - Valida se o usuário possui saldo suficiente antes de realizar um saque.

- **Modelagem de Dados**  
  Modelos para representar **contas correntes** e **transações**, garantindo que contas possam ter múltiplas transações.

- **Segurança**  
  Autenticação JWT para proteger endpoints críticos da API.

- **Documentação com OpenAPI**  
  API documentada com todos os endpoints, parâmetros e modelos de dados, acessível via `/docs`.

---

## 🛠 Tecnologias Utilizadas

- [Python 3.12](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [JWT (PyJWT)](https://pyjwt.readthedocs.io/)
- [Alembic](https://alembic.sqlalchemy.org/) para migrations
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências

---

## ⚙️ Como Rodar o Projeto

1. **Clone o repositório**
```bash
git clone https://github.com/Jezebel1990/bank-api-fastapi.git
cd bank-api-fastapi
```

2. **Instale as dependências**
```bash
poetry install
```

3. **Configure variáveis de ambiente**
Crie um arquivo `.env` com as configurações necessárias, por exemplo:

```bash
DATABASE_URL=sqlite+aiosqlite:///./bank.db
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. **Execute as migrations**

```bash
alembic upgrade head
```

5. **Inicie a API**

```bash
poetry run uvicorn src.main:app --reload
```

6. **Acesse a documentação**

http://127.0.0.1:8000/docs

---

## 🔒 Segurança

- Todos os endpoints sensíveis estão protegidos por JWT.
- Validação de saldo antes de saques.
- Não permite valores negativos em transações.

---
## 👩‍💻 Autora
Feito com ❤️ por [Jezebel Guedes](https://www.linkedin.com/in/jezebel-guedes/) 👋Vamos nos conectar!