from django import forms
from .models import Video
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

