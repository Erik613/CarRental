from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from ReservationManagement.models import Reservation

# Create your views here.

def new_reservation(request):
    reservation = Reservation()
    reservation.save()
    return HttpResponse("new customer")

def car_set_reserved(request):
    reservation = Reservation.objects.get(id=1)
    reservation.reserved = True
    reservation.save()
    return HttpResponse("Car is now reserved")

def update(request): # möglichkeit jeden wert anzupassen
    reservation = Reservation.objects.get(id=1)
    reservation.save()
    return HttpResponse("Updated")

def test(request):
    return render(request, 'EntryReservation.html')