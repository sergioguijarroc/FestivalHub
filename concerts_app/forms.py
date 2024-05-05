from django import forms
from django.forms import BaseFormSet, formset_factory
from .models import Concierto, Artista

class CrearConciertoForm(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = ["nombre", "escenario", "fecha", "descripcion", "foto"]
        labels = {
            "nombre": "Nombre del concierto",
            "escenario": "Escenario",
            "fecha": "Fecha",
            "descripcion": "Descripción",
            "foto": "Foto",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del concierto"}),
            "escenario": forms.TextInput(attrs={"class": "form-control", "placeholder": "Escenario"}),
            "fecha": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción del concierto"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }

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


