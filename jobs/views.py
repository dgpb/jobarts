from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.
def home(request):
    jobs = Job.objects.all()[:5]
    return render(request, 'jobs/index.html', {'jobs' : jobs})

def jobs(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 10)
    page = request.GET.get('page')

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'jobs/jobs.html', {'page' : page, 'jobs' : jobs})

def detail(request, pk):
    jobs = Job.objects.get(id=pk)

    context = {'jobs' : jobs}

    return render(request, 'jobs/detail.html', context)
