from . import views
from django.urls import path, include

urlpatterns = [
    path('add', views.CustomerFormView.as_view(), name='add_customer'),
    path('get/<int:pk>', views.get, name='get_customer'),
    
]
