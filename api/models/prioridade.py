from sqlalchemy import Column, String
from models.base import BaseModel

class Prioridade(BaseModel):
    __tablename__ = "prioridades"
    nivel = Column(String, unique=True, index=True)
    descricao = Column(String)