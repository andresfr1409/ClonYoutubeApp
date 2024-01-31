from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Seguidor, User
from GestionMultimedia.models import Video

def feed(request):
    videos = Video.objects.all().order_by('-fecha_subida')
    return render(request, 'feed.html', {'videos': videos})

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

def buscar_videos(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        resultados_videos = Video.objects.filter(Q(titulo__icontains=query) | Q(usuario__username__icontains=query))
        resultados_usuarios = User.objects.filter(username__icontains=query)
        return render(request, 'feed.html', {'resultados_videos': resultados_videos, 'resultados_usuarios': resultados_usuarios})
