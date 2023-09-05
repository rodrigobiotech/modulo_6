from django.shortcuts import redirect, render
from .forms import UsuarioForm

from .models import Usuario




def vista_index(request):
    return render(request, 'index.html') 

def vista_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {
        'usuarios' : usuarios
    }

    return render(request, 'usuarios.html', contexto)

def vista_registroUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        
           
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})