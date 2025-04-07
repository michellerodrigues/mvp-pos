from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from database.database import Base

# Modelo base para reutilização
class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)