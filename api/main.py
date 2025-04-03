from fastapi import FastAPI
from categorias import router as categorias_router
#from api.tarefas import router as tarefas_router

app = FastAPI()

# Registrar rotas
app.include_router(categorias_router, prefix="/api")
#app.include_router(tarefas_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Gerenciamento de Tarefas!"}
