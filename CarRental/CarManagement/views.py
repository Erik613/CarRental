from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from CarManagement.models import Car

# Create your views here.

def index(request):
    return HttpResponse("First Response")

@login_required(login_url='/accounts/login/')
def new_car(request):
    car = Car(brand="Audi", model_name="A4", license_plate="BI-EE-1997", seats=4, km_age=250000, construction_date=2006, vehicle_type="SUV", gear_type="1")
    car.save()
    return HttpResponse("Ok: ")

@login_required(login_url='/accounts/login/')
def get_car(request):
    cars = Car.objects.filter(id=1).values()
    return HttpResponse(cars)


    