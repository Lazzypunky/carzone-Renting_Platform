from pages.models import Team
from django.shortcuts import render
from cars.models import Car

# Create your views here.
def homepage(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured = True)
    latest_cars = Car.objects.all().order_by('-created_date')
    context = {
        'teams': teams ,
        'featured_cars' : featured_cars,
        'latest_cars' : latest_cars,
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