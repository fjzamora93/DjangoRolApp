from django.contrib.auth.models import User
from .models import UserProfile

def create_missing_user_profiles():
    users_without_profile = User.objects.filter(userprofile__isnull=True)
    for user in users_without_profile:
        UserProfile.objects.create(user=user)

# Ejecuta la función para crear los perfiles faltantes
create_missing_user_profiles()