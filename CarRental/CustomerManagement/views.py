import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from CustomerManagement.models import Customer
from CustomerManagement.forms import CustomerEntryForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def new_customer(request):
    if request.method == 'GET':
            form = CustomerEntryForm()
            return render(request, 'EntryCustomer.html', {'form': form})
        else:
            form = CustomerEntryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('get_customer', pk=form.instance.pk)
            else:
                return HttpResponse('<h1>Fehler</h1>' , status=500)


def update(request): # möglichkeit jeden wert anzupassen
    customer = Customer.objects.get(id=1)
    customer.first_name = "bla"
    customer.save()
    return HttpResponse("Updated")

@login_required(login_url='/accounts/login/')
def customer_get_all(request):
    customer = Customer.objects.values()
    return HttpResponse(customer)

def customer_get_select(request):
    customer = Customer.objects.filter(id=1).values()
    return HttpResponse(customer)

def get_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        return HttpResponse(customer)
    except Customer.DoesNotExist:
        return HttpResponseNotFound('<h1>Not Found</h1>')
