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

    def __str__(self):
        return f"{self.brand} - {self.model_name} - ({self.license_plate})"
        






    
    

