from django.contrib import admin
from .models import Producto

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'fecha_ingreso')
    
    # Permitir búsqueda por ciertos campos
    search_fields = ('nombre', 'categoria')
    
    # Filtros disponibles en la interfaz de administración
    list_filter = ('categoria',)
    
    # Opcional: permite ordenar los productos por fecha de ingreso
    ordering = ('-fecha_ingreso',)
