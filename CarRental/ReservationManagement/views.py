from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.views import generic
from ReservationManagement.models import Reservation
from CarManagement.models import Car
from CustomerManagement.models import Customer
from ReservationManagement.forms import ReservationForm, ReservationUpdateForm

# Create your views here.

class ReservationFormView(generic.FormView):
    form_class = ReservationForm
    template_name = 'form.html'
    pk = None

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form = form.save()
        self.pk = form.pk
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.add_error(None, 'Ups, da ist etwas schiefgelaufen')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ReservationFormView, self).get_context_data(**kwargs)
        if "pk" in self.kwargs:
            context['pagetitle'] = 'Reservierung bearbeiten'
        else:
            context['pagetitle'] = 'Reservierung hinzufügen'
        add_nav_context(context)
        return context


class ReservationUpdateView(generic.edit.UpdateView):
    template_name = "form.html"
    model = Reservation
    form_class = ReservationUpdateForm

    def get_context_data(self, **kwargs):
        context = super(ReservationUpdateView, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Reservierung bearbeiten'
        add_nav_context(context)
        return context

class ReservationListView(generic.ListView):
    model = Reservation
    context_object_name = "reservation_list"
    template_name = "reservationListView.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_nav_context(context) 
        return context
    

def add_nav_context(context):
    context["nav"] = "reservation"
