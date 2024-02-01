from django.urls import path 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.feed, name='feed'),
    path('buscar_videos/', views.buscar_videos, name='buscar_videos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


