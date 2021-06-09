from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)    
    oferta = models.BooleanField()    
    precio = models.PositiveIntegerField() 
