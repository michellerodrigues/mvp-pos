from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    nome = Column(String, unique=True, index=True)
    tarefas = relationship("TarefaModel", back_populates="categoria")