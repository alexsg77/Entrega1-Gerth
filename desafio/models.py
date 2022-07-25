from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class DiosGriego(models.Model):
    nombre = models.CharField(max_length=30)
    simbolo = models.CharField(max_length=30)
    origen = models.CharField(max_length=30)
    reseña = models.CharField(max_length=1000)
    
class DiosRomano(models.Model):
    nombre = models.CharField(max_length=30)
    simbolo = models.CharField(max_length=30)
    origen = models.CharField(max_length=30)
    reseña = models.CharField(max_length=1000)
    
class CrearDios(models.Model):
    nombre = models.CharField(null=True, max_length=30)
    simbolo = models.CharField(null=True, max_length=30)
    origen = models.CharField(null=True, max_length=30)
    reseña = RichTextField(null=True)
    fecha_creacion = models.DateField(null=True)
    autor = models.CharField(null=True, max_length=30)
    def __str__(self):
        return f"Dios: {self.nombre}, simbolo: {self.simbolo}"
    

    