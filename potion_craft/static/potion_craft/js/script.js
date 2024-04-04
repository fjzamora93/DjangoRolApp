

document.addEventListener('DOMContentLoaded', function(){
    const clase_dd = document.querySelector('#id_clase');
    const raza_dd = document.querySelector('#id_raza');
    const genero_dd = document.querySelector('#id_genero');
    const avatar_dd = document.querySelector('#id_portrait');
    const portrait = document.querySelector('#retrato');

    function construirRutaImagen(clase, raza, genero, avatar) {
        let ruta = `/static/potion_craft/img/portraits/${raza}/${genero}-${raza}-${clase}-${avatar}.png`
        console.log(ruta)
        return ruta;
    }

    function actualizarImagen() {
        let claseSeleccionada = clase_dd.value;
        let razaSeleccionada = raza_dd.value;
        let generoSeleccionado = genero_dd.value;
        let avatarSeleccionado = avatar_dd.value;

        let rutaImagen = construirRutaImagen(claseSeleccionada, razaSeleccionada, generoSeleccionado, avatarSeleccionado);
        portrait.src = rutaImagen;
        portrait.alt = claseSeleccionada;
    }

    portrait.src = construirRutaImagen(clase_dd.value, raza_dd.value, genero_dd.value, avatar_dd.value);
    portrait.alt = clase_dd.value;

    const selectsCharCreator = document.querySelectorAll('#charcreator select');
    selectsCharCreator.forEach(select => {
        select.addEventListener('change', actualizarImagen);
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
