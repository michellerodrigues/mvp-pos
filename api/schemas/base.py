from pydantic import BaseModel, field_validator
from typing import List, Literal

class OpcaoBase(BaseModel):
    texto: str
    tags: List[str]
    
    @field_validator('tags')
    def validar_tags(cls, v):
        if not all(tag.startswith('#') for tag in v):
            raise ValueError("Tags devem começar com '#'")
        return v

class PerguntaBase(BaseModel):
    texto: str
    tipo: Literal['radio', 'checkbox']