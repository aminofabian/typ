from django.db import models

class Trip(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} in {self.duration} minutes for Kes{self.price}"
