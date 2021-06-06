from pages.models import Team
from django.shortcuts import render

# Create your views here.
def homepage(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render (request , 'pages/home.html',context)

def contact(request):
    return render(request , 'pages/contact.html')

def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request , 'pages/about.html',context)

def service(request):
    return render(request , 'pages/service.html')