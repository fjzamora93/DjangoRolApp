from django.shortcuts import render, redirect
import datetime, random
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *
from potion_craft.utils import procesar_datos as proc
from potion_craft.utils import ObtencionDatos as obt
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required

# class UserProfileDetailView(DetailView):
#     model = UserProfile
#     template_name = 'perfil.html' 

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_profile = self.get_object()
#         context['personajes'] = user_profile.personajes.all()
#         return context


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def index(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        listado_personajes = Personaje.objects.filter(user_profile = user_profile)
       
    except UserProfile.DoesNotExist:
        user_profile = None
    
    if request.method == "GET":
        personaje_seleccionado = request.GET.get('personaje', '')
        request.session['personaje'] = personaje_seleccionado
        print("Request Session (cogemos la ID del personaje): ", personaje_seleccionado)
       

    return render(request, "potion_craft/index.html", {
        "user_profile": user_profile,
        "listado_personajes" : listado_personajes,
        "personaje_seleccionado" : personaje_seleccionado
       
        })

#AHORA MISMO FUNCIONA DE TAL FORMA QUE SOLAMENTE COGE UN PERSONAJE PARA CADA JUGADOR
@login_required
def inventario(request, personaje_id = 2):
    personaje = Personaje.objects.get(id = personaje_id)
    user_profile = UserProfile.objects.get(user=request.user)
    if request.session['personaje']:
        personaje_seleccionado = request.session['personaje']
        personaje = Personaje.objects.get(id = personaje.id)
    else:
        personaje = Personaje.objects.get(id = personaje.id)
    
    if request.method == "GET":
        personaje_seleccionado = request.GET.get('personaje', '')
        request.session['personaje'] = personaje_seleccionado
        print("Request Session (cogemos la ID en el INVENTARIO): ", personaje_seleccionado)
      
    listado_personajes = Personaje.objects.filter(user_profile = user_profile) if request.user.is_authenticated else []
    return render(request, "potion_craft/inventario.html", {
        "perfiles" : UserProfile.objects.all(),
        "personaje" : personaje,
        "listado_personajes" : listado_personajes,
        "usuario" : user_profile,
     })


def inventario_detail(request, personaje_id):
    personaje = Personaje.objects.get(id = personaje_id)
    request.session['personaje'] = personaje.id

    listado_esencias = PersonajeEsencias.objects.filter(personaje = personaje_id)
    listado_ingredientes = PersonajeIngredientes.objects.filter(personaje = personaje_id)
    listado_pociones = PersonajePotion.objects.filter(personaje = personaje_id)
    print("PRINT INVENTARIO ", personaje.id, listado_pociones)



    return render(request, "potion_craft/inventario_detail.html",{
        "personaje" : personaje,
        "listado_ingredientes" : listado_ingredientes,
        "listado_esencias" : listado_esencias,
        "listado_pociones" : listado_pociones,
    })


def character_creator(request):
    form = CharacterForm()
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            print("FORMULARIO DE CREACIÓN DE PERSONAJE VALIDADO!!")
            personaje = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)

            personaje.user_profile = user_profile
            personaje.save()
            return redirect("potion_craft:inventario")
        else:
            print(form.errors)
 
    return render(request, "potion_craft/character_creator.html",{
        "form": form
    })


def ingredient_craft(request):
    esencias = []
    if request.method == "POST":
        form_ingrediente = IngredienteForm(request.POST)
        if form_ingrediente.is_valid():
            ingr = form_ingrediente.cleaned_data['ingr']
            color = form_ingrediente.cleaned_data['color']
            proceso = form_ingrediente.cleaned_data['proceso']
            herramienta = form_ingrediente.cleaned_data['herramienta']
            esencia = proc.procesar_datos_ingredientes(ingr, color, proceso, herramienta)
            esencias.append(esencia)
            if "ingredientes" not in request.session:
                request.session["ingredientes"] = []
    
            request.session["ingredientes"] += [esencia]

            return HttpResponseRedirect(reverse("potion_craft:potion"))
            
        else:
            print(form_ingrediente.errors)
           
    return render(request, "potion_craft/craft.html", {
    "form_ingrediente": IngredienteForm(request.POST),
    
})


def potion_craft(request):
    personaje_actual = request.session['personaje']
    personaje_actual = Personaje.objects.get(id = personaje_actual)
    form_potion = PotionForm(initial={'dado': 11}, personaje= personaje_actual)

    inventario = obt.Inventario(personaje_actual)
    print("Personaje actual: ", inventario.listado_pociones)
    
    
    return render(request, "potion_craft/potion.html", {
        "inventario" : inventario,
        "personaje" : personaje_actual,
        "form_potion" : form_potion
    })



def borrar_datos_sesion(request):
    if 'ingredientes' in request.session:
        del request.session['ingredientes']
        del request.session['potion']
    return HttpResponseRedirect(reverse("potion_craft:potion"))  # Redirecciona a la vista que desees después de borrar los datos de sesión




# def potion_craft(request):
#     if "ingredientes" not in request.session:
#         request.session["ingredientes"] = []
#     if "potion" not in request.session:
#         request.session["potion"] = []

    
#     if request.method == "POST":
#         form_potion = PotionForm(request.POST)
#         if form_potion.is_valid():
#             print("FORMULARIO VÁLIDO")
#             dado = form_potion.cleaned_data['dado']
#             base = form_potion.cleaned_data['base']
#             alter = form_potion.cleaned_data['alter']
#             conocimiento = form_potion.cleaned_data['conocimiento']
#             util = form_potion.cleaned_data['util']
#             esencias = form_potion.cleaned_data['esencias']

#             resultado_pocion = proc.procesar_datos_pocion(base, alter, conocimiento, util, dado, esencias)
            
#             request.session["potion"] += [resultado_pocion]
#             print(resultado_pocion)
#             return HttpResponseRedirect(reverse("potion_craft:index"))
            
#         else:
#             print(form_potion.errors)
            
#             return render(request, "potion_craft/potion.html", {
#                     "form_potion": PotionForm(request.POST),
#                 })
    
#     else:
#         form_potion = PotionForm(initial={'dado': 11})


#     return render(request, "potion_craft/potion.html", {
#         "ingredientes": request.session["ingredientes"],
#         "form_potion": form_potion,
#     })