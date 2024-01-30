from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from Autenticacion.forms import RegistroForm, LoginForm

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
    return render(request, 'Autenticacion/registro_usuario/registro.html', {'form': form})

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
    return render(request, 'Autenticacion/login/inicio_sesion.html', {'form': form})

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
    return render(request, 'Autenticacion/login/restablecer_contraseña.html')
