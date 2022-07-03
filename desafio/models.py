from django.db import models

# Create your models here.

class Prueba(models.Model):
    nombre = models.CharField(max_length=30)
    simbolo = models.CharField(max_length=30)
    origen = models.CharField(max_length=30)
    fecha = models.DateField(null=True)