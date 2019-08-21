from django.db import models
from apps.cuartel.models import Compania, Cuartel

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=40)


class Cuerpo(models.Model):
    id_cuerpo = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=40)

class Soldado(models.Model):
    id_soldado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    grado = models.CharField(max_length=40)
    servicio = models.ForeignKey(Servicio, models.CASCADE, blank=True, null=True)
    cuerpo = models.ForeignKey(Cuerpo, models.CASCADE, blank=True, null=True)
    compania = models.ForeignKey(Compania,blank=True, null=True)