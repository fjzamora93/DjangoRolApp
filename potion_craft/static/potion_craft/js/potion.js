//javascrpt par ael html de potion.js



document.addEventListener('DOMContentLoaded', function(){
    const esencia_1 = document.querySelector('#id_esencia_1');
    const esencia_2 = document.querySelector('#id_esencia_2');
    const alterCheck = document.querySelector('#id_alter');

    const img_esencia_1 = document.querySelector('#img-esencia-1')
    const img_esencia_2 = document.querySelector('#img-esencia-2')

   
    esencia_1.addEventListener('change', function() {
        console.log(`La opción ${esencia_1.value} ha sido seleccionada.`);
        img_esencia_1.src = `/static/potion_craft/img/ingr/esencia-${esencia_1.value}.png`;
    });

    esencia_2.addEventListener('change', function(){
        console.log(`La opción ${esencia_2.value} ha sido seleccionada.`);
        img_esencia_2.src = `/static/potion_craft/img/ingr/esencia-${esencia_2.value}.png`;
    })
    

    alterCheck.addEventListener('change', function() {
        console.log(alterCheck.value);
    });
});
