from . import views
from django.urls import path, include

urlpatterns = [
    path('new', views.new_reservation),
    path('get/<int:pk>', views.get, name='get_reservation'),
    path('test', views.test),
]
