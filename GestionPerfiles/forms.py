from django import forms
from GestionPerfiles.models import User, CustomUser

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