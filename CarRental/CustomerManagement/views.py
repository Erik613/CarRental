import datetime
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from CustomerManagement.models import Customer
from .forms import CustomerForm

# Create your views here.

class CustomerFormView(FormView):
    form_class = CustomerForm
    template_name = 'form.html'
    pk = None

    def get_success_url(self):
        return reverse('get_car', kwargs={'pk': self.pk})

    def form_valid(self, form):
        form = form.save()
        self.pk = form.pk
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.add_error('Ups, da ist etwas schiefgelaufen')
    
    def get_context_data(self, **kwargs):
        context = super(CustomerFormView, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Kunden hinzufügen'
        return context

def get(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        return HttpResponse(customer)
    except:
        HttpResponseNotFound("<h1>Not Found</h1>")

def update(request): # möglichkeit jeden wert anzupassen
    customer = Customer.objects.get(id=1)
    customer.first_name = "bla"
    customer.save()
    return HttpResponse("Updated")


