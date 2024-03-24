from typing import Any
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from tickets_app.models import Valoracion
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

    def __str__(self):
        return self.nombre



class Concierto(models.Model):
    nombre = models.CharField(max_length=255)
    artista_concierto = models.ForeignKey(Artista, on_delete=models.CASCADE)
    #ubicacion_concierto = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    escenario = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    #precio_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    boletos_disponibles = models.PositiveIntegerField(default=0)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="conciertos")
    #valoracion_media = models.FloatField(blank=True, null=True, default=None)
    festival_concierto = models.ForeignKey(Festival, on_delete=models.CASCADE,related_name="conciertos")
    #Con el related_name="conciertos" se puede acceder a los conciertos de un festival con festival.conciertos.all()


    def actualizar_valoracion_media(self):
        # Obtengo todas las valoraciones asociadas al concierto
        reviews = Valoracion.objects.filter(reserva_valoracion__concierto_reserva=self)

        # Calculo el promedio de las valoraciones
        avg_rating = reviews.aggregate(Avg("rating"))["rating__avg"]
        # Actualizo la valoración media del concierto
        if avg_rating is not None:
            self.valoracion_media = avg_rating

        # Guardo el concierto actualizado
        self.save()

    def __str__(self):
        return f"{self.nombre} - {self.artista_concierto} - {self.fecha}"

"""
class Notificacion(models.Model):
    cliente_notificacion = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mensaje = models.TextField()

    def __str__(self):
        return f"Notificación para {self.cliente_notificacion}: {self.mensaje}"

    class Meta:
        verbose_name_plural = "Notificaciones"
"""