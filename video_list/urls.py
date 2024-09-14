# video_processing/urls.py
from django.contrib import admin
from django.urls import path
from video_app import views

urlpatterns = [
    path('info-admin/', admin.site.urls),
    path('upload/', views.video_upload_view, name='video_upload'),
    path('', views.video_list_view, name='video_list'),
    path('videos/<int:video_id>/', views.video_detail_view, name='video_detail'),
]
