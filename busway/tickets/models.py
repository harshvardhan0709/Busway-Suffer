from django.db import models

# Create your models here.
class Ticket(models.Model):
    username = models.CharField(max_length=120)
    vehicle_type = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    parking_address = models.CharField(max_length=120)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
