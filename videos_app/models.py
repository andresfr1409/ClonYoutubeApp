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

class Seguidor(models.Model):
    id_seguidor = models.AutoField(primary_key= True)
    seguidor = models.ForeignKey(User, related_name='seguidor', on_delete=models.CASCADE)
    seguido = models.ForeignKey(User, related_name='seguido', on_delete=models.CASCADE)
    fecha_seguimiento = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.seguidor

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(upload_to='images/', blank=True, null=True)
    banner = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.user.username