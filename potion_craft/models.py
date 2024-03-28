from django.db import models


class Personaje(models.Model):
    nombre = models.CharField(max_length = 25, unique=True)
    clase = models.CharField(max_length = 25, null=True, blank=True)
    portrait = models.CharField(max_length = 150, null=True, blank=True)
    def __str__(self):
        return self.nombre


class Esencia(models.Model):
    nombre = models.CharField(max_length=25, default='Esencia')
    tipo = models.CharField(max_length = 25, help_text='aire / agua / fuego / tierra') #elemento
    def __str__(self):
        return f"{self.nombre}, del tipo: {self.tipo} "
    
class Ingrediente(models.Model):
    nombre = models.CharField(max_length = 25)
    descripcion = models.CharField(max_length = 140)
    esencias = models.ManyToManyField(Esencia, related_name="esencias_por_ingredientes")
    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"


class Potion(models.Model):
    nombre = models.CharField(max_length = 25)
    descripcion = models.CharField(max_length = 140)
    esencias = models.ManyToManyField('Esencia', related_name='esencias_por_pocion')
    alteracion = models.CharField(max_length=25, default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}: {self.descripcion} "


"""Y  A PARTIR DE AQUÍ LAS RELACIONES CON ATRIBUTOOS PARA EXPRESAR LA CANTIDAD"""

class PersonajePotion(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    potion = models.ForeignKey(Potion, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.personaje.nombre} tiene {self.cantidad} unidades de {self.potion.nombre}"
    

class PersonajeEsencias(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    esencia = models.ForeignKey(Esencia, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    


    def __str__(self):
        return f"{self.personaje.nombre} tiene {self.cantidad} unidades de {self.esencia.nombre}"
    
class PersonajeIngredientes(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.personaje.nombre} tiene {self.cantidad} unidades de {self.ingrediente.nombre}"