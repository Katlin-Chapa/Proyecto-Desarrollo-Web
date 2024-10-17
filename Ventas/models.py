from django.db import models
from django.contrib.auth import get_user_model
from Inventario.models import Producto

class DetalleVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    usuario = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)  # Cambiado aquí

    def save(self, *args, **kwargs):
        self.subtotal = self.producto.precio * self.cantidad  # Calcular subtotal
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.producto.nombre} - Cantidad: {self.cantidad}'
