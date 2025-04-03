from sqlalchemy.ext.declarative import declarative_base

# cria uma classe Base para o instanciamento de novos objetos/tabelas

# qual a diferença entre usar Base Base = declarative_base() e BaseModel(Base):
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship

# Modelo base para reutilização
class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)

