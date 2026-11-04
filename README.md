# Persistência de Dados e Migrações

Atividade da disciplina de APIs e Microsserviços. É uma API de tarefas feita com FastAPI que agora salva os dados em um banco SQLite. O banco é controlado com SQLAlchemy, e a criação da tabela é feita com Alembic.

## Como rodar

1. Baixe o projeto:
   ```
   git clone https://github.com/iguw/Persistencia-de-Dados-e-Migracoes.git
   cd Persistencia-de-Dados-e-Migracoes
   ```

2. Crie e ative o ambiente virtual:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Crie o banco com a migração:
   ```
   alembic upgrade head
   ```

5. Rode a API:
   ```
   uvicorn main:app --reload
   ```

6. Abra http://127.0.0.1:8000/docs para testar as rotas.

## Autor

Guilherme Alves - [@iguw](https://github.com/iguw)