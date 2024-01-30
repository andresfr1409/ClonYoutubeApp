from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.feed, name='feed'),
    path('perfil/', views.perfil, name = 'perfil'),
    path('subir_video/', views.subir_video, name = 'subir_video'),
    path('ver_video/<int:video_id>/', views.ver_video, name='ver_video'),
    path('editar_video/<int:video_id>/', views.editar_video, name='editar_video'),
    path('editar_perfil/', views.editar_perfil, name = 'editar_perfil'),
    path('eliminar_video/<int:video_id>/', views.eliminar_video, name='eliminar_video'),
    path('buscar_videos/', views.buscar_videos, name='buscar_videos'),
    path('seguir_usuario/<str:username>/', views.seguir_usuario, name='seguir_usuario'),
    path('dejar_de_seguir_usuario/<str:username>/', views.dejar_de_seguir_usuario, name='dejar_de_seguir_usuario'),
    path('perfil_usuario/<str:username>/', views.perfil_usuario, name='perfil_usuario')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


