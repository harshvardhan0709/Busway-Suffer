from django.db import models

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)


class Parking_capacity(models.Model):
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    car_capacity = models.CharField(max_length=120)
    bike_capacity = models.CharField(max_length=120)
