# video_app/models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    subtitle_file = models.FileField(upload_to='subtitles/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    start_time = models.FloatField()  # In seconds
    end_time = models.FloatField()
