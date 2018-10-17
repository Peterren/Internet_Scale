
from django.db import models

class Driver (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    car_model  = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    def __str__(self):
        return self.first_name+" "+self.last_name


