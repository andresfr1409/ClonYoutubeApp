from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from GestionPerfiles.models import CustomUser, User
from videos_app.models import Video, Seguidor
from .forms import UserLoginForm, UserProfileEditForm

@login_required
def perfil(request):
    usuario = request.user
    videos = Video.objects.filter(usuario=usuario).order_by('-fecha_subida')
    cantidad_de_videos = videos.count()
    seguidores = Seguidor.objects.filter(seguido=usuario).count()
    seguidos = Seguidor.objects.filter(seguidor=usuario).count()
    return render(request, 'GestionPerfiles/perfil.html', {'usuario': usuario, 'videos': videos, 'seguidores': seguidores, 'cantidad_de_videos': cantidad_de_videos, 'seguidos': seguidos})

@login_required
def editar_perfil(request):
    usuario = request.user
    try:
        usuario_personalizado = CustomUser.objects.get(user=usuario)
    except CustomUser.DoesNotExist:
        usuario_personalizado = None
    if request.method == 'POST':
        form_usuario = UserLoginForm(request.POST, instance=usuario)
        form_perfil = UserProfileEditForm(request.POST, request.FILES, instance=usuario_personalizado)
        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            if usuario_personalizado is None:
                usuario_personalizado = CustomUser(user=usuario)
            form_perfil = UserProfileEditForm(request.POST, request.FILES, instance=usuario_personalizado)
            form_perfil.save()
            return redirect('perfil')
    else:
        form_usuario = UserLoginForm(instance=usuario)
        form_perfil = UserProfileEditForm(instance=usuario_personalizado)
    
    return render(request, 'GestionPerfiles/editar_perfil.html', {'form_usuario': form_usuario, 'form_perfil': form_perfil})

def perfil_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    videos_usuario = Video.objects.filter(usuario=usuario)
    cantidad_de_videos = videos_usuario.count()
    seguidores = Seguidor.objects.filter(seguido=usuario).count()
    seguidos = Seguidor.objects.filter(seguidor=usuario).count()
    return render(request, 'GestionPerfiles/perfil_usuario.html', {'usuario': usuario, 'videos_usuario': videos_usuario, 'seguidores': seguidores, 'cantidad_de_videos': cantidad_de_videos, 'seguidos': seguidos})
