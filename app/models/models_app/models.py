import uuid
from django.db import models

class Driver (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    car_model  = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    username = models.CharField(max_length=50, unique= True)
    birthday = models.DateField(help_text='Format: m/d/yy')
    # id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Product(models.Model):
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    # id = models.IntegerField(primary_key=True)

class Authenticator(models.Model):
    authenticator = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Driver, models.CASCADE, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        driver = Driver.objects.get(id=self.user_id_id)
        return {
            'authenticator': self.authenticator,
            'username': driver.username,
            'first_name': driver.first_name,
            'last_name': driver.last_name,
            'car_model': driver.car_model,
        }

    def __str__(self):
        return ' '.join(map(str, [self.authenticator, self.user_id]))
class Recommand(models.Model):
    item1 = models.IntegerField()
    recommended_items = models.CharField(max_length=50)
