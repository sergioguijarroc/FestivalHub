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
        
class DefinirNumeroEntradasPorZonaForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = [
            "entradas_platino",
            "entradas_oro",
            "entradas_general"
        ]
        labels = {
            "entradas_platino" : "Entradas platino",
            "entradas_oro" : "Entradas oro",
            "entradas_general" : "Entradas general"
        }
        
        widgets = {
            "entradas_platino" : forms.NumberInput(
                attrs={"class": "form-control", "min" : 0, "max" : 5}
            ),
            "entradas_oro" : forms.NumberInput(
                attrs={"class": "form-control", "min" : 0, "max" : 5}
            ),
            "entradas_general" : forms.NumberInput(
                attrs={"class": "form-control", "min" : 0, "max" : 5}
            )
            
        }

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