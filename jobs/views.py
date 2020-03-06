from django.shortcuts import render
from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects.all()
    print(jobs)
    # for job in jobs.all:
    #     print(job.image_file.url)
    return render(request,'jobs/home.html',{'jobs':jobs})