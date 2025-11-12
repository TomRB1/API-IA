# app/routes/cliente.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from utils.db import get_cursor
from managers.cliente_manager import ClienteManager
from models.cliente_model import Cliente, ClienteCreate

router = APIRouter(prefix="/clientes", tags=["clientes"])
manager = ClienteManager()

@router.get("/", response_model=List[Cliente])
def list_clientes(cursor=Depends(get_cursor)):
    return manager.get_all(cursor)

@router.get("/{cliente_id}", response_model=Cliente)
def get_cliente(cliente_id: int, cursor=Depends(get_cursor)):
    row = manager.get_by_id(cliente_id, cursor)
    if not row:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return row

@router.post("/agregar", response_model=Cliente)
def create_cliente(cliente: ClienteCreate, cursor=Depends(get_cursor)):
    return manager.create(cliente.dict(), cursor)

@router.put("/{cliente_id}", response_model=Cliente)
def update_cliente(cliente_id: int, cliente: ClienteCreate, cursor=Depends(get_cursor)):
    return manager.update(cliente_id, cliente.dict(), cursor)

@router.delete("/{cliente_id}")
def delete_cliente(cliente_id: int, cursor=Depends(get_cursor)):
    return manager.delete(cliente_id, cursor)
