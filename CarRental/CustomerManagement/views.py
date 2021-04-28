import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from CustomerManagement.models import Customer

# Create your views here.

def new_customer(request):
    customer = Customer(first_name="Patrick", sec_name="Matern", birth_date=(datetime.date(1997, 4, 9)),
                         residence_street="Test Str", residence_number="69", residence_city="Bielefeld")
    customer.save()
    return HttpResponse("new customer")

def update(request): # möglichkeit jeden wert anzupassen
    customer = Customer.objects.get(id=1)
    customer.first_name = "bla"
    customer.save()
    return HttpResponse("Updated")
