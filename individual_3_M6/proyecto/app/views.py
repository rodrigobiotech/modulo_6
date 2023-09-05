from django.shortcuts import render
from .models import Usuario


def vista_index(request):
    return render(request, 'index.html') 

def vista_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {
        'usuarios' : usuarios
    }

    return render(request, 'usuarios.html', contexto)