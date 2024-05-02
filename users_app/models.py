from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255)


class Cliente(Usuario):
    edad = models.PositiveIntegerField(null=True, blank=True)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Clientes"


class Staff(Usuario):
    funcion = models.TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Establecer staff_status en True al inicializar una instancia de Staff
        self.is_staff = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Staffs"
        

