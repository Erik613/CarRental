from django.db import models

# Create your models here.

verhicle_types = (
    ('SUV', 'SUV'), 
    ('LIMOSINE', 'Limosine'), 
    ('COMBI', 'Combi'),
    ('KLEINWAGEN', 'Kleinwagen'),
)

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=250)
    license_plate = models.CharField(max_length=50)
    seats = models.IntegerField()
    km_age = models.IntegerField()
    construction_date = models.SmallIntegerField()
    vehicle_type = models.CharField(max_length=100, default='SUV', choices=verhicle_types)     #SUV, Limosine, etc...
    is_automatic = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return ('brand: ' + self.brand + ", model_name: " + self.model_name + ", license_plate: " + self.license_plate +
        ', seats: ' + str(self.seats) + ", km_age: " + str(self.km_age) + ", construction_date: " + str(self.construction_date) +
        ", vehicle_type: " + self.vehicle_type + ", is_automatic: " + str(self.is_automatic))






    
    

