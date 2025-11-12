# app/models/pedido_model.py
from pydantic import BaseModel
from datetime import date

class Pedido(BaseModel):
    id: int
    id_cliente: int
    id_componente: int
    cantidad: int
    precio_unitario: float
    fecha: date
    total: float
    cliente_nombre: str | None = None
    componente_nombre: str | None = None

class PedidoCreate(BaseModel):
    id_cliente: int
    id_componente: int
    cantidad: int = 1
    precio_unitario: float
