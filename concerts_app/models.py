from typing import Any
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from users_app.models import Cliente
from django.db.models import Avg
from django.apps import apps
from festivales_app.models import Festival




# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="artistas")
    concierto_relacionado = models.ForeignKey("Concierto", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre



class Concierto(models.Model):
    nombre = models.CharField(max_length=255)
    artista_concierto = models.ForeignKey(Artista, on_delete=models.CASCADE,null=True, blank=True)
    escenario = models.CharField(max_length=255 ,null=True, blank=True)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="conciertos")
    festival_relacionado = models.ForeignKey(Festival, on_delete=models.SET_NULL, related_name="conciertos", null=True, blank=True)  #Con el related_name="conciertos" se puede acceder a los conciertos de un festival con festival.conciertos.all()

    def __str__(self):
        return f"{self.nombre} - {self.artista_concierto} - {self.fecha}"

