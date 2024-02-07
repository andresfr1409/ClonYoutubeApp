from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from Autenticacion.forms import RegistroForm, LoginForm
import random

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

def enviar_codigo(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Generar codigo aleatorio de 4 digitos
            codigo = ''.join(random.choices('0123456789', k=4))
            # Guardar el codigo en la sesion del usuario
            request.session['codigo_verificacion'] = codigo
            request.session['email'] = email
            # Envia el codigo al correo electronico del usuario
            send_mail(
                'Codigo de verificacion para restablecer contraseña',
                f'Tu codigo de verificacion es: {codigo}',
                'feliperin14@gmail.com',
                [email],
                fail_silently= False,
            )
            return redirect('ingresar_codigo')
        else:
            messages.error(request, 'El correo electronico proporcionado no esta registrado')
    return render(request, 'Autenticacion/login/enviar_codigo.html')
