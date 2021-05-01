from django.urls import path
from django.contrib.auth.decorators import login_required

from CarManagement import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', login_required(views.CarFormView.as_view()), name='add_car'),
    path('getAll', login_required(views.CarListView.as_view()), name='c_get_all'),
    path('setReserved', views.car_set_reserved, name='c_set_reserved'),
    path('setKmAge', views.car_set_km_age, name='c_set_km_age'),
    path('update', views.update, name='r_get_all'),
    path('getCar/<int:pk>', views.get_car, name='get_car'),

]