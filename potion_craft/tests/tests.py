#COMANDO PARA HACER TEST: python manage.py test potion_craft

import django.test.testcases
import sys


from django.test import TestCase

from potion_craft.utils import procesar_datos as pd

#from potion_craft.utils import procesar_datos_ingredientes


ingr = "eso"
color = "fuego"
proceso = "fuego"
herramienta = 3
esencia = pd.procesar_datos_ingredientes(ingr, color, proceso, herramienta)
print(esencia)

class TestProcesar(TestCase):
    def test_procesar_datos_exito(self):
        ingr = "eso"
        color = "fuego"
        proceso = "fuego"
        herramienta = 3
        resultado = pd.procesar_datos_ingredientes(ingr, color, proceso, herramienta)
        print(resultado)
        self.assertEqual(resultado, "esencia ígnea")

    def test_procesar_datos_fallo(self):
        ingr = "eso"
        color = "fuego"
        proceso = "aire"
        herramienta = 3
        resultado = pd.procesar_datos_ingredientes(ingr, color, proceso, herramienta)
        self.assertEqual(resultado, "¡Fallo!")

    def test_procesar_datos_error(self):
        ingr = "eso"
        color = "aire"
        proceso = "aire"
        herramienta = 3
        resultado = pd.procesar_datos_ingredientes(ingr, color, proceso, herramienta)
        self.assertEqual(resultado, "¡Fallo!")