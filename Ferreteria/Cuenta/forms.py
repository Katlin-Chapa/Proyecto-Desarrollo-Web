from django import forms
from .models import Cuenta, PerfilUsuario

class FormularioRegistro(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese Contraseña',
        'class': 'form-control',
    }))
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar Contraseña',
        'class': 'form-control',
    }))

    class Meta:
        model = Cuenta
        fields = ['nombre', 'apellido', 'numero_telefono', 'correo', 'contrasena']

    def __init__(self, *args, **kwargs):
        super(FormularioRegistro, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Ingrese su nombre'
        self.fields['apellido'].widget.attrs['placeholder'] = 'Ingrese sus apellidos'
        self.fields['numero_telefono'].widget.attrs['placeholder'] = 'Ingrese su número'
        self.fields['correo'].widget.attrs['placeholder'] = 'Ingrese su correo'
        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = 'form-control'

    def clean(self):
        datos_limpios = super(FormularioRegistro, self).clean()
        contrasena = datos_limpios.get('contrasena')
        confirmar_contrasena = datos_limpios.get('confirmar_contrasena')

        if contrasena != confirmar_contrasena:
            raise forms.ValidationError(
                'Parece que la contraseña no coincide, verifique su información'
            )


class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ('nombre', 'apellido', 'numero_telefono')

    def __init__(self, *args, **kwargs):
        super(FormularioUsuario, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = 'form-control'


class FormularioPerfilUsuario(forms.ModelForm):
    imagen_perfil = forms.ImageField(
        required=False,
        error_messages={'invalid': ('Solo archivos de imagen')},
        widget=forms.FileInput
    )

    class Meta:
        model = PerfilUsuario
        fields = ('direccion_linea_1', 'direccion_linea_2', 'ciudad', 'estado', 'pais', 'imagen_perfil')

    def __init__(self, *args, **kwargs):
        super(FormularioPerfilUsuario, self).__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs['class'] = 'form-control'
