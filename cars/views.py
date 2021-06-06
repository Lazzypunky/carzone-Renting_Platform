from cars.models import Car
from django.shortcuts import render

# Create your views here.
def cars(request):
    cars = Car.objects.all()
    data = {
        'cars':cars
    }
    return render (request , 'cars/cars.html',data)