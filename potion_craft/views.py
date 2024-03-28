from django.shortcuts import render
import datetime, random
from django import forms

#importamos esto, para que podamos usar el HttpResponse.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from potion_craft.utils import procesar_datos as proc
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.models import UserProfile

#En esta función vamos a ver cómo insertar y crear varibles en HTML desde Python. 


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

esencias = []

def index(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        print("INTENTO CON ÉXITO: ", user_profile.nombre )
        
    except UserProfile.DoesNotExist:
        user_profile = None
        print("NO HAY PERFIL DE USUARIO")

    if "potion" not in request.session:
        request.session["potion"] = []
    return render(request, "potion_craft/index.html", {
        "potion_form": request.session["potion"],
        "user_profile": user_profile
        }
    )

def character_creator(request):
    return render(request, "potion_craft/character_creator.html",{
        "form": CharacterForm()
    })

def inventario(request):
     return render(request, "potion_craft/inventario.html", {
          
     })

def ingredient_craft(request):
    if request.method == "POST":
        form_ingrediente = IngredienteForm(request.POST)
       
        if form_ingrediente.is_valid():
            #Entre corchetes va el nombre del campo que quiero recuperar. 
            #Recuerda que el método .cleaned_data[] te hace perder los label, así que usaremos fields y choices en su lugar
            ingr = form_ingrediente.cleaned_data['ingr']
            color = form_ingrediente.cleaned_data['color']
            proceso = form_ingrediente.cleaned_data['proceso']
            herramienta = form_ingrediente.cleaned_data['herramienta']
            

            esencia = proc.procesar_datos_ingredientes(ingr, color, proceso, herramienta)
            esencias.append(esencia)
            print(esencia)
            
            if "ingredientes" not in request.session:
                request.session["ingredientes"] = []
            #request.session["lista"] es una lista que va a ir guardando los datos de sesión tal y como le diga.
            request.session["ingredientes"] += [esencia]

            return HttpResponseRedirect(reverse("potion_craft:potion"))
            
        else:
            print("Formulario NO válido")
            return render(request, "potion_craft/craft.html", {
                "form_ingrediente": PotionForm(request.POST),
              
            })
    return render(request, "potion_craft/craft.html", {
    "form_ingrediente": IngredienteForm(request.POST),
    
})

import random
from django.shortcuts import render
from .forms import PotionForm

def potion_craft(request):
   
    if "ingredientes" not in request.session:
        request.session["ingredientes"] = []
    if "potion" not in request.session:
                request.session["potion"] = []

    
    if request.method == "POST":
        print("CONDICIÓN 1")
        form_potion = PotionForm(request.POST)
        
        if form_potion.is_valid():
            print("FORMULARIO VÁLIDO")
            dado = form_potion.cleaned_data['dado']
            base = form_potion.cleaned_data['base']
            alter = form_potion.cleaned_data['alter']
            conocimiento = form_potion.cleaned_data['conocimiento']
            util = form_potion.cleaned_data['util']
            esencias = form_potion.cleaned_data['esencias']

            resultado_pocion = proc.procesar_datos_pocion(base, alter, conocimiento, util, dado, esencias)
            
            request.session["potion"] += [resultado_pocion]
            print(resultado_pocion)
            return HttpResponseRedirect(reverse("potion_craft:index"))
            
        else:
            print(form_potion.errors)
            
            return render(request, "potion_craft/potion.html", {
                    "form_potion": PotionForm(request.POST),
                })
    
    else:
        form_potion = PotionForm(initial={'dado': 11})


    return render(request, "potion_craft/potion.html", {
        "ingredientes": request.session["ingredientes"],
        "form_potion": form_potion,
        
    })




def borrar_datos_sesion(request):
    if 'ingredientes' in request.session:
        del request.session['ingredientes']
        del request.session['potion']
    return HttpResponseRedirect(reverse("potion_craft:potion"))  # Redirecciona a la vista que desees después de borrar los datos de sesión




"""
def lista(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "hello/lista.html", {
        "tasks" : request.session["tasks"],
        "tareas": tareas,
        }
    )

"""


"""
if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tareas.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("primer_proyecto:lista"))
        
        else:
            return render(request, "hello/añadir.html", {
                "form":form
            })
    
    return render(request, "hello/añadir.html", {
        "form" : NewTaskForm() 
    })

"""