
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('yt_downloader', include('yt_downloader.urls')),
]
