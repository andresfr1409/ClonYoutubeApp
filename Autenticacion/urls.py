from django.urls import path 
from Autenticacion import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('iniciar_sesion/', views.iniciar_sesion, name = 'iniciar_sesion'),
    path('login/', auth_views.LoginView.as_view(template_name='inicio_sesion.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'feed'), name='logout'),
    path('restablecer_contraseña/', views.restablecer_contraseña, name='restablecer_contraseña'),
]
