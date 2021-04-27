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
    

    
