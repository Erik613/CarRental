from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add', login_required(views.ReservationFormView.as_view()), name='add_reservation'),
    path('get/<int:pk>', views.get, name='get_reservation'),
    path('test', views.test),
]
