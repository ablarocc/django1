from django.db import models

class Paleta(models.Model):
    color = models.CharField(max_length=20)
    escote = models.CharField(max_length=20)
    fecha = models.DateField()
    

# Create your models here.
