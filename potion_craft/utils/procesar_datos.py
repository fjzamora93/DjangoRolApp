import random

"""
Esta función puede devolver dos cosas:
En caso de error, devuelve ¡Fallo!
En caso de acierto, devuelve una tupla.
Creo que sería mejor que esta función simplemente actualizase la base de datos
para que en vez de devolver dos cosas, siempre devuelva la misma.
"""

def procesar_datos_ingredientes(ingr, color, proceso, herramienta):
    herramienta = int(herramienta)
    if proceso not in color:
        return "¡Fallo!"
    
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
    return "¡Fallo!" if cantidad == 0  else esencia



def procesar_datos_pocion(base, alteracion, conocimiento, util, dado, esencias = list, ):
    
    base = int(base)
    conocimiento = int(conocimiento)
    util = int(util)
    dado = int(dado)
    sum = dado + util + conocimiento + base
    if sum <= 11:
        return ("¡Tirada fallida!", "dado:", dado, "suma: ", sum, dado, util, conocimiento, base)
    
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
                efecto = "Curación"
                if alteracion == 1:
                    efecto = "Veneno"
                if alteracion == 2:
                    efecto = "Calma"
            case "3":
                efecto = "Resistencia"
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
                    efecto = "Suerte"
                    if alteracion == 1:
                        efecto = "Aturdimiento"
                    if alteracion == 2:
                        efecto = "Locura"

            case "3":
                if esencias[0] == 2:
                    efecto = "Vida Falsa"
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
                    efecto = "Destreza"
                    if alteracion == 1:
                        efecto = "Ceguera"
                    if alteracion == 2:
                        efecto = "Euforia"
    
    return efecto
