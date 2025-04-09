from sqlalchemy import Column, String
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    nome = Column(String, unique=True, index=True)
    tarefas = relationship("TarefaModel", back_populates="categoria")


class TarefaModel(BaseModel):
    __tablename__ = "tarefas"
    descricao = Column(String, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    recorrencia_id = Column(Integer, ForeignKey("recorrencias.id"))
    prioridade_id = Column(Integer, ForeignKey("prioridades.id"))
    categoria = relationship("CategoriaModel", back_populates="tarefas")


class RecorrenciaModel(BaseModel):
    __tablename__ = "recorrencias"
    descricao = Column(String, unique=True, index=True)


class PrioridadeModel(BaseModel):
    __tablename__ = "prioridades"
    nivel = Column(String, unique=True, index=True)
    descricao = Column(String)