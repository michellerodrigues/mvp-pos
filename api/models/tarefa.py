from sqlalchemy import Column, String, Integer, ForeignKey
from models.base import BaseModel

class Tarefa(BaseModel):
    __tablename__ = "tarefas"
    descricao = Column(String, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    recorrencia_id = Column(Integer, ForeignKey("recorrencias.id"))
    prioridade_id = Column(Integer, ForeignKey("prioridades.id"))