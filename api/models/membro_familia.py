from sqlalchemy import Column, String
from models.base import BaseModel

class MembroFamilia(BaseModel):
    __tablename__ = "membros_familia"
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefone = Column(String)
    tipo = Column(String)  # Responsável ou Familiar