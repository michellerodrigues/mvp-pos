from fastapi import HTTPException
from models.questionario import OpcaoModel, PerguntaModel, QuestionarioModel, RespostaModel
from models.usuario import UsuarioModel
from sqlalchemy.future import select
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from schemas.converters import PerguntaConverter


def get_db_questionario_by_user(email: str, db: Session):

    usuario = db.execute(
        select(UsuarioModel).where(UsuarioModel.email == email)
    )
    usuario = usuario.scalars().first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    questionario = db.execute(
        select(QuestionarioModel)
        .where(QuestionarioModel.usuario_id == usuario.id)
        .order_by(QuestionarioModel.data_criacao.desc())
        .limit(1)
    )
    questionario = questionario.scalars().first()
    
    if not questionario:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    
    perguntas = db.execute(
        select(PerguntaModel)
        .options(selectinload(PerguntaModel.opcoes).selectinload(OpcaoModel.respostas))
    )
    perguntas = perguntas.scalars().all()
    

    return [
        PerguntaConverter.to_schema(pergunta,questionario.id)
        for pergunta in perguntas
    ]