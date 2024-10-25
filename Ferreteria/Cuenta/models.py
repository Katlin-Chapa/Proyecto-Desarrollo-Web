from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AdministradorCuenta(BaseUserManager):
    def crear_usuario(self, nombre, apellido, nombre_usuario, correo, contrasena=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')

        if not nombre_usuario:
            raise ValueError('El usuario debe tener un nombre de usuario')

        usuario = self.model(
            correo=self.normalize_email(correo),
            nombre_usuario=nombre_usuario,
            nombre=nombre,
            apellido=apellido,
        )

        usuario.set_password(contrasena)
        usuario.save(using=self._db)
        return usuario

    def crear_superusuario(self, nombre, apellido, correo, nombre_usuario, contrasena):
        usuario = self.crear_usuario(
            correo=self.normalize_email(correo),
            nombre_usuario=nombre_usuario,
            contrasena=contrasena,
            nombre=nombre,
            apellido=apellido,
        )

        usuario.es_admin = True
        usuario.esta_activo = True
        usuario.es_staff = True
        usuario.es_superadmin = True
        usuario.save(using=self._db)
        return usuario


class Cuenta(AbstractBaseUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=55)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(max_length=50, unique=True)
    numero_telefono = models.CharField(max_length=50)

    # Campos de atributos
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultimo_login = models.DateTimeField(auto_now_add=True)
    es_admin = models.BooleanField(default=False)
    es_staff = models.BooleanField(default=False)
    esta_activo = models.BooleanField(default=False)
    es_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre_usuario', 'nombre', 'apellido']

    objects = AdministradorCuenta()

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    def __str__(self):
        return self.correo

    def tiene_permiso(self, perm, obj=None):
        return self.es_admin

    def tiene_permisos_modulo(self, etiqueta_modulo):
        return True


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(Cuenta, on_delete=models.CASCADE)
    direccion_linea_1 = models.CharField(blank=True, max_length=100)
    direccion_linea_2 = models.CharField(blank=True, max_length=100)
    imagen_perfil = models.ImageField(blank=True, upload_to='perfilusuario')
    ciudad = models.CharField(blank=True, max_length=20)
    estado = models.CharField(blank=True, max_length=5)
    pais = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.usuario.nombre

    def direccion_completa(self):
        return f'{self.direccion_linea_1} {self.direccion_linea_2}'
