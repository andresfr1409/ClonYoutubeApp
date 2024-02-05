from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(upload_to='images/', blank=True, null=True)
    banner = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
