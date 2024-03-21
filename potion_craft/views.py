from django.shortcuts import render
import datetime
from django import forms

#importamos esto, para que podamos usar el HttpResponse.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *

# Create your views here.

#En esta función vamos a ver cómo insertar y crear varibles en HTML desde Python. 

ingredientes = []

def index(request):
    #Paso 1, definimos la variable
    now = datetime.datetime.now()
    return render(request, "potion_craft/index.html", {
        "newyear": now.month == 1 and now.day == 1
        }
    )

def ingredient_craft(request):
    
    if request.method == "POST":
        print("Condición 0")
        form_ingrediente = IngredienteForm(request.POST)
        form_potion = PotionForm(request.POST)
        if form_ingrediente.is_valid():
            print("Condición 1")

            #Entre corchetes va el nombre del campo que quiero recuperar
            ingrediente = form_ingrediente.cleaned_data["planta"]


            ingredientes.append(ingrediente)

            #request.session["lista"] es una lista que va a ir guardando los datos de sesión tal y como le diga.
            request.session["ingredientes"] = request.session.get("ingredientes", []) + [ingrediente]

            return HttpResponseRedirect(reverse("potion_craft:potion"))
            
    
        else:
            print("Condición 2")
            return render(request, "potion_craft/craft.html", {
                "form_ingrediente": PotionForm(request.POST),
                "form_potion": IngredienteForm(),
            })
    print("Condición nula")
    return render(request, "potion_craft/craft.html", {
    "form_ingrediente": IngredienteForm(request.POST),
    "form_potion": PotionForm(),
})

def potion_craft(request):
    if "ingredientes" not in request.session:
        request.session["ingredientes"] = []
    
    return render(request, "potion_craft/potion.html",{
        "ingredientes" : request.session["ingredientes"]
    })
    



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


def borrar_datos_sesion(request):
    if 'ingredientes' in request.session:
        del request.session['ingredientes']
    return HttpResponseRedirect(reverse("potion_craft:craft"))  # Redirecciona a la vista que desees después de borrar los datos de sesión
