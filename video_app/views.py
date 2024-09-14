# video_app/views.py
from django.shortcuts import render, redirect
from .models import Video, Subtitle
from .tasks import process_video

# Video upload view 
def video_upload_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        video_file = request.FILES.get('video_file')
        
        video = Video.objects.create(title=title, video_file=video_file)
        process_video.delay(video.id)  # Celery task to process video
        return redirect('video_list')

    return render(request, 'video_upload.html')

# Video list view 
def video_list_view(request):
    videos = Video.objects.all()
    # print(videos,"------------------------21")
    return render(request, 'video_list.html', {'videos': videos})

# Subtitle search and video view
def video_detail_view(request, video_id):
    video = Video.objects.get(id=video_id)
    search_term = request.GET.get('term', '')
    subtitles = Subtitle.objects.filter(video_id=video_id, text__icontains=search_term)
    
    return render(request, 'video_detail.html', {
        'video': video,
        'subtitles': subtitles,
        'search_term': search_term
    })
