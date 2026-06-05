from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Pago(BaseModel):
    id: int
    miembro: str
    monto: float
    fecha: str

pagos_db = [
    Pago(id=1, miembro="Juan Perez", monto=30.0, fecha="2023-10-01"),
    Pago(id=2, miembro="Maria Gomez", monto=300.0, fecha="2023-10-02"),
]

@router.get("/pagos", response_model=List[Pago])
async def get_pagos():
    return pagos_db

@router.get("/pagos/{pago_id}", response_model=Pago)
async def get_pago(pago_id: int):
    pago = next((p for p in pagos_db if p.id == pago_id), None)
    if pago is None:
        raise HTTPException(status_code=404, detail="Pago not found")
    return pago

@router.post("/pagos", response_model=Pago)
async def create_pago(pago: Pago):
    pagos_db.append(pago)
    return pago

@router.put("/pagos/{pago_id}", response_model=Pago)
async def update_pago(pago_id: int, pago: Pago):
    index = next((i for i, p in enumerate(pagos_db) if p.id == pago_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Pago not found")
    pagos_db[index] = pago
    return pago

@router.delete("/pagos/{pago_id}")
async def delete_pago(pago_id: int):
    index = next((i for i, p in enumerate(pagos_db) if p.id == pago_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Pago not found")
    del pagos_db[index]
    return {"detail": "Pago deleted"}