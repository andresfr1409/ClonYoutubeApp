from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class RegistroForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu Nombre de usuario'}), label='Nombre de usuario')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Tu Email'}), label='Correo electronico')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa una contraseña '}), label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repite tu contraseña'}), label='Contraseña (confirmacion)')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-outline custom-input ', 'id': 'login', 'placeholder': 'Tu Email'}), label='Correo electronico')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-outline custom-input ', 'id': 'login', 'placeholder': 'Ingresa tu contraseña '}), label='Contraseña')
