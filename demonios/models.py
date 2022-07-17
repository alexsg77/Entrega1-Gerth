from django.db import models

class CrearDemonio(models.Model):
    nombre = models.CharField(null=True, max_length=30)
    simbolo = models.CharField(null=True, max_length=30)
    origen = models.CharField(null=True, max_length=30)
    reseña = models.CharField(null=True, max_length=300)
    def __str__(self):
        return f"Demonio: {self.nombre}, simbolo: {self.simbolo}"