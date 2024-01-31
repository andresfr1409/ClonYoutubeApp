from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    id_video = models.AutoField(primary_key= True)
    titulo = models.CharField(max_length=100, null=True)
    descripcion = models.TextField()
    archivo_video = models.FileField(upload_to='videos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
