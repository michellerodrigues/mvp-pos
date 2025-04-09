from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Session
from datetime import datetime
from database.database import SessionLocal
from models.usuario import UsuarioModel
from schemas.usuario import Usuario, UsuarioCreate, UsuarioLogin
from security.security import criar_hash_senha, verificar_senha
from schemas.questionario import PerguntaSchema, QuestionarioResponse
from services.questionario import get_db_questionario_by_user

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if db.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    hash_senha = criar_hash_senha(usuario.senha)
    
    db_usuario = UsuarioModel(
        nome=usuario.nome,
        email=usuario.email,
        hash_senha=hash_senha
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    
    return db_usuario

# TODO:  padronizar nome objetos (schemas, models, etc. ver plural x singular (bancp, classe e nome arquivo, pep8)
# TODO:  colocar bearer token na próxima sprint
@router.post("/login")
def login(dados_login: UsuarioLogin,  db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.email == dados_login.email).first()
    
    if not usuario or not verificar_senha(dados_login.senha, usuario.hash_senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos"
        )
    
    # Atualiza último acesso
    usuario.data_ultimo_acesso = datetime.now()
    db.commit()

    return dados_login


@router.get("/{email}/questionario", response_model=QuestionarioResponse) #Trocar para response
def get_questionarios_por_email(email: str, db: Session = Depends(get_db)):
    questionarioUsuario = get_db_questionario_by_user(email, db)
        
    if questionarioUsuario is None:
        raise HTTPException(status_code=400, detail="Questionario não respondido")
    
    return {"perguntas": questionarioUsuario}