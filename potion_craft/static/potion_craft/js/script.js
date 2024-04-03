

document.addEventListener('DOMContentLoaded', function(){
    const clase_dd = document.querySelector('#id_clase');
    const portrait = document.querySelector('#retrato');
    
    // Función para construir la ruta de la imagen en función del valor seleccionado en el dropdown
    function construirRutaImagen(clase) {
        return `/static/potion_craft/img/portraits/${clase.toLowerCase()}/sample.png`;
    }
    
    portrait.src = construirRutaImagen(clase_dd.value);
    portrait.alt = clase_dd.value;
    
    // Agregar un evento change al dropdown
    clase_dd.addEventListener('change', function(){
       
        let claseSeleccionada = this.value;
        let rutaImagen = construirRutaImagen(claseSeleccionada);
        portrait.src = rutaImagen;
        portrait.alt = claseSeleccionada;
        console.log(rutaImagen);
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
