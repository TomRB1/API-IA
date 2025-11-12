# app/routes/componente.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from utils.db import get_cursor
from managers.componente_manager import ComponenteManager
from models.componente_model import Componente, ComponenteCreate

router = APIRouter(prefix="/componentes", tags=["componentes"])
manager = ComponenteManager()

@router.get("/", response_model=List[Componente])
def list_components(cursor=Depends(get_cursor)):
    return manager.get_all(cursor)

@router.get("/{comp_id}", response_model=Componente)
def get_component(comp_id: int, cursor=Depends(get_cursor)):
    row = manager.get_by_id(comp_id, cursor)
    if not row:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    return row

@router.post("/agregar", response_model=Componente)
def create_component(comp: ComponenteCreate, cursor=Depends(get_cursor)):
    return manager.create(comp.dict(), cursor)

@router.put("/{comp_id}", response_model=Componente)
def update_component(comp_id: int, comp: ComponenteCreate, cursor=Depends(get_cursor)):
    return manager.update(comp_id, comp.dict(), cursor)

@router.delete("/{comp_id}")
def delete_component(comp_id: int, cursor=Depends(get_cursor)):
    return manager.delete(comp_id, cursor)
