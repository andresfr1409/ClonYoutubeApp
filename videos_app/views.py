from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Video, Seguidor, User
from .forms import VideoForm,VideoEditForm

def feed(request):
    videos = Video.objects.all().order_by('-fecha_subida')
    return render(request, 'feed.html', {'videos': videos})

@login_required
def subir_video(request):
    if request.method =='POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.usuario = request.user
            video.save()
            return redirect('perfil')
    else:
        form = VideoForm()
    return render(request, 'subir_video.html', {'form': form})

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

@login_required
def editar_video(request, video_id):
    video = Video.objects.get(id_video=video_id)
    if request.method == 'POST':
        form = VideoEditForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = VideoEditForm(instance=video)
    
    context = {
        'form': form,
        'video': video,
    }
    return render(request, 'editar_video.html', context)

@login_required
def eliminar_video(request, video_id):
    video = Video.objects.get(id_video = video_id)
    video.delete()
    return redirect('perfil')

def ver_video(request, video_id):
    video = get_object_or_404(Video, id_video=video_id)
    return render(request, 'ver_video.html' , {'video': video})

def buscar_videos(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        resultados_videos = Video.objects.filter(Q(titulo__icontains=query) | Q(usuario__username__icontains=query))
        resultados_usuarios = User.objects.filter(username__icontains=query)
        return render(request, 'feed.html', {'resultados_videos': resultados_videos, 'resultados_usuarios': resultados_usuarios})
