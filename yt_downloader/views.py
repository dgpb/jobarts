from django.shortcuts import render

# Create your views here.

def ytb(request):
    return render(request, 'yt_downloader/ytb.html')
