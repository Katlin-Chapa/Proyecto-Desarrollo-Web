from django.contrib import admin
from .models import Categoria, Subcategoria, Producto, ImagenProducto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'subcategoria', 'fecha_ingreso')
    search_fields = ('nombre',)
    list_filter = ('subcategoria',)
    ordering = ('-fecha_ingreso',)

@admin.register(ImagenProducto)
class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'imagen')
    search_fields = ('producto__nombre',)

