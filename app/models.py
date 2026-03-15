from django.db import models
from django.utils import timezone
import random

class Parcel(models.Model):
    tracking_number = models.CharField(max_length=11, unique=True)
    departure_address = models.CharField(max_length=255)
    arrival_address = models.CharField(max_length=255)
    weight = models.IntegerField()
    status = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = 'TRK' + random.randint(100000000, 999999999).__str__()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Colis n°{self.id} - {self.weight}kg"

# Create your models here.
