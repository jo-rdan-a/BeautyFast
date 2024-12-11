# BeautyFast
BeautyFast

**Esta API foi construída como uma prática para entender melhor o desenvolvimento de APIs RESTful utilizando FastAPI, uma ferramenta moderna e de alto desempenho para criação de APIs com Python.

---
### Aluna: *Jordana dos Reis Machado*
### Disciplina: *Arquitetura de Sistemas*
### Professor: *Gabriel Tavares*

---

## Endpoints 🌐

### 1. **Listar produtos** 📋
**GET** `/produtos`
**Responsta:**
```json
  {
  "status": "success",
  "message": "Produtos listados com sucesso.",
  "data": []
}
```

### 2. Listar produtor por Id
**GET** `/protudos/{produto_id}`
**Responsta:**
```json
  {
    "status": "success",
    "message": "Produto encontrado.",
    "data": [
      {
        "id": 4,
        "nome": "Esmalte",
        "marca": "Boa",
        "preco": 15
      }
    ]
  } 
```

### 3. Cadastrar produto
**POST** `/produtos`
**Responsta:**
```json
  {
    "status": "success",
    "message": "Produto cadastrado.",
    "data": [
      {
        "id": 4,
        "nome": "Esmalte",
        "marca": "Boa",
        "preco": 15
      }
    ]
  }
```

### 4. Atualizar Produto
**PUT** `/produtos/{produto_id}`
**Responsta:**
```json
  {
    "status": "success",
    "message": "Produto atualizado com sucesso.",
    "data": [
      {
        "id": 1,
        "nome": "Batom",
        "marca": "Myu",
        "preco": 50
      }
    ]
  }
```

### 5. Deletar produto
**DELETE** `/produtoss/{produto_id}`
**Responsta:**
```json
  {
    "status": "success",
    "message": "Produto atualizado com sucesso.",
    "data": [
      {
        "id": 1,
        "nome": "Batom",
        "marca": "Myu",
        "preco": 50
      }
    ]
  }
```

## Como Executar 🚀

### Pré-requisitos

Antes de rodar o projeto, é necessário ter os seguintes pré-requisitos:

- 🐍 **Python 3.9** ou superior instalado.
- 📦 Instalar as dependências do projeto.

### Passos

1. **Clone o repositório**:
   Se você ainda não tem o projeto, clone-o para sua máquina local com o seguinte comando:
   ```bash
   git clone https://github.com/jo-rdan-a/BeautyFast.git
   cd nome-do-repositorio
   ```
  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

4. Open your browser and navigate to:
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📄
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 📚

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
