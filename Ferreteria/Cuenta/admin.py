from django.contrib import admin
from .models import Perfil


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha_de_nacimiento', 'foto']


admin.site.register(Perfil, PerfilAdmin)
