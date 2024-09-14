from celery import shared_task
import subprocess
from .models import Video
import os

@shared_task
def process_video(video_id):
    video = Video.objects.get(id=video_id)
    subtitle_path = f"{os.path.splitext(video.video_file.path)[0]}.srt"
    command = f"ffmpeg -i {video.video_file.path} -map 0:s:0 {subtitle_path}"
    
    # Run command
    subprocess.run(command, shell=True)

    # Save subtitle file path
    video.subtitle_file = subtitle_path
    video.save()

    return subtitle_path
