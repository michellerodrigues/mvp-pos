from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.categorias import router as categorias_router
from routers.usuario import router as usuario_router


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8005"],  # Ou "*" para permitir todas
    allow_credentials=True,
    allow_methods=["*"],  # Ou ["GET", "POST", ...]
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(categorias_router, prefix="/api")
app.include_router(usuario_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Gerenciamento de Tarefas!"}


