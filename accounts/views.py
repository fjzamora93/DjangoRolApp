from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#En esta función vamos a ver cómo insertar y crear varibles en HTML desde Python. 

from .forms import SignupForm, SignupFormPersonalizado
from django.views.decorators.csrf import csrf_protect


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@csrf_protect
def signup(request):
    print("SE HA HECHO POR AQUÍ")
    if request.method == 'POST':
        formulario = SignupForm(request.POST)
        #formulario_prefabricado = SignupForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            login(request, user)
            return redirect('index')
    else:
        formulario = SignupForm()
        #formulario_prefabricado = SignupForm()
                                                        
    return render(request, 'registration/signup.html', 
                  {'formulario':formulario,
                #'formulario_prefabricado': formulario_prefabricado
                   })

# from django.contrib.auth.views import LoginView
# from accounts.forms import CustomAuthenticationForm
# class CustomLoginView(LoginView):
#     authentication_form = CustomAuthenticationForm