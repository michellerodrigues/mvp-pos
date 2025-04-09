import json
from pydantic import BaseModel, field_validator
from typing import List
from .base import OpcaoBase, PerguntaBase

class OpcaoSchema(OpcaoBase):
    selecionada: bool

class PerguntaSchema(PerguntaBase):
    opcoes: List[OpcaoSchema]

    @field_validator('opcoes')
    def validar_opcoes_radio(cls, v, values):
        if values.data.get('tipo') == 'radio':
            selecionadas = sum(1 for opcao in v if opcao.selecionada)
            if selecionadas > 1:
                raise ValueError("Perguntas 'radio' devem ter no máximo uma opção selecionada")
        return v

class QuestionarioResponse(BaseModel):
    perguntas: List[PerguntaSchema]


    
OpcaoSchema.model_rebuild()
QuestionarioResponse.model_rebuild()
PerguntaSchema.model_rebuild()