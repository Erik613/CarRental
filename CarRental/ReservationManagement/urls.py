from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add', login_required(views.ReservationFormView.as_view()), name='add_reservation'),
    path('getAll', login_required(views.ReservationListView.as_view()), name='get_all_reservation'),
    path('get/<int:pk>', login_required(views.ReservationUpdateView.as_view()), name='get_reservation'),
    path('test', views.test),
]
