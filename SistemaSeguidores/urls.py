from django.urls import path 
from SistemaSeguidores import views

urlpatterns = [
    path('seguir_usuario/<str:username>/', views.seguir_usuario, name='seguir_usuario'),
    path('dejar_de_seguir_usuario/<str:username>/', views.dejar_de_seguir_usuario, name='dejar_de_seguir_usuario'),
]
