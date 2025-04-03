from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from models.base import BaseModel

class Execucao(BaseModel):
    __tablename__ = "execucoes"
    tarefa_id = Column(Integer, ForeignKey("tarefas.id"))
    data_execucao = Column(DateTime, nullable=False)
    observacoes = Column(String)