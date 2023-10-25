from django.contrib import admin
from .models import Video, Seguidor, CustomUser


admin.site.register(Video)
admin.site.register(Seguidor)
admin.site.register(CustomUser)