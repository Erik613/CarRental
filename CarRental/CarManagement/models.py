from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=250)
    license_plate = models.CharField(max_length=50)
    seats = models.IntegerField()
    km_age = models.IntegerField()
    construction_date = models.SmallIntegerField()
    vehicle_type = models.CharField(max_length=100)     #SUV, Limosine, etc...
    gear_type = models.CharField(max_length=50)
    reserved = models.BooleanField(default=False)

class Reservation(models.Model):
    id_user = models.CharField(max_length=50)
    car_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()