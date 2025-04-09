from datetime import datetime
import json
from sqlalchemy import Column, ForeignKey, Integer, DateTime, String,Text
from sqlalchemy.orm import relationship
from schemas.questionario import OpcaoSchema, PerguntaSchema
from models.base import BaseModel, CompositeKeyBase
from database.database import Base


class PerguntaModel(BaseModel):
    __tablename__ = 'perguntas'

    texto = Column(Text, nullable=False)
    tipo = Column(String(10), nullable=False)
    
    # Relações
    opcoes = relationship("OpcaoModel", back_populates="pergunta")

   
class QuestionarioModel(BaseModel):
    __tablename__ = 'questionario'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    data_criacao = Column(DateTime, default=datetime.now)
    respostas = relationship('RespostaModel', back_populates="questionario")
    

class OpcaoModel(BaseModel):
    __tablename__ = 'opcoes'
        
    texto = Column(Text, nullable=False)
    tags = Column(Text, nullable=False)
    pergunta_id = Column(Integer, ForeignKey('perguntas.id'))
    
    # Relações
    pergunta = relationship("PerguntaModel", back_populates="opcoes")
    respostas = relationship("RespostaModel", back_populates="opcao")
    

class RespostaModel(CompositeKeyBase):
    __tablename__ = 'respostas'
    questionario_id = Column(Integer, ForeignKey('questionario.id'), primary_key=True)
    opcao_id = Column(Integer, ForeignKey('opcoes.id'), primary_key=True)
    
    # Relações
    questionario = relationship("QuestionarioModel", back_populates="respostas")
    opcao = relationship("OpcaoModel", back_populates="respostas")