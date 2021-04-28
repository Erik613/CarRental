import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from CarManagement.models import Car
from CarManagement.forms import CarEntryForm

# Create your views here.


def index(request):
    return render(request, 'EntryCar.html')

def update(request): # möglichkeit jeden wert anzupassen
    car = Car.objects.get(id=1)
    car.model_name = "bla"
    car.save()
    return HttpResponse("Updated")

@login_required(login_url='/accounts/login/')
def new_car(request):
    if request.method == 'GET':
        form = CarEntryForm()
        return render(request, 'EntryCar.html', {'form': form})
    else:
        form = CarEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_car', pk=form.instance.pk)
        else:
            return HttpResponse('<h1>Fehler</h1>' , status=500)

@login_required(login_url='/accounts/login/')
def car_get_all(request):
    cars = Car.objects.values()
    return HttpResponse(cars)

def car_get_select(request):
    cars = Car.objects.filter(id=1).values()
    return HttpResponse(cars)

def get_car(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        return HttpResponse(car)
    except Car.DoesNotExist:
        return HttpResponseNotFound('<h1>Not Found</h1>')

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

