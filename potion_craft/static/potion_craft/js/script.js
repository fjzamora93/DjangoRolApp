
document.addEventListener('DOMContentLoaded', function(){
    const clase_dd = document.querySelector('#id_clase');
    const raza_dd = document.querySelector('#id_raza');
    const genero_dd = document.querySelector('#id_genero');
    const avatar_dd = document.querySelector('#id_portrait');
    const portrait = document.querySelector('#retrato');
    const portraitLeft = document.querySelector('#retrato-izquierda');
    const portraitRight = document.querySelector('#retrato-derecha');

    const botonAnterior = document.querySelector('.galeria button[value="-"]');
    const botonSiguiente = document.querySelector('.galeria button[value="+"]');


    function construirRutaImagen(clase, raza, genero, avatar) {
        let ruta_principal = `/static/potion_craft/img/portraits/${raza}/${genero}-${raza}-${clase}-${avatar}.png`
        var anterior = parseInt(avatar) - 1;
        var avatarAnterior = anterior.toString();
        var siguiente = parseInt(avatar) + 1;
        var avatarSiguiente = siguiente.toString();
        let ruta_anterior = `/static/potion_craft/img/portraits/${raza}/${genero}-${raza}-${clase}-${avatarAnterior}.png`
        let ruta_siguiente = `/static/potion_craft/img/portraits/${raza}/${genero}-${raza}-${clase}-${avatarSiguiente}.png`
        var rutas = [ruta_principal, ruta_anterior, ruta_siguiente]
        console.log(rutas)
        return rutas;
    }

    function actualizarImagen(boton = null) {
        var operador = boton.value;
        let claseSeleccionada = clase_dd.value;
        let razaSeleccionada = raza_dd.value;
        let generoSeleccionado = genero_dd.value;
        let avatarSeleccionado = avatar_dd.value;

        if (operador != null){
            if (operador === "+"){
                var intAvatar = parseInt(avatarSeleccionado) + 1;
            } else {
                var intAvatar = parseInt(avatarSeleccionado) - 1;
            }
            avatarSeleccionado = intAvatar.toString();
            avatar_dd.value = avatarSeleccionado
            console.log(avatarSeleccionado, avatar_dd.value)
            
        }
        
        let rutas = construirRutaImagen(claseSeleccionada, razaSeleccionada, generoSeleccionado, avatarSeleccionado);
        portrait.src = rutas[0];
        portraitLeft.src = rutas[1];
        portraitRight.src = rutas[2]
    }

    //portrait.src = construirRutaImagen(clase_dd.value, raza_dd.value, genero_dd.value, avatar_dd.value);


    const selectsCharCreator = document.querySelectorAll('#charcreator select');
    selectsCharCreator.forEach(select => {
        select.addEventListener('change', actualizarImagen);

    });

    // Asignar event listeners a los botones
    botonAnterior.addEventListener('click', function() {
        actualizarImagen(this);
    });

    botonSiguiente.addEventListener('click', function() {
        actualizarImagen(this);
    });

});














// //MINUTO 50

// function hello(){
//     //Esta es la forma de declarar variables, let, y constantes const
//     const heading = document.querySelector('#ejemplo')

//         //Este es el selector de propiedades de JavaScript
//     if (heading.innerHTML === '¡Adiós!'){
//         heading.innerHTML = "¡Hola!"
//     } else {
//         heading.innerHTML = "¡Adiós!"
//     }
// }

// let counter = 0;
// function count(){
//     counter ++;
//     alert(counter)
// }

// /*El EventListener tomará dos parámetros, primero el evento en sí mismo (cargar la página), 
// el segundo es la función que se ejecutará en el evento, que puede definirse justo ahí*/
// document.addEventListener('DOMContentLoaded', function(){
//     //Un selector puede referirse a una función
//     document.querySelector('#ejemploboton').onclick = hello;
//     document.querySelector('#ejemploformulario').onsubmit = function(){
//         const nombre = document.querySelector('#nombre').value;
//         alert(`Hola! ${nombre}`);
//     };
// });
