from django.db import models
from ckeditor.fields import RichTextField

class CrearDemonio(models.Model):
    nombre = models.CharField(null=True, max_length=30)
    simbolo = models.CharField(null=True, max_length=30)
    origen = models.CharField(null=True, max_length=30)
    reseña = RichTextField(null=True)
    fecha_creacion = models.DateField(null=True)
    autor = models.CharField(null=True, max_length=30)
    
    def __str__(self):
        return f"Demonio: {self.nombre}, simbolo: {self.simbolo}"