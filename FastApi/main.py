from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# Crear la aplicación
app = FastAPI(title="Mi Projecto", version="0.0.1")

partida = []

# Lista de orígenes permitidos
origins = [
    "http://localhost:5500",  # si tu frontend corre aquí
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],  # permite cualquier origen (no recomendable en producción)
    allow_origins=origins,  # permite solo esos orígenes
    allow_credentials=True,
    allow_methods=["*"],    # permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],    # permite todas las cabeceras
)

# Funciones
@app.get("/")
def read_root():
    return {"mensaje": "Hola alumnos!"}

@app.get("/saludo/{nombre}")
def read_item(nombre: str):
    return {"saludo": f"Hola {nombre}!"}
