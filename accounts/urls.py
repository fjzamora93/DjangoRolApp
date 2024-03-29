from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView 
from . import views
from .views import SignUpView



app_name = "accounts"

#RECUERDA QUE LA PÁGINA DE LOGIN ESTÁ AQUÍ: http://127.0.0.1:8000/accounts/login/
#El login está en ACCOUNTS, y no en la app como tal.

urlpatterns=[
    path('', TemplateView.as_view(template_name="potion_craft/index.html"), name="index"),
    #path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/", views.signup, name="signup"),
    
]

