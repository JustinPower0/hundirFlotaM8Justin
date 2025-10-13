from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import random
# Funciones Normales

def crearMatriz(dim):
    matriz = []
    for i in range(dim):
        fila = []
        for j in range(dim):
            fila.append(0)
        matriz.append(fila)
    return matriz

def agregarMatrizPartida(partida, dim, contador):
    matriz = crearMatriz(dim)
    partida[contador] = matriz
    return contador + 1, matriz

def agregarbarcos(partida, partida_id):
    matriz = partida.get(partida_id)
    if matriz is None:
        return {"error": "Partida no encontrada"}

    dim = len(matriz)
    barcos = {}
    nombres = {
        1: "submari",
        2: "destructor",
        3: "creuer",
        4: "cuirassat",
        5: "portaavions"
    }

    barcos_lista = [
        [1],             # submari
        [2, 2],          # destructor
        [3, 3, 3],       # creuer
        [4, 4, 4, 4],    # cuirassat
        [5, 5, 5, 5, 5]  # portaavions
    ]

    for barco in barcos_lista:
        tipo = barco[0]
        nombre = nombres[tipo]
        longitud = len(barco)
        colocado = False

        while not colocado:
            orientacion = random.choice(["horizontal", "vertical"])
            if orientacion == "horizontal":
                fila = random.randint(0, dim - 1)
                col = random.randint(0, dim - longitud)
                posiciones = [(fila, col + i) for i in range(longitud)]
            else:
                fila = random.randint(0, dim - longitud)
                col = random.randint(0, dim - 1)
                posiciones = [(fila + i, col) for i in range(longitud)]

            # Verificar que no hay solapamientos
            if all(matriz[x][y] == 0 for x, y in posiciones):
                for x, y in posiciones:
                    matriz[x][y] = tipo
                barcos[nombre] = posiciones
                colocado = True

    return {"matriz": matriz, "barcos": barcos}

# Variable
partida = {}
matriz = []
contador = 1

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