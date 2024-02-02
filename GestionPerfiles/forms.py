from django import forms
from GestionPerfiles.models import User, CustomUser

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'FormPerfil'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-input', 'id': 'FormPerfil'}),
        }

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['imagen_perfil', 'banner']
        
        widgets = {
            'imagen_perfil': forms.ClearableFileInput(attrs={'class': 'form-control custom-file-input', 'id': 'FormPerfil', 'accept': 'image/*'}),
            'banner': forms.ClearableFileInput(attrs={'class': 'form-control custom-file-input','id': 'FormPerfil', 'accept': 'image/*'}),
        }