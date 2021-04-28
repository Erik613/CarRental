from django.urls import path

from CarManagement import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_car, name='new_car'),
    path('getAll', views.car_get_all, name='c_get_all'),
    path('setReserved', views.car_set_reserved, name='c_set_reserved'),
    path('getSelect', views.car_get_select, name='c_get_select'),
    path('setKmAge', views.car_set_km_age, name='c_set_km_age'),
    path('update', views.update, name='r_get_all'),
    path('getCar/<int:pk>', views.get_car, name='get_car'),

]