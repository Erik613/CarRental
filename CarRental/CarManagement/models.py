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

    def __str__(self):
        return ('brand: ' + self.brand + ", model_name: " + self.model_name + ", license_plate: " + self.license_plate +
        ', seats: ' + str(self.seats) + ", km_age: " + str(self.km_age) + ", construction_date: " + str(self.construction_date) +
        ", vehicle_type: " + self.vehicle_type + ", gear_type: " + self.gear_type)


class Reservation(models.Model):
    id_user = models.CharField(max_length=50)
    car_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    sec_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    residence_street = models.CharField(max_length=50)
    residence_number = models.CharField(max_length=50)
    residence_city = models.CharField(max_length=50)

    
    

