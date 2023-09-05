from django.urls import path

from app.views import vista_index, vista_usuarios, vista_registroUsuario

urlpatterns = [
    path('', vista_index, name='index'),
    path('usuarios/', vista_usuarios, name='usuarios'),
    path('registroUsuario/', vista_registroUsuario, name='registroUsuario'),
]