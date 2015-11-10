from django.db import models

# Create your models here.


class LugarEvento(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    latitud =models.FloatField(blank=True, null=True)
    altitud =models.FloatField(blank=True, null=True)
    calificacion = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateTimeField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    lugar_evento = models.ForeignKey(LugarEvento)

    def __unicode__(self):
        return self.nombre
    
class Taller(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    ponente = models.ForeignKey('auth.User')
    evento = models.ForeignKey(Evento)
