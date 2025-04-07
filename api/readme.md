Instale as dependências:

bash
Copy
pip install fastapi sqlalchemy pydantic uvicorn
Execute o servidor:

bash
Copy
uvicorn main:app --reload --port 8002
Acesse a API em:

Copy
http://127.0.0.1:8000