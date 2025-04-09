# schemas/converters.py
import json
from models import OpcaoModel, PerguntaModel

class OpcaoConverter:
    @staticmethod
    def to_schema(opcao: OpcaoModel, questionario_id: int) -> dict:
        return {
            "texto": opcao.texto,
            "tags": json.loads(opcao.tags),
            "selecionada": any(
                r.questionario_id == questionario_id
                for r in opcao.respostas
            )
        }

class PerguntaConverter:
    @staticmethod
    def to_schema(pergunta: PerguntaModel, questionario_id: int) -> dict:
        return {
            "texto": pergunta.texto,
            "tipo": pergunta.tipo,
            "opcoes": [
                OpcaoConverter.to_schema(opcao, questionario_id)
                for opcao in pergunta.opcoes
            ]
        }