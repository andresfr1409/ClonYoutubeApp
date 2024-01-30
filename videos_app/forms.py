from django import forms
from .models import Video,User, CustomUser
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

