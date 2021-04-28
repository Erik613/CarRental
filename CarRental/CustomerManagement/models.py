from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    sec_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    residence_street = models.CharField(max_length=50)
    residence_number = models.CharField(max_length=50)
    residence_city = models.CharField(max_length=50)