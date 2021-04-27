import datetime

from django.shortcuts import render
from django.http import HttpResponse
from CarManagement.models import Car
from CarManagement.models import Reservation
from CarManagement.models import Customers

# Create your views here.


def index(request):
    return HttpResponse("First Response")

def update(request): # möglichkeit jeden wert anzupassen
    car = Car.objects.get(id=1)
    car.model_name = "bla"
    car.save()
    return HttpResponse("Updated")

def new_car(request):
    car = Car(brand="BMW", model_name="A4", license_plate="BI-EE-1997", seats=4, km_age=250000, construction_date=2006,
              vehicle_type="SUV", gear_type="1")
    car.save()
    return HttpResponse("Ok: ")

def car_get_all(request):
    cars = Car.objects.values()
    return HttpResponse(cars)

def car_get_select(request):
    cars = Car.objects.filter(id=1).values()
    return HttpResponse(cars)

def car_set_reserved(request):
    car = Car.objects.get(id=1)
    car.reserved = True
    car.save()
    return HttpResponse("Car is now reserved")

def car_set_km_age(request):
    car = Car.objects.get(id=1)
    car.km_age = 1000
    car.save()
    return HttpResponse("Cars km_age changed")

def new_reservation(requests):
    reservation = Reservation(id_user="test", car_id="1", start_date=datetime.datetime.now(),
                              end_date=datetime.datetime.now())
    reservation.save()
    return HttpResponse("OK: ")

def reservation_get_all(request):
    reservation = Reservation.objects.values()
    return HttpResponse(reservation)

def new_customer(request):
    customer = Customers(first_name="Patrick", sec_name="Matern", birth_date=(datetime.date(1997, 4, 9)),
                         residence_street="Test Str", residence_number="69", residence_city="Bielefeld")
