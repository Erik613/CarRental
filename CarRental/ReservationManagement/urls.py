from . import views
from django.urls import path, include

urlpatterns = [
    path('add', views.ReservationFormView.as_view(), name='add_reservation'),
    path('get/<int:pk>', views.get, name='get_reservation'),
    path('test', views.test),
]
