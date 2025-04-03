from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.categoria import Categoria
from schemas.categoria import CategoriaCreate, Categoria
from models import Session

router = APIRouter()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@router.post("/categorias/", response_model=Categoria)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = Categoria(nome=categoria.nome)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.get("/categorias/{categoria_id}", response_model=Categoria)
def ler_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return db_categoria