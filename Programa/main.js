let tabla = document.getElementById("tabla");

tabla.addEventListener("click",(event) => {
    event.preventDefault();

    fetch("http://127.0.0.1:8000/matriz")
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error:', error));
})
