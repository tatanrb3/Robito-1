console.log(document.getElementById('btnEnviar'))

document.getElementById('btnEnviar').addEventListener('click', function (e) {
    e.preventDefault();

    var input = document.getElementById('forgetAnswer').value
    var answer = document.getElementById('answer-bot')

    fetch(`/get-info/${input}/`) // Ruta de la vista Django
    .then(response => response.json())
    .then(data => {
        answer.innerHTML = data["mensaje"];
        console.log(data); // Maneja la respuesta de la vista Django aquí
    })
    .catch(error => {
        console.error('Error:', error);
    });
});