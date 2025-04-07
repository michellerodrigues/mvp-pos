from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from models.categoria import CategoriaModel
from schemas.categoria import CategoriaCreate  as CategoriaCreateSchema
from schemas.categoria import Categoria as CategoriaSchema
from database.database import SessionLocal
from typing import List,Dict, Any


router = APIRouter()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categorias/", response_model=CategoriaSchema)
def criar_categoria(categoria: CategoriaCreateSchema, db: Session = Depends(get_db)):
    db_categoria = CategoriaModel(nome=categoria.nome)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.get("/categorias/", response_model=List[CategoriaSchema])
def listar_categorias(db: Session = Depends(get_db)):
    db_categoria = db.query(CategoriaModel).all()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return db_categoria

@router.get("/categorias/{categoria_id}", response_model=CategoriaSchema)
def ler_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = db.query(CategoriaModel).filter(CategoriaModel.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return db_categoria


from typing import List, Dict, Any
from fastapi.encoders import jsonable_encoder

@router.get("/categoriasx/")
def listar_categorias(db: Session = Depends(get_db)):
    categorias = db.query(CategoriaModel).options(
        joinedload(CategoriaModel.tarefas)
    ).all()
    
    if not categorias:
        raise HTTPException(status_code=404, detail="Nenhuma categoria encontrada")
    
    response = []
    for categoria in categorias:
        categoria_dict = {
            "categoria": categoria.nome,
            "tarefas": [
                {
                    "id": tarefa.id,
                    "nome": tarefa.nome,
                    "v": tarefa.concluida
                } for tarefa in categoria.tarefas
            ]
        }
        response.append(categoria_dict)
    
    return response

@router.get("/categorias/", response_model=List[CategoriaSchema])
def listar_categorias(db: Session = Depends(get_db)):
    # Carrega categorias com suas tarefas em uma única consulta
    categorias = db.query(CategoriaModel).options(
        joinedload(CategoriaModel.tarefas)
    ).all()
    
    if not categorias:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma categoria encontrada"
        )
    
    return categorias