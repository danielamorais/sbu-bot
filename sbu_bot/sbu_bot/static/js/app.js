//TODO: Enviar request se email valido
function validarEmail() {
    var email = document.getElementById("email").value;
    var div = document.getElementById("erroEmail");
    console.log("O email eh " + email);
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    regex.test(email) ? console.log("ok") : div.style.display = "block";
}

function esconderDiv() {
    var div = document.getElementById("erroEmail");
    div.style.display = "none";
}