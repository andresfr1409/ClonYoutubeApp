from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from GestionMultimedia.models import Video
from GestionMultimedia.forms import VideoForm, VideoEditForm

@login_required
def subir_video(request):
    if request.method =='POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.usuario = request.user
            video.save()
            return redirect('perfil')
    else:
        form = VideoForm()
    return render(request, 'subir_video.html', {'form': form})

@login_required
def editar_video(request, video_id):
    video = Video.objects.get(id_video=video_id)
    if request.method == 'POST':
        form = VideoEditForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = VideoEditForm(instance=video)
    
    context = {
        'form': form,
        'video': video,
    }
    return render(request, 'editar_video.html', context)

@login_required
def eliminar_video(request, video_id):
    video = Video.objects.get(id_video = video_id)
    video.delete()
    return redirect('perfil')

def ver_video(request, video_id):
    video = get_object_or_404(Video, id_video=video_id)
    return render(request, 'ver_video.html' , {'video': video})


