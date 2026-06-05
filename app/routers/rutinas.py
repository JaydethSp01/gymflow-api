from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Rutina(BaseModel):
    id: int
    nombre: str
    descripcion: str

rutinas_db = [
    Rutina(id=1, nombre="Rutina de Fuerza", descripcion="Entrenamiento de fuerza para todo el cuerpo"),
    Rutina(id=2, nombre="Rutina de Cardio", descripcion="Ejercicios de cardio para mejorar la resistencia"),
]

@router.get("/rutinas", response_model=List[Rutina])
async def get_rutinas():
    return rutinas_db

@router.get("/rutinas/{rutina_id}", response_model=Rutina)
async def get_rutina(rutina_id: int):
    rutina = next((r for r in rutinas_db if r.id == rutina_id), None)
    if rutina is None:
        raise HTTPException(status_code=404, detail="Rutina not found")
    return rutina

@router.post("/rutinas", response_model=Rutina)
async def create_rutina(rutina: Rutina):
    rutinas_db.append(rutina)
    return rutina

@router.put("/rutinas/{rutina_id}", response_model=Rutina)
async def update_rutina(rutina_id: int, rutina: Rutina):
    index = next((i for i, r in enumerate(rutinas_db) if r.id == rutina_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Rutina not found")
    rutinas_db[index] = rutina
    return rutina

@router.delete("/rutinas/{rutina_id}")
async def delete_rutina(rutina_id: int):
    index = next((i for i, r in enumerate(rutinas_db) if r.id == rutina_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Rutina not found")
    del rutinas_db[index]
    return {"detail": "Rutina deleted"}