var arreglo = new Array();
var x = 0;

function grabar() {
    var nombre= document.getElementById('txtNombre').value;
    var apellido= document.getElementById('txtApellido').value;
    var email = document.getElementById('txtEmail').value;
    var usuario = document.getElementById('txtUsuario').value;
    var pass = document.getElementById('txtPass').value;
    var fono = document.getElementById('txtFono').value;
    var rut = document.getElementById('txtRut').value;
    reg = new registro();
    reg.setNombre(nombre);
    reg.setApellido(apellido);
    reg.setEmail(email);
    reg.setUsuario(usuario);
    reg.setPass(pass);
    reg.setFono(fono);
    reg.setRut(rut);
    alert(reg.imprimir());
    arreglo[x]=JSON.stringify(reg);
    x++;
    localStorage.setItem('registros',arreglo);
    alert('Registro Almacenado');
}
function listar() {
    var todo='<table border=1>';
    todo = todo + '<tr> <td>rut</td> <td>Nombre</td> <td>Apellido</td> <td>Email</td> </tr>';
    var datos = localStorage.getItem('registros');
    var arreglo_temp = new Array();
    datos = datos.split('},{').join('};{'); 
    arreglo_temp = datos.split(';');
    for (let index = 0; index < arreglo_temp.length; index++) {
        var registro = arreglo_temp[index];
        var reg = JSON.parse(registro);
        todo = todo + "<tr> <td>"+reg.rut+"</td> <td>"+reg.nombre+"</td> <td>"+reg.apellido+"</td> <td>"+reg.email+"</td> </tr>"
    }  
    todo = todo + "</table>";
    document.getElementById('listado').innerHTML= todo;
}