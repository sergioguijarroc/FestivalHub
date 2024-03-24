from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
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
