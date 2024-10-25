from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta, PerfilUsuario
from django.utils.html import format_html

class CuentaAdmin(UserAdmin):
    list_display = ('correo', 'nombre', 'apellido', 'nombre_usuario', 'ultimo_acceso', 'fecha_registro', 'activo')
    list_display_links = ('correo', 'nombre', 'apellido')
    readonly_fields = ('ultimo_acceso', 'fecha_registro')
    ordering = ('-fecha_registro',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class PerfilUsuarioAdmin(admin.ModelAdmin):
    def miniatura(self, objeto):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(objeto.imagen_perfil.url))

    miniatura.short_description = "Imagen de perfil"
    list_display = ('miniatura', 'usuario', 'ciudad', 'estado', 'pais')

admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
