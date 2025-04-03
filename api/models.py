from django.db import models

class Plat(models.Model):
    plate = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.plate
