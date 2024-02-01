from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from SistemaSeguidores.models import Seguidor, User

def seguir_usuario(request, username):
    usuario_a_seguir = get_object_or_404(User, username=username)
    if request.user.is_authenticated:
        if request.user != usuario_a_seguir and not request.user.seguidor.filter(seguido=usuario_a_seguir).exists():
            Seguidor.objects.create(seguidor=request.user, seguido=usuario_a_seguir)
            messages.success(request, f'Has comenzado a seguir a {username}.')
        else:
            messages.warning(request, 'Ya sigues a este usuario')
    else:
        messages.warning(request, 'Debes iniciar sesión o registrarte')
    return redirect('perfil_usuario', username=username)

def dejar_de_seguir_usuario(request, username):
    usuario_a_dejar_de_seguir = get_object_or_404(User, username=username)
    
    if request.user.is_authenticated:
        if request.user != usuario_a_dejar_de_seguir and request.user.seguidor.filter(seguido=usuario_a_dejar_de_seguir).exists():
            request.user.seguidor.filter(seguido=usuario_a_dejar_de_seguir).delete()
            messages.success(request, f'Has dejado de seguir a {username}' )
        else:
            messages.warning(request, 'No sigues a este usuario')
    else:
        messages.warning(request, 'Debes iniciar sesión o registrarte')
    return redirect('perfil_usuario', username=username)
