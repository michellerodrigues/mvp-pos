from pydantic import BaseModel

class ExecucaoBase(BaseModel):
    tarefa_id: int
    observacao: str
    data_execucao: date

class ExecucaoCreate(ExecucaoBase):
    pass

class Execucao(ExecucaoBase):
    id: int

    class Config:
        orm_mode = True