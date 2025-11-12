# app/models/marca_model.py
from pydantic import BaseModel

class Marca(BaseModel):
    id: int
    nombre: str
    pais_origen: str | None = None

class MarcaCreate(BaseModel):
    nombre: str
    pais_origen: str | None = None
