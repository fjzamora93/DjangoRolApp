from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserProfile



class CustomUserAdmin(UserAdmin):
    # Define los campos que quieres mostrar en la lista de usuarios en el panel de administración
    list_display = ['username', 'nombre', 'email', 'is_staff', 'is_active']

    # Define los campos que deseas que sean enlaces en la lista de usuarios
    list_display_links = ['username', 'nombre']

    # Define los campos que quieres que sean editables en la lista de usuarios
    list_editable = ['is_staff', 'is_active']

    # Define los filtros que quieres utilizar en el panel de administración
    list_filter = ['is_staff', 'is_active']

    # Define los campos de búsqueda que quieres habilitar en el panel de administración
    search_fields = ['username', 'nombre', 'email']

    # Personaliza el formulario de edición para el modelo CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Define los campos a mostrar cuando se crea un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'nombre', 'email', 'is_staff', 'is_active')}
        ),
    )

# Registra cada modelo de forma individual, la única excepción es el de USER.
admin.site.register(UserProfile)
admin.site.register(CustomUser, CustomUserAdmin)