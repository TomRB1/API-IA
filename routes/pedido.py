# app/routes/pedido.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from utils.db import get_cursor
from managers.pedido_manager import PedidoManager
from models.pedido_model import Pedido, PedidoCreate

router = APIRouter(prefix="/pedidos", tags=["pedidos"])
manager = PedidoManager()

@router.get("/", response_model=List[Pedido])
def list_pedidos(cursor=Depends(get_cursor)):
    return manager.get_all(cursor)

@router.get("/{pedido_id}", response_model=Pedido)
def get_pedido(pedido_id: int, cursor=Depends(get_cursor)):
    row = manager.get_by_id(pedido_id, cursor)
    if not row:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return row

@router.post("/agregar", response_model=Pedido)
def create_pedido(pedido: PedidoCreate, cursor=Depends(get_cursor)):
    return manager.create(pedido.dict(), cursor)

@router.put("/{pedido_id}", response_model=Pedido)
def update_pedido(pedido_id: int, pedido: PedidoCreate, cursor=Depends(get_cursor)):
    return manager.update(pedido_id, pedido.dict(), cursor)

@router.delete("/{pedido_id}")
def delete_pedido(pedido_id: int, cursor=Depends(get_cursor)):
    return manager.delete(pedido_id, cursor)
