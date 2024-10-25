from django import forms
from django.contrib.auth.models import User
from .models import Perfil


class FormularioLogin(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=128)
    contraseña = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['nombre_de_usuario'].label = 'Nombre de usuario'
        self.fields['contraseña'].label = 'Contraseña'

    def clean(self):
        nombre_de_usuario = self.cleaned_data['nombre_de_usuario']
        contraseña = self.cleaned_data['contraseña']
        if not User.objects.filter(username=nombre_de_usuario).exists():
            raise forms.ValidationError('¡No estás registrado!')

        usuario = User.objects.get(username=nombre_de_usuario)
        if usuario and not usuario.check_password(contraseña):
            raise forms.ValidationError('¡Contraseña incorrecta!')


class FormularioRegistro(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    contraseña_confirmar = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'contraseña', 'contraseña_confirmar', 'email']

    def __init__(self, *args, **kwargs):
        super(FormularioRegistro, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['contraseña'].label = 'Contraseña'
        self.fields['contraseña'].help_text = 'Crea una contraseña'
        self.fields['contraseña_confirmar'].label = 'Repite la contraseña'
        self.fields['email'].label = 'Tu correo electrónico'
        self.fields['email'].help_text = 'Por favor, proporciona una dirección real'

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["contraseña"])
        if commit:
            usuario.save()
        return usuario

    def clean(self):
        nombre_de_usuario = self.cleaned_data['username']
        contraseña = self.cleaned_data['contraseña']
        contraseña_confirmar = self.cleaned_data['contraseña_confirmar']
        email = self.cleaned_data['email']
        if User.objects.filter(username=nombre_de_usuario).exists():
            raise forms.ValidationError('¡El nombre de usuario ya está en uso!')
        if contraseña != contraseña_confirmar:
            raise forms.ValidationError('¡Tus contraseñas no coinciden!')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('¡Ya existe un usuario con este correo electrónico!')


class FormularioPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']
        labels = {'foto': 'Avatar'}


class FormularioEdicionUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico'
        }


class FormularioEdicionPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('foto', )
