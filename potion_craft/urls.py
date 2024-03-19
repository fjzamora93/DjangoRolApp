from django.urls import path
from . import views



app_name = "potion_craft"

urlpatterns=[
    path("", views.index, name="index"), #Cuando alguien visite la url vacía, verá la index.
    path("craft", views.potion_craft, name="craft"),
]

