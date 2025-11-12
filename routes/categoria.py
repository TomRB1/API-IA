# app/routes/categoria.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from utils.db import get_cursor
from managers.categoria_manager import CategoriaManager
from models.categoria_model import Categoria, CategoriaCreate

router = APIRouter(prefix="/categorias", tags=["categorias"])
manager = CategoriaManager()

@router.get("/", response_model=List[Categoria])
def list_cats(cursor=Depends(get_cursor)):
    return manager.get_all(cursor)

@router.get("/{cat_id}", response_model=Categoria)
def get_cat(cat_id: int, cursor=Depends(get_cursor)):
    row = manager.get_by_id(cat_id, cursor)
    if not row:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return row

@router.post("/agregar", response_model=Categoria)
def create_cat(cat: CategoriaCreate, cursor=Depends(get_cursor)):
    return manager.create(cat.dict(), cursor)

@router.put("/{cat_id}", response_model=Categoria)
def update_cat(cat_id: int, cat: CategoriaCreate, cursor=Depends(get_cursor)):
    return manager.update(cat_id, cat.dict(), cursor)

@router.delete("/{cat_id}")
def delete_cat(cat_id: int, cursor=Depends(get_cursor)):
    return manager.delete(cat_id, cursor)
