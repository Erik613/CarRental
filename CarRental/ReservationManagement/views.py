from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from ReservationManagement.models import Reservation
from ReservationManagement.forms import ReservationForm

# Create your views here.

def new_reservation(request):
    if request.method == 'GET':
        form = ReservationForm()
        return render(request, 'EntryReservation.html', {'form': form})
    else:
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_reservation', pk=form.instance.pk)
        else:
            return render(request, 'EntryReservation.html', {'form': form})

def get(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
        return HttpResponse(reservation)
    except Car.DoesNotExist:
        return HttpResponseNotFound('<h1>Not Found</h1>')


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
