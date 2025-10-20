let tabla = document.getElementById("tablero");
let guardar = document.getElementById("guardar");
let estadisticas = document.getElementById("estadisticas");
let estado_juego = document.getElementById("estado_juego");


const puntuacion_Base = 1000;
const disparar = 10;
const bonus_tocar = 20;
const bonus_Hundir_Barco = 50;
const penalizacion_Segundo = 1;


tabla.addEventListener("click", (event) => {
    event.preventDefault();
    let dimencion = parseInt(prompt("Introduzca una dimencion max 7"))
    fetch("http://127.0.0.1:8000/barcos/" + dimencion)
        .then(response => response.json())
        .then(data => {
            console.table(data);
        })
        .catch(error => console.error('Error:', error));
    // if (isNaN(dimencion) || dimencion < 7 || dimencion > 20) {
    //     alert("Introduce una dimencion entre 20 y 7")
    // } else {
    // }
})

estadisticas.addEventListener("click", (event) => {
    event.preventDefault();
    fetch("http://127.0.0.1:8000/estadisticas")
        .then(response => response.json())                 //fetch para tener las estadisticas
        .then(data => {
            console.table(data);
        })
        .catch(error => console.error('Error:', error));
})


document.addEventListener("DOMContentLoaded", () => {
    fetch("http://127.0.0.1:8000/estado_juego")
        .then(response => response.json())
        .then(data => {
            console.table(data);
        })
        .catch(error => console.error('Error:', error));
});



function crearTabla(matriz) {
    const tbody = document.getElementById("#tablero tbody");
    tbody.innerHTML = "";
    let celdas = ""
    let dimX = 6, dimY = 5;

    for (let i = 0; i < matriz.length; i++) {
        const fila = document.createElement("tr");
        for (let j = 0; j < matriz[i].length; j++) {
            const celda = document.createElement("td");
            celda.setAttribute(i);
            celda.setAttribute(j);
            fila.appendChild(celda);
        }
        tbody.appendChild(fila);
    }
    document.getElementById("tablero").innerHTML = celdas;
}


function calcularPuntuacio(joc) {

    let puntuacio = puntuacion_Base;

    puntuacio -= joc.disparos * disparar;

    // Bonus por tocar casella
    puntuacio += joc.casillasTocadas * bonus_tocar;

    // Bonus por hundir Barco
    puntuacio += joc.vaixellsEnfonsats * bonus_Hundir_Barco;

    // Penalización por tiempo 
    puntuacio -= joc.segons * penalizacion_Segundo;

    // Si abandonó
    if (joc.abandonat) {
        puntuacio = 0; // regla estricta
    }

    return puntuacio;
}

