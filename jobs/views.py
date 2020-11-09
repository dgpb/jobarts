from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'jobs/index.html')

def jobs(request):
    return render(request, 'jobs/jobs.html')

def detail(request):
    return render(request, 'jobs/detail.html')
