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
from django.views.decorators.csrf import csrf_protect

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

@csrf_protect
def index(request):
    form = CharacterForm()
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        listado_personajes = Personaje.objects.filter(user_profile = user_profile)
        if 'personaje' in request.session:
            personaje_seleccionado = request.session['personaje']
        else:
            request.session['personaje'] = ''

    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, "potion_craft/index.html", {
        "user_profile": user_profile,
        "listado_personajes" : listado_personajes,
        "personaje_seleccionado" : personaje_seleccionado,
        "form": form
        })

#AHORA MISMO FUNCIONA DE TAL FORMA QUE SOLAMENTE COGE UN PERSONAJE PARA CADA JUGADOR
@login_required
@csrf_protect
def inventario(request, personaje_id = 2):
    if 'personaje' not in request.session or request.session['personaje'] == "":
        alerta = "Selecciona un personaje"
    else:
        alerta =""
    personaje = Personaje.objects.get(id = personaje_id)
    user_profile = UserProfile.objects.get(user=request.user)
    if 'personaje' in request.session:
        personaje_seleccionado = request.session['personaje']
    else:
        request.session['personaje'] = None
      
    listado_personajes = Personaje.objects.filter(user_profile = user_profile) if request.user.is_authenticated else []
    return render(request, "potion_craft/inventario.html", {
        "perfiles" : UserProfile.objects.all(),
        "personaje" : personaje,
        "listado_personajes" : listado_personajes,
        "usuario" : user_profile,
        "alerta" : alerta,
     })

@csrf_protect
def inventario_detail(request, personaje_id):
    personaje = Personaje.objects.get(id = personaje_id)
    request.session['personaje'] = personaje.id

    listado_esencias = PersonajeEsencias.objects.filter(personaje = personaje_id)
    listado_ingredientes = PersonajeIngredientes.objects.filter(personaje = personaje_id)
    listado_pociones = PersonajePotion.objects.filter(personaje = personaje_id)
   

    return render(request, "potion_craft/inventario_detail.html",{
        "personaje" : personaje,
        "listado_ingredientes" : listado_ingredientes,
        "listado_esencias" : listado_esencias,
        "listado_pociones" : listado_pociones,
    })

@csrf_protect
def character_creator(request):
    form = CharacterForm()
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            print("FORMULARIO DE CREACIÓN DE PERSONAJE VALIDADO!!")
            personaje = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)

            personaje.user_profile = user_profile
            personaje.portrait = proc.generador_ruta_portrait(personaje.genero, personaje.raza, personaje.clase, personaje.portrait)
            personaje.save()
            return redirect("potion_craft:inventario")
        else:
            print(form.errors)
 
    return render(request, "potion_craft/character_creator.html",{
        "form": form
    })

@csrf_protect
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

@csrf_protect
def potion_craft(request):
    if 'personaje' not in request.session or request.session['personaje'] == "":
        return HttpResponseRedirect(reverse("potion_craft:inventario"))

    personaje_actual = request.session['personaje']
    personaje_actual = Personaje.objects.get(id = personaje_actual)
    form_potion = PotionForm(initial={'dado': 11}, personaje= personaje_actual)
    inventario = obt.Inventario(personaje_actual)

    if request.method == "POST":
        form_potion = PotionForm(request.POST, personaje=personaje_actual)

        if form_potion.is_valid():
            dado = form_potion.cleaned_data['dado']
            base = form_potion.cleaned_data['base']
            alter = form_potion.cleaned_data['alter']
            conocimiento = form_potion.cleaned_data['conocimiento']
            util = form_potion.cleaned_data['util']

            esencia_1 = form_potion.cleaned_data['esencia_1']
            esencia_2 = form_potion.cleaned_data['esencia_2']
            esencias = [esencia_1, esencia_2]

            pocion_añadida = proc.procesar_datos_pocion(base, alter, conocimiento, 
                                                          util, dado, esencias, personaje_actual)
            
            #TODO CREAR UN CASO PARA MANEJAR EL "NONE" (cuando las esencias eran 0 y cuando la poción falla)
            if pocion_añadida != None:
                request.session["potion"] = pocion_añadida.potion.nombre
                return redirect("potion_craft:inventario_detail", personaje_id=personaje_actual.id)
              
        else:
            form_potion = PotionForm(initial={'dado': 11}, personaje=personaje_actual)
            
    
    return render(request, "potion_craft/potion.html", {
        "inventario" : inventario,
        "personaje" : personaje_actual,
        "form_potion" : form_potion
    })


@csrf_protect
def borrar_datos_sesion(request):
    if 'ingredientes' in request.session:
        del request.session['ingredientes']
        del request.session['potion']
    return HttpResponseRedirect(reverse("potion_craft:potion"))  # Redirecciona a la vista que desees después de borrar los datos de sesión



