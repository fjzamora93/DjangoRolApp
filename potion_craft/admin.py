from django.contrib import admin

# Register your models here.
from potion_craft.models import *

admin.site.register(Personaje)
admin.site.register(Potion)
admin.site.register(Esencia)
admin.site.register(Ingrediente)

admin.site.register(PersonajePotion)
admin.site.register(PersonajeEsencias)
admin.site.register(PersonajeIngredientes)