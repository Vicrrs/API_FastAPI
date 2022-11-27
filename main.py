from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


produtos = [
    Produto(id=1, nome='NotebookGamer', preco=4800.00, em_oferta=False),
    Produto(id=2, nome='Xbox Series S', preco=3800.00, em_oferta=True),
    Produto(id=3, nome='Box Harry potter', preco=200.00, em_oferta=True),
    Produto(id=4, nome='Microfone Blue', preco=280.00, em_oferta=True),
    Produto(id=5, nome='Iphone 14', preco=8280.00, em_oferta=False)
]

app = FastAPI()


@app.get('/')
async def index():
    return {"Universo": "Vetorial"}


@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto

            return prod
    return None
