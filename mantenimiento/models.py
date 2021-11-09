from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
#Modelo para tabla de Lugares
class lugar(models.Model):
    Nombre = models.CharField(max_length=30,verbose_name="nombre")
    Descripcion = models.CharField(max_length=100,verbose_name="descripcion")

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

    def __str__(self):
        return self.Nombre

# Modelo para tabla de Areas
class Area(models.Model):
    Nombre =models.CharField(max_length=10,verbose_name="area")
    Descripcion = models.CharField(max_length=100,verbose_name="descripcion")
    lugar = models.ForeignKey(lugar,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "área"
        verbose_name_plural = "áreas"
        ordering = ['Nombre']


    def __str__(self):
        return self.Nombre +'-'+ self.Descripcion

# Modelo de Tipo de Equipos
class TipoEquipo(models.Model):
    Prefijo = models.CharField(max_length=3,verbose_name="prefijo")
    Nombre = models.CharField(max_length=30,verbose_name="Tipo de Equipo")
    Descripcion = models.CharField(max_length=100,verbose_name="descripcion")

    class Meta:
        verbose_name = "tipo de equipo"
        verbose_name_plural ="tipos de equipos"
        ordering = ['Nombre']

    def __str__(self):
        return self.Prefijo + '-'+ self.Nombre + '  =  ' + self.Descripcion

        
