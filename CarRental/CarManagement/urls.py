from django.urls import path

from CarManagement import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newCar', views.new_car, name='new_car'),
    path('getCar', views.get_car, name='get_car'),
]