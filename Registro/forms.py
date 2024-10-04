# Registro/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from AutenticacionPersonalizada.models import AutenticacionUsuario  # Asegúrate de que la importación sea correcta

class RegistroFormulario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = AutenticacionUsuario
        fields = ('username', 'email', 'password1', 'password2')
