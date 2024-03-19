from django.shortcuts import render
import datetime
from django import forms

#importamos esto, para que podamos usar el HttpResponse.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *

# Create your views here.

#En esta función vamos a ver cómo insertar y crear varibles en HTML desde Python. 



def index(request):
    #Paso 1, definimos la variable
    now = datetime.datetime.now()
    return render(request, "potion_craft/index.html", {
        "newyear": now.month == 1 and now.day == 1
        }
    )

def potion_craft(request):
    form = PotionForm(request.POST)

    return render(request, "potion_craft/craft.html", {
        "form" : form
    })


#http://127.0.0.1:8000/hello/javi
