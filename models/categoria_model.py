# app/models/categoria_model.py
from pydantic import BaseModel

class Categoria(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None

class CategoriaCreate(BaseModel):
    nombre: str
    descripcion: str | None = None
