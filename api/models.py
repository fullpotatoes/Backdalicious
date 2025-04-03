from django.db import models


class Plat(models.Model):
    plate = models.CharField(max_length=100, default="Nom inconnu")
    description = models.TextField(default="Aucune description fournie")
    image = models.CharField(max_length=100, default="Image inconnue")

    def __str__(self):
        return self.plate
