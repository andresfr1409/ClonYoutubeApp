from django.urls import path 
from GestionMultimedia import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('subir_video/', views.subir_video, name = 'subir_video'),
    path('ver_video/<int:video_id>/', views.ver_video, name='ver_video'),
    path('editar_video/<int:video_id>/', views.editar_video, name='editar_video'),
    path('eliminar_video/<int:video_id>/', views.eliminar_video, name='eliminar_video'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
