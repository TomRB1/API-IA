# app/routes/marca.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from utils.db import get_cursor
from managers.marca_manager import MarcaManager
from models.marca_model import Marca, MarcaCreate

router = APIRouter(prefix="/marcas", tags=["marcas"])
manager = MarcaManager()

@router.get("/", response_model=List[Marca])
def list_marcas(cursor=Depends(get_cursor)):
    return manager.get_all(cursor)

@router.get("/{marca_id}", response_model=Marca)
def get_marca(marca_id: int, cursor=Depends(get_cursor)):
    row = manager.get_by_id(marca_id, cursor)
    if not row:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return row

@router.post("/agregar", response_model=Marca)
def create_marca(marca: MarcaCreate, cursor=Depends(get_cursor)):
    return manager.create(marca.dict(), cursor)

@router.put("/{marca_id}", response_model=Marca)
def update_marca(marca_id: int, marca: MarcaCreate, cursor=Depends(get_cursor)):
    return manager.update(marca_id, marca.dict(), cursor)

@router.delete("/{marca_id}")
def delete_marca(marca_id: int, cursor=Depends(get_cursor)):
    return manager.delete(marca_id, cursor)
