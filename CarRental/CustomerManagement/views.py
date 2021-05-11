import datetime
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Customer
from .forms import CustomerForm

# Create your views here.

class CustomerFormView(generic.FormView):
    form_class = CustomerForm
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
        context = super(CustomerFormView, self).get_context_data(**kwargs)
        if "pk" in self.kwargs:
            context['pagetitle'] = 'Kunden bearbeiten'
        else:
            context['pagetitle'] = 'Kunden hinzufügen'
        return context

    def get_form_kwargs(self):
        form_kwargs = super(CustomerFormView, self).get_form_kwargs()
        if 'pk' in self.kwargs:
            form_kwargs['instance'] = Customer.objects.get(pk=int(self.kwargs['pk']))
        return form_kwargs




class CustomerListView(generic.ListView):
    model = Customer
    context_object_name = "customer_list"
    template_name = "customerListView.html"

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


