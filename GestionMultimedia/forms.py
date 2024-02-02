from django import forms
from GestionMultimedia.models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video   
        fields = ['titulo', 'descripcion', 'archivo_video']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'FormVideo','placeholder': 'Ingresa el título'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control custom-textarea', 'id': 'FormVideo', 'placeholder': 'Ingresa la descripción'}),
            'archivo_video': forms.ClearableFileInput(attrs={'class': 'form-control custom-file-input', 'id': 'FormVideo'}),
        }

class VideoEditForm(forms.ModelForm):
    class Meta:
        model = Video   
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'FormVideo','placeholder': 'Ingresa el título'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control custom-textarea', 'id': 'FormVideo', 'placeholder': 'Ingresa la descripción'}),
        }