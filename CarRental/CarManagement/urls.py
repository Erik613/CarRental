from django.urls import path
from django.contrib.auth.decorators import login_required

from CarManagement import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', login_required(views.CarFormView.as_view()), name='add_car'),
    path('getAll', login_required(views.CarListView.as_view()), name='c_get_all'),
    path('get/<int:pk>', login_required(views.CarFormView.as_view()), name='get_car'),

]