from django import forms
from .models import ReservaFestival,ReservaAutobus,ReservaParking
from festivales_app.models import Festival
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users_app.models import Usuario

class ActualizarEntradas(forms.ModelForm):
    class Meta:
        model = Festival
        fields = [
            "boletos_disponibles"
        ]

class ReservaFestivalForm(forms.ModelForm):
    class Meta:
        model = ReservaFestival
        fields = [
            "cantidad_tickets",
        ]
        labels = {
            "cantidad_tickets": "Cantidad de boletos",
        }
        widgets = {
            "cantidad_tickets": forms.NumberInput(
                attrs={"class": "form-control", "min": 0, "max": 5}
            ),
        }
        
""" class DefinirNumeroEntradasPorZonaForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = [
            
        ]
 """
class ReservaAutobusForm(forms.ModelForm):
    class Meta:
        model = ReservaAutobus
        fields = [
            "cantidad_tickets",
        ]
        labels = {
            "cantidad_tickets": "Cantidad de boletos",
        }
        widgets = {
            "cantidad_tickets": forms.NumberInput(
                attrs={"class": "form-control", "min": 0, "max": 5}
            ),
        }
        

class ReservaParkingForm(forms.ModelForm):
    class Meta:
        model = ReservaParking
        fields = [
            "cantidad_tickets",
        ]
        labels = {
            "cantidad_tickets": "Cantidad de boletos",
        }
        widgets = {
            "cantidad_tickets": forms.NumberInput(
                attrs={"class": "form-control", "min": 0, "max": 5}
            ),
        }