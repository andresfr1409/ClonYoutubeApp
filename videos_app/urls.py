from django.urls import path 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.feed, name='feed'),
    path('buscar_videos/', views.buscar_videos, name='buscar_videos'),
    path('seguir_usuario/<str:username>/', views.seguir_usuario, name='seguir_usuario'),
    path('dejar_de_seguir_usuario/<str:username>/', views.dejar_de_seguir_usuario, name='dejar_de_seguir_usuario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


