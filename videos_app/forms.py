from django import forms
from .models import Video,User, CustomUser
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


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video   
        fields = ['titulo', 'descripcion', 'archivo_video']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control custom-textarea'}),
        }

class VideoEditForm(forms.ModelForm):
    class Meta:
        model = Video   
        fields = ['titulo', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control custom-textarea'}),
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-group', 'id': 'EditarEmail'}),
        }

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['imagen_perfil', 'banner']

