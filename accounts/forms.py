# en forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nombre']  # Agrega aquí los campos adicionales necesarios




#TODO ADAPTACION DEL PREFABRICADO
class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Ingresa un nombre de usuario'
        })

    username = forms.CharField(label='Nombre de usuario', max_length=150, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text=
        "Tu contraseña no puede ser demasiado similar a tu otra información personal.<br> "
        "Tu contraseña debe contener al menos 8 caracteres.<br> "
        "Tu contraseña no puede ser una contraseña común.<br> "
        "Tu contraseña no puede ser completamente numérica.")
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput, help_text='Ingrese la misma contraseña que antes, para verificación.')

    class Meta:
        model = User
        fields = ('username',  'password1', 'password2')



#TODO CREACIÓN DE USUARIOS PERSONALIZADO (PROPENSO A ERRORES)
class SignupFormPersonalizado(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'placeholder': 'Escribe un nombre público'
        })
    username = forms.CharField(label='Nombre de usuario', max_length=150, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.')
    nombre = forms.CharField(label='Nombre', help_text='Obligatorio')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text=
        "Tu contraseña no puede ser demasiado similar a tu otra información personal.<br> "
        "Tu contraseña debe contener al menos 8 caracteres.<br> "
        "Tu contraseña no puede ser completamente numérica.")
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput, help_text='Ingrese la misma contraseña que antes, para verificación.')
    class Meta:
        model = CustomUser
        fields = ['username', 'nombre', 'password1', 'password2']

