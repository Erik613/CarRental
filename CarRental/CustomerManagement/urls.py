from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add', login_required(views.CustomerFormView.as_view()), name='add_customer'),
    path('getAll', login_required(views.CustomerListView.as_view()), name='get_all_customer'),
    path('get/<int:pk>', login_required(views.CustomerFormView.as_view()), name='get_customer'),
    
]
