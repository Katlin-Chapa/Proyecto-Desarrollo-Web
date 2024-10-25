from django import forms

CANTIDAD_PRODUCTO_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CarritoAgregarProductoForm(forms.Form):
    cantidad = forms.TypedChoiceField(choices=CANTIDAD_PRODUCTO_CHOICES, coerce=int)
    actualizar = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
