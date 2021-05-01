from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add', login_required(views.CustomerFormView.as_view()), name='add_customer'),
    path('get/<int:pk>', views.get, name='get_customer'),
    
]
