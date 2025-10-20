let guardar = document.getElementById("guardar")
let estadisticas = document.getElementById("estadisticas")

guardar.addEventListener("click", (event) => {
    event.preventDefault()
    const nombre = document.getElementById("nombre").value
    const ampliada = document.getElementById("ampliada").value
    const altura = document.getElementById("altura").value

    if (nombre == "" || ampliada == "" || altura == "") {

    }
    else {
        fetch(`http://127.0.0.1:8000/partida/${ampliada}/${altura}/${nombre}`)
            .then(response => response.json())
            .then(data => {
                const partidaID = data.id

                fetch(`http://127.0.0.1:8000/barcos/${partidaID}`)
                    .then(res => res.json())
                    .then(data => {
                        crearTabla(data.matriz)
                    })
                tablero.addEventListener("click", event => {
                    const celda = event.target;
                    if (celda.tagName !== "TD") return

                    const x = celda.getAttribute("data-x")
                    const y = celda.getAttribute("data-y")

                    fetch(`http://127.0.0.1:8000/tocados/${partidaID}/${x}/${y}`)
                        .then(res => res.json())
                        .then(data => {
                            celda.classList.remove("oculto")
                            celda.setAttribute("class", celda.className + " desactivada")

                            if (data.resultado === "Agua") {
                                celda.setAttribute("class", "agua")
                                celda.textContent = "O"
                            } else if (data.resultado === "impacto") {
                                celda.setAttribute("class", "impacto")
                                celda.textContent = "X"
                            }
                        })
                        .catch(err => {
                            console.error("Error al disparar:", err)
                        });
                })
            })
    }

})

estadisticas.addEventListener("click", (event) => {
    event.preventDefault();
    fetch("http://127.0.0.1:8000/estadisticas")
        .then(response => response.json())
        .then(data => {
            console.table(data);
        })
        .catch(error => console.error('Error:', error))
})

function crearTabla(matriz) {
    const tablero = document.querySelector("#tablero tbody")
    tablero.innerHTML = ""

    for (let i = 0; i < matriz.length; i++) {
        const fila = document.createElement("tr")

        for (let j = 0; j < matriz[i].length; j++) {
            const celda = document.createElement("td")
            celda.textContent = matriz[i][j]

            celda.setAttribute("data-x", i)
            celda.setAttribute("data-y", j)
            celda.setAttribute("data-valor", matriz[i][j])
            celda.setAttribute("class", "oculto")
            celda.textContent = ""
            fila.appendChild(celda)
        }

        tablero.appendChild(fila)
    }
}
