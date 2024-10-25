from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from orders.models import Order
from .forms import FormularioRegistro, FormularioPerfil, FormularioLogin, FormularioEdicionUsuario, FormularioEdicionPerfil
from .models import Perfil


class VistaRegistro(View):
    def get(self, request):
        formulario = FormularioRegistro()
        formulario_foto = FormularioPerfil()
        return render(request, 'registration/register.html', {'form': formulario, 'foto': formulario_foto})

    def post(self, request):
        formulario = FormularioRegistro(request.POST)
        formulario_foto = FormularioPerfil(request.POST, request.FILES)
        if formulario.is_valid() and formulario_foto.is_valid():
            nuevo_usuario = formulario.save(commit=False)
            nuevo_usuario.save()
            perfil = Perfil.objects.create(usuario=nuevo_usuario)
            avatar = request.FILES.get('foto')
            if avatar:
                perfil.foto = avatar
            perfil.save()

            usuario = authenticate(
                username=formulario.cleaned_data['username'],
                password=formulario.cleaned_data['contraseña']
            )

            login(request, usuario)
            return redirect('shop:product_list')


class VistaLogin(View):
    def get(self, request):
        formulario = FormularioLogin()
        return render(request, 'registration/login.html', {'form': formulario})

    def post(self, request):
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            nombre_de_usuario = formulario.cleaned_data['nombre_de_usuario']
            contraseña = formulario.cleaned_data['contraseña']
            usuario_login = authenticate(username=nombre_de_usuario, password=contraseña)
            if usuario_login:
                login(request, usuario_login)
                return redirect('shop:product_list')
        return render(request, 'registration/login.html', {'form': formulario})


class VistaEdicion(View):
    @login_required
    def get(self, request):
        formulario_usuario = FormularioEdicionUsuario(instance=request.user)
        formulario_perfil = FormularioEdicionPerfil(instance=request.user.perfil)
        return render(request, 'registration/edit.html', {'form_usuario': formulario_usuario, 'form_perfil': formulario_perfil})

    @login_required
    def post(self, request):
        formulario_usuario = FormularioEdicionUsuario(instance=request.user, data=request.POST)
        formulario_perfil = FormularioEdicionPerfil(instance=request.user.perfil, data=request.POST, files=request.FILES)
        if formulario_usuario.is_valid() and formulario_perfil.is_valid():
            usuario_cambiado = formulario_usuario.save(commit=False)
            usuario_cambiado.save()
            perfil = Perfil.objects.get(usuario=usuario_cambiado)
            avatar = request.FILES.get('foto')
            if avatar:
                perfil.foto = avatar
            formulario_perfil.save()
            return redirect('shop:product_list')


class VistaCuenta(View):
    @login_required
    def get(self, request):
        orden = Order.objects.filter(user=request.user).order_by('-id')
        return render(request, 'registration/account.html', {'orden': orden})
