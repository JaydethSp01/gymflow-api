from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import miembros, membresias, clases, rutinas, pagos
import os

app = FastAPI()

origins = os.environ.get("CORS_ORIGINS", "*").split(",")
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(miembros.router)
app.include_router(membresias.router)
app.include_router(clases.router)
app.include_router(rutinas.router)
app.include_router(pagos.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
