from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='photo/', blank=True)

    def __str__(self):
        return 'Perfil para el usuario {}'.format(self.usuario.username)
