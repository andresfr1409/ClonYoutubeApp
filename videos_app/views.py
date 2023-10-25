from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Video, Seguidor, CustomUser, User
from .forms import VideoForm, RegistroForm, LoginForm, VideoEditForm, UserLoginForm, UserProfileEditForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email'] 
            user.save()
            login(request, user)
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'login/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil')
            else:
                form.add_error(None, 'Credenciales invalidas. por favor, verifica tu correo electronico y contraseña')
    else:
        form = LoginForm()
    return render(request, 'login/inicio_sesion.html', {'form': form})

def feed(request):
    videos = Video.objects.all().order_by('-fecha_subida')
    return render(request, 'feed.html', {'videos': videos})

@login_required
def perfil(request):
    usuario = request.user
    videos = Video.objects.filter(usuario=usuario).order_by('-fecha_subida')
    cantidad_de_videos = videos.count()
    seguidores = Seguidor.objects.filter(seguido=usuario).count()
    seguidos = Seguidor.objects.filter(seguidor=usuario).count()
    return render(request, 'perfil.html', {'usuario': usuario, 'videos': videos, 'seguidores': seguidores, 'cantidad_de_videos': cantidad_de_videos, 'seguidos': seguidos})

def perfil_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    videos_usuario = Video.objects.filter(usuario=usuario)
    cantidad_de_videos = videos_usuario.count()
    seguidores = Seguidor.objects.filter(seguido=usuario).count()
    seguidos = Seguidor.objects.filter(seguidor=usuario).count()
    return render(request, 'perfil_usuario.html', {'usuario': usuario, 'videos_usuario': videos_usuario, 'seguidores': seguidores, 'cantidad_de_videos': cantidad_de_videos, 'seguidos': seguidos})

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
    
    return render(request, 'editar_perfil.html', {'form_usuario': form_usuario, 'form_perfil': form_perfil})

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

def restablecer_contraseña(request):
    User = get_user_model()
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        try:
            user = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
        except User.DoesNotExist:
            messages.error(request, 'Usuario no encontrado, Intentalo nuevamente .')
            return redirect('restablecer_contraseña')
        if new_password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden, Intentalo nuevamente.')
            return redirect('restablecer_contraseña')
        # Cambiar la contraseña del usuario
        user.password = make_password(new_password)
        user.save()
        messages.success(request, 'La contraseña se cambió con éxito. Ahora puedes iniciar sesión con tu nueva contraseña.')
        return redirect('restablecer_contraseña')
    return render(request, 'login/restablecer_contraseña.html')