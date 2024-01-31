from django.db import models
from django.contrib.auth.models import User

class Seguidor(models.Model):
    id_seguidor = models.AutoField(primary_key= True)
    seguidor = models.ForeignKey(User, related_name='seguidor', on_delete=models.CASCADE)
    seguido = models.ForeignKey(User, related_name='seguido', on_delete=models.CASCADE)
    fecha_seguimiento = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.seguidor