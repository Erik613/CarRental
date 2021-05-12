import datetime
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from CarManagement.models import Car
from CarManagement.forms import CarEntryForm

# Create your views here.


class CarFormView(generic.FormView):
    form_class = CarEntryForm
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
        context = super(CarFormView, self).get_context_data(**kwargs)
        if "pk" in self.kwargs:
            context['pagetitle'] = 'Auto bearbeiten'
        else:
            context['pagetitle'] = 'Auto hinzufügen'
        add_nav_context(context)
        return context
    
    def get_form_kwargs(self):
        form_kwargs = super(CarFormView, self).get_form_kwargs()
        if 'pk' in self.kwargs:
            form_kwargs['instance'] = Car.objects.get(pk=int(self.kwargs['pk']))
        return form_kwargs

class CarListView(generic.ListView):
    model = Car
    context_object_name = "car_list"
    template_name = "carListView.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_nav_context(context)
        return context
    

class CarDetailView(generic.DetailView):
    model = Car

def index(request):
    return HttpResponse("First Response")

def update(request): # möglichkeit jeden wert anzupassen
    car = Car.objects.get(id=1)
    car.model_name = "bla"
    car.save()
    return HttpResponse("Updated")

def add_nav_context(context):
    context["nav"] = "car"

'''
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
'''
@login_required(login_url='/accounts/login/')
def car_get_all(request):
    cars = Car.objects.values()
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

