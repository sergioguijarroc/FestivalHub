from django import forms
from django.forms import BaseFormSet, formset_factory
from .models import Concierto, Artista
from datetime import datetime, timezone
from django.forms import ValidationError

class CrearConciertoForm(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = ["nombre_concierto", "fecha"]
        labels = {
            "nombre_concierto": "Nombre del concierto",
            "fecha": "Fecha",
        }
        widgets = {
            "nombre_concierto": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del concierto"}),
            "fecha": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
        }
        
        def clean_fecha(self):
            fecha = self.cleaned_data.get("fecha")
            if fecha < datetime.now(timezone.utc).date():
                raise ValidationError("La fecha del festival no puede ser en el pasado.")
            return fecha

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ["nombre", "genero", "descripcion", "foto"]
        labels = {
            "nombre": "Nombre del artista",
            "genero": "Género",
            "descripcion": "Descripción",
            "foto": "Foto",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del artista"}),
            "genero": forms.TextInput(attrs={"class": "form-control", "placeholder": "Género del artista"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción del artista"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }


