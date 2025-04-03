from sqlalchemy import Column, String
from models.base import BaseModel

class Recorrencia(BaseModel):
    __tablename__ = "recorrencias"
    descricao = Column(String, unique=True, index=True)