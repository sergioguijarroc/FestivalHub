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
        
class AñadirEntradasFestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = [
            "entradas_general",
            "entradas_oro",
            "entradas_platino",
            "precio_entrada_general",
            "precio_entrada_oro",
            "precio_entrada_platino",
        ]
        labels = {
            "entradas_general": "Entradas general",
            "entradas_oro": "Entradas oro",
            "entradas_platino": "Entradas platino",
            "precio_entrada_general": "Precio entrada general",
            "precio_entrada_oro": "Precio entrada oro",
            "precio_entrada_platino": "Precio entrada platino",
        }
        widgets = {
            "entradas_general": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "entradas_oro": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "entradas_platino": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "precio_entrada_general": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "precio_entrada_oro": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "precio_entrada_platino": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
        }
    #Validar que al menos un tipo de entrada esté disponible
    def clean(self):
        cleaned_data = super().clean()
        entradas_general = cleaned_data.get("entradas_general")
        entradas_oro = cleaned_data.get("entradas_oro")
        entradas_platino = cleaned_data.get("entradas_platino")
        if entradas_general + entradas_oro + entradas_platino == 0:
            raise forms.ValidationError("Debe haber al menos un tipo de entrada disponible.")
        return cleaned_data

    #Esto es para que los campos sean requeridos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True