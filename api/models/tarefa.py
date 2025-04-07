from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

class TarefaModel(BaseModel):
    __tablename__ = "tarefas"
    descricao = Column(String, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    recorrencia_id = Column(Integer, ForeignKey("recorrencias.id"))
    prioridade_id = Column(Integer, ForeignKey("prioridades.id"))
    #concluida = Column(Boolean, default=False)  # 'v' no seu JSON TODO: MAPEAR
    categoria = relationship("CategoriaModel", back_populates="tarefas")