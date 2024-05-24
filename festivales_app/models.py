from django.db import models
from django.utils import timezone


# Create your models here.

class Festival(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion_festival = models.ForeignKey("Ubicacion", on_delete=models.CASCADE)
    boletos_disponibles = models.PositiveIntegerField(default=0)
    entradas_platino = models.PositiveIntegerField(null=True,blank=True)
    entradas_oro = models.PositiveIntegerField(null=True,blank=True)
    entradas_general = models.PositiveIntegerField(null=True,blank=True)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="festivales")
    valoracion_media = models.FloatField(blank=True, null=True, default=None)
    disponibilidad_autobuses = models.BooleanField(default=False)
    disponibilidad_parking = models.BooleanField(default=False)
    precio_entrada_platino = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_entrada_oro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_entrada_general = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    genero_principal = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    def get_precio_entrada(self, tipo_entrada):
        if tipo_entrada == "platino":
            return self.precio_entrada_platino
        elif tipo_entrada == "oro":
            return self.precio_entrada_oro
        return self.precio_entrada_general

    def get_entradas_disponibles(self, tipo_entrada):
        if tipo_entrada == "platino":
            return self.entradas_platino
        elif tipo_entrada == "oro":
            return self.entradas_oro
        return self.entradas_general
    class Meta:
        verbose_name_plural = "Festivales"
        
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ubicaciones"
        
class Autobus(models.Model):
    ubicacion_parada = models.CharField(max_length=255)
    capacidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_salida = models.DateTimeField()
    festival_relacionado = models.ForeignKey("Festival", on_delete=models.CASCADE)
    plazas_disponibles = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Autobús del festival {self.festival_relacionado.nombre} con salida desde {self.ubicacion_parada}"

    class Meta:
        verbose_name_plural = "Autobuses"
    
class Parking(models.Model):
    ubicacion_parking = models.CharField(max_length=255)
    capacidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    festival_relacionado = models.ForeignKey("Festival", on_delete=models.CASCADE)
    plazas_disponibles = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Parking del festival {self.festival_relacionado.nombre} con ubicación en {self.ubicacion_parking}"
    class Meta:
        verbose_name_plural = "Parkings"
