from django.db import models

# Create your models here.

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=35)
    edad = models.PositiveBigIntegerField()
    nacimiento = models.DateTimeField()

        