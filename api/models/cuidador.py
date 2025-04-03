from sqlalchemy import Column, String, Float
from models.base import BaseModel

class Cuidador(BaseModel):
    __tablename__ = "cuidadores"
    nome = Column(String, index=True)
    especialidade = Column(String)
    telefone = Column(String)
    email = Column(String, unique=True, index=True)
    custo_hora = Column(Float)