from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def overview(request): 
    return render (request,'student/overview.html')

def projects(request):
    return render (request,'student/projects.html')

def cohort(request):
    return render (request,'student/cohort.html')