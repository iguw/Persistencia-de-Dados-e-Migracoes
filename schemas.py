from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class TarefaCreate(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    descricao: Optional[str] = Field(default=None, max_length=300)
    concluida: bool = False


class Tarefa(TarefaCreate):
    id: int

    # permite converter o objeto do banco em Tarefa
    model_config = ConfigDict(from_attributes=True)