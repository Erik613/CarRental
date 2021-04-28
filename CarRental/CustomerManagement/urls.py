from . import views
from django.urls import path, include

urlpatterns = [
    path('new', views.new_customer),
    
]
