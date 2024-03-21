from django.urls import path
from . import views



app_name = "potion_craft"

urlpatterns=[
    path("", views.index, name="index"), #Cuando alguien visite la url vacía, verá la index.
    path("craft", views.ingredient_craft, name="craft"),
    path("potion", views.potion_craft, name="potion"),
    path('borrar-datos-sesion/', views.borrar_datos_sesion, name='borrar_datos_sesion'),
]

