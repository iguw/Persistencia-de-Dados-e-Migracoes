from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import TarefaModel
from schemas import Tarefa, TarefaCreate

app = FastAPI(title="API de Tarefas")


@app.get("/")
def raiz():
    return {"mensagem": "API de Tarefas no ar!"}


@app.get("/tarefas", response_model=list[Tarefa])
def listar_tarefas(concluida: Optional[bool] = None, db: Session = Depends(get_db)):
    query = db.query(TarefaModel)
    if concluida is not None:
        query = query.filter(TarefaModel.concluida == concluida)
    return query.all()


@app.get("/tarefas/{tarefa_id}", response_model=Tarefa)
def buscar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@app.post("/tarefas", response_model=Tarefa, status_code=201)
def criar_tarefa(dados: TarefaCreate, db: Session = Depends(get_db)):
    nova = TarefaModel(
        titulo=dados.titulo,
        descricao=dados.descricao,
        concluida=dados.concluida,
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, dados: TarefaCreate, db: Session = Depends(get_db)):
    tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa.titulo = dados.titulo
    tarefa.descricao = dados.descricao
    tarefa.concluida = dados.concluida

    db.commit()
    db.refresh(tarefa)
    return tarefa


@app.delete("/tarefas/{tarefa_id}", status_code=204)
def remover_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    db.delete(tarefa)
    db.commit()