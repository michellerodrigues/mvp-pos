from pydantic import BaseModel
from typing import List


class CategoriaBase(BaseModel):
    nome: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int
    tarefas: List['Tarefa'] = []

    class Config:
        orm_mode = True


class TarefaBase(BaseModel):
    descricao: str
    categoria_id: int
    recorrencia_id: int
    prioridade_id: int

class TarefaCreate(TarefaBase):
    pass

class Tarefa(TarefaBase):
    id: int

    class Config:
        orm_mode = True