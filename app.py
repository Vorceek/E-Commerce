from fastapi import FastAPI

app = FastAPI(title="Minha API")

@app.get("/")
def raiz():
    return {"msg": "Olá, FastAPI!"}
