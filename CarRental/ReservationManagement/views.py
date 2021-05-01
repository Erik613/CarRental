from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from ReservationManagement.models import Reservation
from ReservationManagement.forms import ReservationForm

# Create your views here.

class ReservationFormView(FormView):
    form_class = ReservationForm
    template_name = 'form.html'
    pk = None

    def get_success_url(self):
        return reverse('get_reservation', kwargs={'pk': self.pk})

    def form_valid(self, form):
        form = form.save()
        self.pk = form.pk
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.add_error(None, 'Ups, da ist etwas schiefgelaufen')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ReservationFormView, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Reservierung hinzufügen'
        return context

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
