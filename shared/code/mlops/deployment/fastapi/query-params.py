from fastapi import FastAPI

from .mylib import load_model

app = FastAPI()

model = load_model(...)  # Code de chargement du modèle

@app.get("/")
async def main(value: int):
    output = model.predict(value)
    return {"output": output}
