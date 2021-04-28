from django.db import models
from CustomerManagement.models import Customer
from CarManagement.models import Car

# Create your models here.

class Reservation(models.Model):
    id_customer= models.ForeignKey(Customer, on_delete=models.RESTRICT)
    id_car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    start_date = models.DateField()
    end_date = models.DateField()