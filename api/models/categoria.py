from sqlalchemy import Column, String
from models.base import BaseModel

class Categoria(BaseModel):
    __tablename__ = "categorias"
    nome = Column(String, unique=True, index=True)