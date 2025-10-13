from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import random

# Variable
partida = {}
matriz = []
contador = 1
barcos_definicion = {
    "submari": {"id": 1, "longitud": 1},
    "destructor": {"id": 2, "longitud": 2},
    "creuer": {"id": 3, "longitud": 3},
    "cuirassat": {"id": 4, "longitud": 4},
    "portaavions": {"id": 5, "longitud": 5}
}


# Funciones Normales

# Funcion Crear Matriz
def crearMatriz(dim):
    matriz = []
    for i in range(dim):
        fila = []
        for j in range(dim):
            fila.append(0)
        matriz.append(fila)
    return matriz

# Funcion Agrergar Matriz Partida
def agregarMatrizPartida(partida, dim, contador):
    matriz = crearMatriz(dim)
    partida[contador] = matriz
    return contador + 1, matriz

# Funcion Agregar Barcos
def agregarbarcos(partida, partida_id):
    matriz = partida.get(partida_id)
    if matriz is None:
        return {"error": "Partida no encontrada"}

    dim = len(matriz)
    total_casillas = dim * dim
    limite_ocupacion = int(total_casillas * 0.3)

    barcos = {}
    estado = {"ocupadas": 0}

    def colocar_barco(nombre, info):
        tipo = info["id"]
        longitud = info["longitud"]
        intentos = 0
        continuar = False
        while intentos < 100:
            orientacion = random.choice(["horizontal", "vertical"])
            if orientacion == "horizontal":
                fila = random.randint(0, dim - 1)
                col = random.randint(0, dim - longitud)
                posiciones = [(fila, col + i) for i in range(longitud)]
            else:
                fila = random.randint(0, dim - longitud)
                col = random.randint(0, dim - 1)
                posiciones = [(fila + i, col) for i in range(longitud)]
            libre = True
            for x, y in posiciones:
                if matriz[x][y] != 0:
                    libre = False
                    break
            if libre:
                for x, y in posiciones:
                    matriz[x][y] = tipo
                barcos.setdefault(nombre, []).extend(posiciones)
                estado["ocupadas"] += longitud
                continuar = True
                break
            intentos += 1
        return continuar

    for nombre, info in barcos_definicion.items():
        colocado = colocar_barco(nombre, info)
        if not colocado:
            return {"error": f"No se pudo colocar el barco {nombre}"}

    while estado["ocupadas"] < limite_ocupacion:
        nombre, info = random.choice(list(barcos_definicion.items()))
        if estado["ocupadas"] + info["longitud"] > limite_ocupacion:
            break
        colocar_barco(nombre, info)

    return {"matriz": matriz, "barcos": barcos}

# Crear la aplicación
app = FastAPI(title="Mi Projecto", version="0.0.1")

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

# Funciones FastApi
@app.get("/partida/{dim}", tags=["Partida"])
def devolver_matriz(dim: int):
    global partida,contador
    contador, matriz = agregarMatrizPartida(partida, dim, contador)
    return {"id": contador - 1, "matriz": matriz}

@app.get("/barcos/{partida_id}", tags=["Barcos"])
def colocar_barcos(partida_id: int):
    resultado = agregarbarcos(partida, partida_id)
    return resultado