# app/models/cliente_model.py
from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nombre: str
    apellido: str | None = None
    telefono: str | None = None
    email: str | None = None

class ClienteCreate(BaseModel):
    nombre: str
    apellido: str | None = None
    telefono: str | None = None
    email: str | None = None
