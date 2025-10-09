let tabla = document.getElementById("tabla");
let validacion = true
tabla.addEventListener("click", (event) => {
    event.preventDefault();
    let dimencion = parseInt(prompt("Introduzca una dimencion max 7"))
    if (isNaN(dimencion) || dimencion < 7 || dimencion > 20) {
        alert("Introduce una dimencion entre 20 y 7")
        validacion = false
    } else {
        fetch("http://127.0.0.1:8000/matriz/" + dimencion)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                validacion = false
            })
            .catch(error => console.error('Error:', error));
    }
})
