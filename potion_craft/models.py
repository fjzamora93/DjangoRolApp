from django.db import models


class Personaje(models.Model):
    nombre = models.CharField(max_length = 25)
    ingredientes = models.ManyToManyField('Ingrediente', related_name='personaje_ingrediente')
    esencias = models.ManyToManyField('Esencia', related_name='personaje_esencia')
    potions = models.ManyToManyField('Potion', related_name='personaje_potion')
    def __str__(self):
        return self.nombre


class Esencia(models.Model):
    tipo = models.CharField(max_length = 25)
    cantidad = models.IntegerField()
    def __str__(self):
        return f"{self.cantidad} unidades de {self.tipo} "
    
class Ingrediente(models.Model):
    nombre = models.CharField(max_length = 25)
    descripcion = models.CharField(max_length = 25)
    cantidad = models.IntegerField()
    esencia = models.ForeignKey(Esencia, on_delete = models.CASCADE, related_name = "esencia_en_ingrediente")
    def __str__(self):
        return f"{self.cantidad} unidades de {self.nombre} {self.descripcion}"

class Potion(models.Model):
    nombre = models.CharField(max_length = 25)
    descripcion = models.CharField(max_length = 140)
    cantidad = models.IntegerField()
    esencias = models.ManyToManyField('Esencia', related_name='esencias_por_pocion')
    def __str__(self):
        return f"{self.cantidad} unidades de {self.nombre}. {self.descripcion} "
