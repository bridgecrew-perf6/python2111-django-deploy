from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField()
    profesion = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"