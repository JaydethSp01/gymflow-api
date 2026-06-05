from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Miembro(BaseModel):
    id: int
    nombre: str
    email: str

miembros_db = [
    Miembro(id=1, nombre="Juan Perez", email="juan.perez@example.com"),
    Miembro(id=2, nombre="Maria Gomez", email="maria.gomez@example.com"),
]

@router.get("/miembros", response_model=List[Miembro])
async def get_miembros():
    return miembros_db

@router.get("/miembros/{miembro_id}", response_model=Miembro)
async def get_miembro(miembro_id: int):
    miembro = next((m for m in miembros_db if m.id == miembro_id), None)
    if miembro is None:
        raise HTTPException(status_code=404, detail="Miembro not found")
    return miembro

@router.post("/miembros", response_model=Miembro)
async def create_miembro(miembro: Miembro):
    miembros_db.append(miembro)
    return miembro

@router.put("/miembros/{miembro_id}", response_model=Miembro)
async def update_miembro(miembro_id: int, miembro: Miembro):
    index = next((i for i, m in enumerate(miembros_db) if m.id == miembro_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Miembro not found")
    miembros_db[index] = miembro
    return miembro

@router.delete("/miembros/{miembro_id}")
async def delete_miembro(miembro_id: int):
    index = next((i for i, m in enumerate(miembros_db) if m.id == miembro_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Miembro not found")
    del miembros_db[index]
    return {"detail": "Miembro deleted"}