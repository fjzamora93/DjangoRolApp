from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



def generate_unique_name():
    return str(uuid.uuid4())[:7]  # Genera un valor único basado en un UUID y toma los primeros 8 caracteres


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, default=generate_unique_name)
   
    def __str__(self):
        return self.user.username














def validate_password(value):
    if value < 4:
        raise ValidationError("Contraseña demasiado corta")

class CustomUser(AbstractUser):
    #Aquí podrías añadir cualquier campo que quieras al registrarse el usuario (extiende el prefabricado)
    nombre = models.CharField(max_length=25, default=generate_unique_name)
    password = models.CharField(max_length=15, validators=[validate_password])
    
# # Configuración para evitar conflictos de acceso inverso con grupos y permisos
CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'