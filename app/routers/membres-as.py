from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Membresia(BaseModel):
    id: int
    tipo: str
    precio: float

membresias_db = [
    Membresia(id=1, tipo="Mensual", precio=30.0),
    Membresia(id=2, tipo="Anual", precio=300.0),
]

@router.get("/membresias", response_model=List[Membresia])
async def get_membresias():
    return membresias_db

@router.get("/membresias/{membresia_id}", response_model=Membresia)
async def get_membresia(membresia_id: int):
    membresia = next((m for m in membresias_db if m.id == membresia_id), None)
    if membresia is None:
        raise HTTPException(status_code=404, detail="Membresia not found")
    return membresia

@router.post("/membresias", response_model=Membresia)
async def create_membresia(membresia: Membresia):
    membresias_db.append(membresia)
    return membresia

@router.put("/membresias/{membresia_id}", response_model=Membresia)
async def update_membresia(membresia_id: int, membresia: Membresia):
    index = next((i for i, m in enumerate(membresias_db) if m.id == membresia_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Membresia not found")
    membresias_db[index] = membresia
    return membresia

@router.delete("/membresias/{membresia_id}")
async def delete_membresia(membresia_id: int):
    index = next((i for i, m in enumerate(membresias_db) if m.id == membresia_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Membresia not found")
    del membresias_db[index]
    return {"detail": "Membresia deleted"}