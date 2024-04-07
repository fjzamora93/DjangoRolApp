
import csv
from ..models import *

TABLA_EFECTOS = "potion_craft/utils/tabla_efectos.csv"



def clasificar_esencias(esencias = list, alteracion = str, personaje_actual = Personaje) -> str:
    if all(esen == "0" for esen in esencias):
        efecto = None

    else:
        matriz = leer_csv(TABLA_EFECTOS)
        
        if alteracion == "0":
            efecto = matriz[int(esencias[0])] [int(esencias[1])]
        elif alteracion == "1":
            efecto = matriz[int(esencias[0]) + 5] [int(esencias[1]) + 4]
        elif alteracion == "2":
            efecto = matriz[int(esencias[0]) + 10] [int(esencias[1])+ 8]
        print("--------------------", efecto, int(esencias[0]), int(esencias[1]))
    
    # for esen in esencias:
    #     if esen != "0":
    #         esen = Esencia.objects.get(valor = esencias[0])
    #         personaje_esencias = PersonajeEsencias.objects.get(personaje = personaje_actual, esencia = esen)
    #         personaje_esencias.cantidad -= 1

    return efecto.strip() if efecto != None or efecto != "None" else  None
  

def leer_csv(nombre_archivo):
    matriz = []
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            matriz.append(fila)
    return matriz

matriz = leer_csv(TABLA_EFECTOS)
print(matriz[2][0])
# matriz = leer_csv(TABLA_EFECTOS)

# for fila in matriz:
#     print(fila)





listado_efectos = [
                    [None,    "Maná", "Curativa", "Piel de Piedra", "Fuerza"],
                    ["Maná",    "ELECTRIFICANTE", "Suerte Líquida", None, "Agilidad"],
                    ["Curativa", "Suerte Líquida", "CONGELACIÓN", "Falsa Vida", None],
                    ["Piel de Piedra", None, "Falsa Vida", "PETRIFICACIÓN", "Antídoto"],
                    ["Fuerza", "Agilidad", None, "Antídoto", "EXPLOSIVA"],
                ]

listado_efectos_alteracion_1 = [
                        [None, "Desconcentración", "Veneno", "Petrificación", "Debilitadora"],
                        ["Desconcentración", "SILENCIO", "Agotamiento", None, "Aturdimiento"],
                        ["Veneno", "Agotamiento", "CONGELACIÓN", "Fragilidad", None],
                        ["Petrificación", None, "Fragilidad", "PETRIFICACIÓN", "Corrosiva"],
                        ["Debilitadora", "Aturdimiento", None, "Corrosiva", "EXPLOSIVA"],
                    ]

listado_efectos_alteracion_2 = [
                        [None, "Desconcentración", "Veneno", "Petrificación", "Debilitadora"],
                        ["Desconcentración", "ELECTRIFICANTE", "Congelación", None, "Aturdimiento"],
                        ["Veneno", "Congelación", "CONGELACIÓN", "Fragilidad", None],
                        ["Petrificación", None, "Fragilidad", "PETRIFICACIÓN", "Corrosiva"],
                        ["Debilitadora", "Aturdimiento", None, "Corrosiva", "EXPLOSIVA"],
                    ]
    # if len(esencias) == 1:
    #     print("listado de 1 solo ingrediente", esencias, esencias[0])
    #     match esencias[0]:
    #         case "1":
    #             efecto = "Maná"
    #             if alteracion == 1:
    #                 efecto = "Eléctrica"
    #             if alteracion == 2:
    #                 efecto = "Inspiración"

    #         case "2":
    #             efecto = "Curativa"
    #             if alteracion == 1:
    #                 efecto = "Veneno"
    #             if alteracion == 2:
    #                 efecto = "Calma"
    #         case "3":
    #             efecto = "Piel de Piedra"
    #             if alteracion == 1:
    #                 efecto = "Petrificación"
    #             if alteracion == 2:
    #                 efecto = "Concentración"
    #         case "4":
    #             efecto = "Fuerza"
    #             if alteracion == 1:
    #                 efecto = "Explosiva"
    #             if alteracion == 2:
    #                 efecto = "Furia"
    # if len(esencias) == 2:
    #     print("listado de 2 ingredientes", esencias, esencias[1])
    #     match esencias[1]:
    #         case "2":
    #             if esencias[0] == 1:
    #                 efecto = "Suerte Líquida"
    #                 if alteracion == 1:
    #                     efecto = "Aturdimiento"
    #                 if alteracion == 2:
    #                     efecto = "Locura"

    #         case "3":
    #             if esencias[0] == 2:
    #                 efecto = "Falsa Vida"
    #                 if alteracion == 1:
    #                     efecto = "Congelación"
    #                 if alteracion == 2:
    #                     efecto = "Depresión"

    #         case "4":
    #             if esencias[0] == 1:
    #                 efecto = "Antídoto"
    #                 if alteracion == 1:
    #                     efecto = "Corrosiva"
    #                 if alteracion == 2:
    #                     efecto = "Alcohol"

    #             if esencias[0] == 3:
    #                 efecto = "Agilidad"
    #                 if alteracion == 1:
    #                     efecto = "Ceguera"
    #                 if alteracion == 2:
    #                     efecto = "Euforia"
    