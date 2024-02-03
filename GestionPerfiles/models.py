from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(upload_to='images/', blank=True, null=True)
    banner = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    def delete(self, using=None, keep_parents=False):
        if self.imagen_perfil:
            self.imagen_perfil.storage.delete(self.imagen_perfil.name)
        if self.banner:
            self.banner.storage.delete(self.banner.name)
        super().delete(using=using, keep_parents=keep_parents)
