from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newCar', views.new_car, name='new_car'),
    path('cgetAll', views.car_get_all, name='c_get_all'),
    path('csetReserved', views.car_set_reserved, name='c_set_reserved'),
    path('cgetSelect', views.car_get_select, name='c_get_select'),
    path('csetKmAge', views.car_set_km_age, name='c_set_km_age'),
    path('newReservation', views.new_reservation, name='new_reservation'),
    path('rgetAll', views.reservation_get_all, name='r_get_all'),
]