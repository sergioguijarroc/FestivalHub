from django.db import models
from users_app.models import Usuario

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# Create your models here.
class ReservaFestival(models.Model):
    festival_reserva = models.ForeignKey(
        "festivales_app.Festival", on_delete=models.CASCADE
    )
    cliente_reserva = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad_tickets = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]  # Como máximo puede comprar 5 boletos
    )
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente_reserva} - {self.festival_reserva} - {self.cantidad_tickets}"
    class Meta:
        verbose_name_plural = "Reservas de Festivales"

class ReservaAutobus(models.Model):
    autobus_reserva = models.ForeignKey(
        "festivales_app.Autobus", on_delete=models.CASCADE
    )
    cliente_reserva = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad_tickets = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]  # Como máximo puede comprar 5 boletos
    )
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente_reserva} - {self.autobus_reserva} - {self.cantidad_tickets}"
    class Meta:
        verbose_name_plural = "Reservas de Autobuses"
        
class ReservaParking(models.Model):
    parking_reserva = models.ForeignKey(
        "festivales_app.Parking", on_delete=models.CASCADE
    )
    cliente_reserva = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad_tickets = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]  # Como máximo puede comprar 5 boletos
    )
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente_reserva} - {self.parking_reserva} - {self.cantidad_tickets}"
    class Meta:
        verbose_name_plural = "Reservas de Parkings"

""" class Reserva(models.Model):
    concierto_reserva = models.ForeignKey(
        "concerts_app.Concierto", on_delete=models.CASCADE
    )
    cliente_reserva = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    cantidad_tickets = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]  # Como máximo puede comprar 5 boletos
    )
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    valoracion_usuario = models.OneToOneField(
        "Valoracion", on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def actualizarReservaYaExistente(self, unidades, importeNuevo):
        self.cantidad_tickets += unidades
        self.importe += importeNuevo
        self.save()

    def __str__(self):
        return f"{self.cliente_reserva} - {self.concierto_reserva} - {self.cantidad_tickets}"
 """

""" class Valoracion(models.Model):
    reserva_valoracion = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    usuario_valoracion = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
    )

    rating = models.FloatField(null=True, blank=True, default=None)

    def actualizar_rating(self, rating):
        self.rating = rating

    def __str__(self):
        return f"{self.usuario_valoracion} - {self.reserva_valoracion} - {self.rating}"

    # verbose
    class Meta:
        verbose_name_plural = "Valoraciones"
 """

"""
class Promocion(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    descuento = models.FloatField(default=0)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(default=timezone.now() + timezone.timedelta(days=15))

    def __str__(self):
        return self.nombre

    def calcularDescuento(self, importe):
        self.descuento = importe * 0.1
        self.save()
        return self.descuento

    class Meta:
        verbose_name_plural = "Promociones"
"""
