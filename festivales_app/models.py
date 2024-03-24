from django.db import models


# Create your models here.

class Festival(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion_festival = models.ForeignKey("Ubicacion", on_delete=models.CASCADE)
    boletos_disponibles = models.PositiveIntegerField(default=0)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="festivales")
    valoracion_media = models.FloatField(blank=True, null=True, default=None)
    disponibilidad_autobuses = models.BooleanField(default=False)
    disponibilidad_parking = models.BooleanField(default=False)
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ubicaciones"