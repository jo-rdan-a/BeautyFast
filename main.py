from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()


# Modelos
class ProdutoBeleza(BaseModel):
    id: int
    nome: str
    marca: str
    preco: float


# Resposta padrão
class ResponseModel(BaseModel):
    status: str
    message: str
    data: Any


# "Banco de dados" em memória
produtos: Dict[int, ProdutoBeleza] = {
    1: ProdutoBeleza(id=1, nome="Shampoo Hidratante", marca="L'Oréal", preco=35.50),
    2: ProdutoBeleza(
        id=2, nome="Condicionador Reparador", marca="Pantene", preco=28.90
    ),
    3: ProdutoBeleza(id=3, nome="Creme Anti-Idade", marca="Nivea", preco=45.00),
}

# Endpoints


# 1. Listar todos os produtos de beleza
@app.get("/produtos", response_model=ResponseModel)
async def listar_produtos():
    return ResponseModel(
        status="success",
        message="Produtos listados com sucesso.",
        data=list(produtos.values()),
    )


# 2. Adicionar um novo produto de beleza
@app.post("/produtos", response_model=ResponseModel)
async def criar_produto(produto: ProdutoBeleza):
    if produto.id in produtos:
        raise HTTPException(status_code=400, detail="Produto com este ID já existe.")

    produtos[produto.id] = produto
    return ResponseModel(
        status="success", message="Produto cadastrado.", data=[produto]
    )


# 3. Atualizar informações de um produto de beleza
@app.put("/produtos/{produto_id}", response_model=ResponseModel)
async def atualizar_produto(produto_id: int, produto: ProdutoBeleza):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    produtos[produto_id] = produto
    return ResponseModel(
        status="success", message="Produto atualizado com sucesso.", data=[produto]
    )


# 4. Deletar um produto de beleza
@app.delete("/produtos/{produto_id}", response_model=ResponseModel)
async def deletar_produto(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    produto = produtos.pop(produto_id)
    return ResponseModel(
        status="success", message="Produto deletado com sucesso.", data=[produto]
    )


# 5. Obter informações detalhadas de um produto de beleza
@app.get("/produtos/{produto_id}", response_model=ResponseModel)
async def obter_produto(produto_id: int):
    produto = produtos.get(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    return ResponseModel(
        status="success", message="Produto encontrado.", data=[produto]
    )
