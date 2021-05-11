from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    residence_street = models.CharField(max_length=50)
    post_code = models.IntegerField()
    residence_city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.birth_date}"