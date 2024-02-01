from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from GestionMultimedia.models import Video

def feed(request):
    videos = Video.objects.all().order_by('-fecha_subida')
    return render(request, 'feed.html', {'videos': videos})

def buscar_videos(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        resultados_videos = Video.objects.filter(Q(titulo__icontains=query) | Q(usuario__username__icontains=query))
        resultados_usuarios = User.objects.filter(username__icontains=query)
        return render(request, 'feed.html', {'resultados_videos': resultados_videos, 'resultados_usuarios': resultados_usuarios})
