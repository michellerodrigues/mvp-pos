from pydantic import BaseModel

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