# Persistência de Dados e Migrações (FastAPI + SQLAlchemy)

API RESTful com CRUD de tarefas, usando FastAPI, SQLAlchemy, SQLite e migrações com Alembic.

## Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/iguw/Persistencia-de-Dados-e-Migracoes.git
   cd Persistencia-de-Dados-e-Migracoes
   ```

2. Crie e ative o ambiente virtual:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
   No Linux/macOS: `source venv/bin/activate`

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie o banco de dados aplicando as migrações:
   ```bash
   alembic upgrade head
   ```

5. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

6. Acesse a documentação Swagger em http://127.0.0.1:8000/docs

### Usando o VS Code

1. Abra a **pasta do projeto** (`File > Open Folder...`), e não a pasta de cima.
2. Abra o terminal integrado (`` Ctrl + ` ``) e siga os passos 2 a 5 acima.
3. Selecione o interpretador: `Ctrl + Shift + P`, **Python: Select Interpreter** e escolha `.\venv\Scripts\python.exe`.

## Autor

Guilherme Alves ([@iguw](https://github.com/iguw))