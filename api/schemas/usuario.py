from datetime import datetime
from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    data_ultimo_acesso: datetime | None
    
    class Config:
        orm_mode = True

class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str