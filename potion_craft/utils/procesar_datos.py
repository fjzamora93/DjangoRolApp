import random
from ..models import *

"""
Esta función puede devolver dos cosas:
En caso de error, devuelve None
En caso de acierto, devuelve una tupla.
Creo que sería mejor que esta función simplemente actualizase la base de datos
para que en vez de devolver dos cosas, siempre devuelva la misma.
"""

def procesar_datos_ingredientes(ingr, color, proceso, herramienta):
    herramienta = int(herramienta)
    if proceso not in color:
        return None
    
    match herramienta:
        case 0:
            cantidad = 0
        case 1:
            cantidad = random.randint(0, 1)
        case 2:
            cantidad = 2
        case 3:
            cantidad = 3
        case 4:
            cantidad = random.randint(1, 3)

    tipo = random.choice(color.split("-"))
    match tipo:
        case "agua":
            tipo = "esencia acuosa"
        case "fuego":
            tipo = "esencia ígnea"
        case "aire":
            tipo = "esencia volátil"
        case "tierra":
            tipo = "esencia terrosa"
       
    esencia = tipo

    #TODO incorporar cantidad a la base de datos
    cantidad = cantidad
    return None if cantidad == 0  else esencia



def procesar_datos_pocion(base, alteracion, conocimiento, util, dado=int, esencias=list, personaje_actual=Personaje)->PersonajePotion:
    
    base = int(base)
    conocimiento = int(conocimiento)
    util = int(util)
    dado = int(dado)
    sum = dado + util + conocimiento + base
    if sum <= 11:
        return None
    
    efecto = 'Ingredientes no válidos!'
    if len(esencias) == 1:
        print("listado de 1 solo ingrediente", esencias, esencias[0])
        match esencias[0]:
            case "1":
                efecto = "Maná"
                if alteracion == 1:
                    efecto = "Eléctrica"
                if alteracion == 2:
                    efecto = "Inspiración"

            case "2":
                efecto = "Curativa"
                if alteracion == 1:
                    efecto = "Veneno"
                if alteracion == 2:
                    efecto = "Calma"
            case "3":
                efecto = "Piel de Piedra"
                if alteracion == 1:
                    efecto = "Petrificación"
                if alteracion == 2:
                    efecto = "Concentración"
            case "4":
                efecto = "Fuerza"
                if alteracion == 1:
                    efecto = "Explosiva"
                if alteracion == 2:
                    efecto = "Furia"
    
    if len(esencias) == 2:
        print("listado de 2 ingredientes", esencias, esencias[1])
        match esencias[1]:
            case "2":
                if esencias[0] == 1:
                    efecto = "Suerte Líquida"
                    if alteracion == 1:
                        efecto = "Aturdimiento"
                    if alteracion == 2:
                        efecto = "Locura"

            case "3":
                if esencias[0] == 2:
                    efecto = "Falsa Vida"
                    if alteracion == 1:
                        efecto = "Congelación"
                    if alteracion == 2:
                        efecto = "Depresión"

            case "4":
                if esencias[0] == 1:
                    efecto = "Antídoto"
                    if alteracion == 1:
                        efecto = "Corrosiva"
                    if alteracion == 2:
                        efecto = "Alcohol"

                if esencias[0] == 3:
                    efecto = "Agilidad"
                    if alteracion == 1:
                        efecto = "Ceguera"
                    if alteracion == 2:
                        efecto = "Euforia"
    

    pocion_añadida = actualizar_bbdd(personaje_actual, efecto, esencias)

    return pocion_añadida


def actualizar_bbdd(personaje_actual = Personaje, efecto = str, valor_esencias_gastadas = list)->PersonajePotion:
    nueva_pocion = Potion.objects.get(nombre = efecto)
    if not PersonajePotion.objects.filter(personaje = personaje_actual, potion = nueva_pocion).exists():
        pocion_añadida = PersonajePotion.objects.create(
            personaje = personaje_actual,
            potion = nueva_pocion,
            cantidad = 1)
  
    else:
        pocion_añadida = PersonajePotion.objects.get(personaje = personaje_actual, potion = nueva_pocion)
        pocion_añadida.cantidad += 1
        pocion_añadida.save()
    
    for esencia in valor_esencias_gastadas:
        esencia = Esencia.objects.get(valor = esencia)
        personaje = PersonajeEsencias.objects.get(personaje = personaje_actual, esencia = esencia.valor)
        if personaje.cantidad == 0 or None:
            return None
        
        print("COMPROBACION", personaje, esencia)
        personaje.cantidad -= 1
        personaje.save()


    return pocion_añadida
    
    
def generador_ruta_portrait(genero, raza, clase, portrait):
    ruta = f'potion_craft/img/portraits/{raza}/{genero}-{raza}-{clase}-{portrait}.png'
    print(ruta)
    return ruta