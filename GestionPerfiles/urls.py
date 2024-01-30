from django.urls import path 
from GestionPerfiles import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('perfil/', views.perfil, name = 'perfil'),
    path('editar_perfil/', views.editar_perfil, name = 'editar_perfil'),
    path('perfil_usuario/<str:username>/', views.perfil_usuario, name='perfil_usuario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
