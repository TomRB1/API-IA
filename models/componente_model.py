# app/models/componente_model.py
from pydantic import BaseModel

class Componente(BaseModel):
    id: int
    nombre: str
    id_marca: int | None = None
    id_categoria: int | None = None
    precio: float
    stock: int
    descripcion: str | None = None
    marca_nombre: str | None = None    # optional extra in responses
    categoria_nombre: str | None = None

class ComponenteCreate(BaseModel):
    nombre: str
    id_marca: int | None = None
    id_categoria: int | None = None
    precio: float
    stock: int = 0
    descripcion: str | None = None
