from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView 
from . import views
from .views import *



app_name = "potion_craft"

#RECUERDA QUE LA PÁGINA DE LOGIN ESTÁ AQUÍ: http://127.0.0.1:8000/accounts/login/
#El login está en ACCOUNTS, y no en la app como tal.

app_name = "potion_craft"

urlpatterns = [
    path("", views.index, name="index"), #Cuando alguien visite la url vacía, verá la index.
    path("craft/", views.ingredient_craft, name="craft"),
    path("potion/", views.potion_craft, name="potion"),
    path('inventario/', views.inventario, name='inventario'),
    path("inventario/<int:personaje_id>", views.inventario_detail, name="inventario_detail"),

    path('character_creator/', views.character_creator, name='character_creator'),
    path('borrar/', views.borrar_datos_sesion, name='borrar'),
    path('admin/', admin.site.urls),
]

