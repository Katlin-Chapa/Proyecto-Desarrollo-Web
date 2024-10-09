from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, null=False)  # No permite nulos

    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=255, null=False)  # No permite nulos
    categoria = models.ForeignKey(Categoria, related_name='subcategorias', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=False)  # No permite nulos
    descripcion = models.TextField(null=False)  # No permite nulos
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)  # No permite nulos
    stock = models.IntegerField(null=False)  # No permite nulos
    subcategoria = models.ForeignKey(Subcategoria, related_name='productos', on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

