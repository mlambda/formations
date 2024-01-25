from fastapi import FastAPI
from pydantic import BaseModel

from .mylib import load_model

app = FastAPI()

class MyData(BaseModel):
    x: int
    y: int

model = load_model(...)  # Code de chargement du modèle

@app.post("/")
async def main(my_data: MyData):
    output = model.predict(my_data)
    return {"output": output}
