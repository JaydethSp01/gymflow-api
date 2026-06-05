from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Clase(BaseModel):
    id: int
    nombre: str
    instructor: str

clases_db = [
    Clase(id=1, nombre="Yoga", instructor="Ana Lopez"),
    Clase(id=2, nombre="Spinning", instructor="Carlos Diaz"),
]

@router.get("/clases", response_model=List[Clase])
async def get_clases():
    return clases_db

@router.get("/clases/{clase_id}", response_model=Clase)
async def get_clase(clase_id: int):
    clase = next((c for c in clases_db if c.id == clase_id), None)
    if clase is None:
        raise HTTPException(status_code=404, detail="Clase not found")
    return clase

@router.post("/clases", response_model=Clase)
async def create_clase(clase: Clase):
    clases_db.append(clase)
    return clase

@router.put("/clases/{clase_id}", response_model=Clase)
async def update_clase(clase_id: int, clase: Clase):
    index = next((i for i, c in enumerate(clases_db) if c.id == clase_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Clase not found")
    clases_db[index] = clase
    return clase

@router.delete("/clases/{clase_id}")
async def delete_clase(clase_id: int):
    index = next((i for i, c in enumerate(clases_db) if c.id == clase_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Clase not found")
    del clases_db[index]
    return {"detail": "Clase deleted"}