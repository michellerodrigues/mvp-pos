from pydantic import BaseModel

class MembroFamiliaBase(BaseModel):
    nome: str
    email: str
    telefone: str
    tipo: str

class MembroFamiliaCreate(MembroFamiliaBase):
    pass

class MembroFamilia(MembroFamiliaBase):
    id: int

    class Config:
        orm_mode = True