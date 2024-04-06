from ..models import *




class Inventario():
    def __init__(self, personaje_id):
        super().__init__()
        self.listado_ingredientes = PersonajeIngredientes.objects.filter(personaje = personaje_id)
        self.listado_esencias = PersonajeEsencias.objects.filter(personaje = personaje_id)
        self.listado_pociones = PersonajePotion.objects.filter(personaje = personaje_id)

   
        self.detalles_pociones = []
        for pocion in self.listado_pociones:
            objeto_potion = pocion.potion
            cantidad = pocion.cantidad
            detalles_pocion = {
                'nombre': objeto_potion.nombre,
                'descripcion': objeto_potion.descripcion,
                'cantidad': cantidad}
            self.detalles_pociones.append(detalles_pocion)

        self.detalles_esencias = []
        for esencia in self.listado_esencias:
            objeto_esencia = esencia.esencia
            cantidad = esencia.cantidad
            detalles_esencia = {
                'nombre': objeto_esencia.nombre,
                'tipo': objeto_esencia.tipo,
                'valor' : objeto_esencia.valor,
                'cantidad': cantidad}
            self.detalles_esencias.append(detalles_esencia)



    def __str__(self):
        return f"{self.listado_esencias}, {self.listado_ingredientes}, {self.listado_pociones}"

#!FUNCIONES OBSOLETAS
def dict_ingredientes(personaje_id):
    listado_ingredientes = PersonajeIngredientes.objects.filter(personaje = personaje_id)
    diccionario_ingredientes = {}
    for item in listado_ingredientes:
        diccionario_ingredientes[item.ingrediente] = item.cantidad

    return diccionario_ingredientes


def obtener_listado_esencias(personaje_id):
    """Es posible filtrar directamente por la id que tengamos"""
    #personaje = Personaje.objects.get(id = personaje_id)
    esencias_personaje = PersonajeEsencias.objects.filter(personaje = personaje_id)
    listado_esencias = []

    for esencia in esencias_personaje:
        listado_esencias.append(esencia)
    
    return listado_esencias


    