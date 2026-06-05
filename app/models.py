from pydantic import BaseModel

class Miembro(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str

class Membresia(BaseModel):
    id: int
    tipo: str
    precio: float

class Clase(BaseModel):
    id: int
    nombre: str
    horario: str

class Rutina(BaseModel):
    id: int
    descripcion: str
    duracion: int

class Pago(BaseModel):
    id: int
    miembro_id: int
    monto: float
    fecha: str
