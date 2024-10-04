# registro/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistroFormulario  # Importa tu formulario personalizado

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Error en el registro. Asegúrate de que los datos sean válidos.')
    else:
        form = RegistroFormulario()

    return render(request, 'registro.html', {'form': form})
