from pydantic import BaseModel
from typing import List
from schemas.tarefa import Tarefa


class CategoriaBase(BaseModel):
    nome: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int
    tarefas: List[Tarefa] = []  # Lista de tarefas

    class Config:
        orm_mode = True