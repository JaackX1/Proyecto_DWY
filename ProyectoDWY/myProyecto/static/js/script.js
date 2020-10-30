/*
function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.length != 10) {
        alert("verifique el largo del rut");
        return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();

    if (dv != dv_usuario) {
        alert("|| Rut Incorrecto ||");
        return false;
    } else {
        return true;
    }
}*/


function validarNombre() {
    var nombre = document.getElementById("txtNombre").value;
    if (nombre.trim().length >= 3 && nombre.trim().length <= 80) {
        return true;
    }
    if (nombre.trim().length < 3) {
        alert("El Nombre no debe estar vacio y debe contener entre 3 y 80 caracteres");
        return false;
    }

}

function validarApellido() {
    var Apellido = document.getElementById("txtApellido").value;
    if (Apellido.trim().length >= 3 && Apellido.trim().length <= 80) {
        return true;
    }
    if (Apellido.trim().length < 3) {
        alert("El Apellido no debe estar vacio y debe contener entre 3 y 80 caracteres");
        return false;

    }
}

/*
function validaFecha() {
    var fechaFormulario = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();
    //////////////////////////////////////////////////
    var anno = fechaFormulario.slice(0, 4);
    var mes = fechaFormulario.slice(5, 7);
    var dia = fechaFormulario.slice(8, 10);
    //////////////////////////////////////////////////
    var fechaMia = new Date(anno, (mes - 1), dia); //0-+
    //////////////////////////////////////////////////
    if (fechaMia > fechaSistema) {
        alert("Fecha incorrecta");
        return false;
    } else {
        return true;
    }

}*/

function validarUsuario() {
    var nombre = document.getElementById("txtUsuario").value;
    if (nombre.trim().length >= 8) {
        return true;
    }
    if (nombre.trim().length < 8) {
        alert("Usuario debe contener como minimo 8 caracteres");
        return false;
    }
}




function validarPassword1() {
    var pass1 = document.getElementById("txtPass").value;
    if (pass1.length >= 8) {
        return true;
    }
    if (pass1.length < 8) {
        alert("Contraseña debe contener como minimo 8 caracteres");
        return false;
    }
}

function validarPassword2() {
    var pass2 = document.getElementById("txtPass2").value;
    if (pass2.length >= 8) {
        return true;
    }
    if (pass2.length < 8) {
        alert("Contraseña debe contener como minimo 8 caracteres");
        return false;
    }
}

function validarMismaPassword() {
    var pass1 = document.getElementById("txtPass").value;
    var pass2 = document.getElementById("txtPass2").value;
    if (pass2.length >= 8) {
        return true;
    }
    if (pass2.length < 8) {
        alert("Contraseña debe contener como minimo 8 caracteres");
        return false;
    }

    if (validarPassword1() == true) {
        if (validarPassword2() == true) {
            if (pass1 == pass2) {
                return true;
            }
            if (pass1 != pass2) {
                alert("Las contraseñas deben ser iguales");
                return false;
            }
        }
    }
}

function validar_email(email) {
    var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email) ? true : false;
}

function validarEmail() {
    var email = document.getElementById("txtCorreo").value;

    if (validar_email(email)) {
        return true;
    } else {
        alert("El email NO es correcto");
        return false;
    }

}





function Validaciones() {
    var resp = true;
    /*if (validarRut() == false) {
        resp = false;
    }*/
    if (validarNombre() == false) {
        resp = false;
    }
    if (validarApellido() == false) {
        resp = false;
    }
    if (validarEmail() == false) {
        resp = false;
    }
    /*
    if (validaFecha() == false) {
        resp = false;
    }*/
    if (validarUsuario() == false) {
        resp = false;
    }
    if (validarPassword1() == false) {
        resp = false;
    }
    if (validarPassword2() == false) {
        resp = false;
    }
    if (validarMismaPassword() == false) {
        resp = false;
    }



}




function validarPrecio() {
    var nom = document.getElementById("txtPrecio").value;
    if (nom >= 1) {
        return true;
    }
    if (nom < 1) {
        alert("Debe ingresar como mínimo 1 peso");
        return false;

    }
}

function validarDescripcion() {
    var nom = document.getElementById("txtDescripcion").value;
    if (nom.trim().length >= 3 && nom.trim().length <= 200) {
        return true;
    }

    if (nom.trim().length >= 1 && nom.trim().length <= 2 || nom.trim().length >= 201) {
        alert("La Descripcion debe contener como minimo 3 caracteres");
        return false;
    }
    if (nom.trim().length == 0) {
        return true;
    }
}

function validarNombreInsumo() {
    var nom = document.getElementById("txtInsumo").value;
    if (nom.trim().length >= 3) {
        return true;
    }
    if (nom.trim().length <= 2) {
        alert("Nombre de insumo debe contener como minimo 3 caracteres");
        return false;

    }
}



function ValidacionesInsumos() {
    var resp = true;

    if (validarNombreInsumo() == false) {
        resp = false;
    }
    if (validarPrecio() == false) {
        resp = false;
    }
    if (validarDescripcion() == false) {
        resp = false;
    }




}