from django import forms
from .models import Concierto, Artista


class CrearConciertoForm(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = [
            "nombre",
            "artista_concierto",
            "fecha",
            "descripcion",
            "foto",
        ]
        labels = {
            "nombre": "Nombre del concierto",
            "artista_concierto": "Artista",
            "fecha": "Fecha",
            "descripcion": "Descripción",
            "foto": "Foto",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del concierto"}
            ),
            "artista_concierto": forms.Select(attrs={"class": "form-control"}),
            "fecha": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción del concierto",
                }
            ),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }


# required = False en todos los campos
class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = [
            "nombre",
            "genero",
            "descripcion",
            "foto",
        ]
        labels = {
            "nombre": "Nombre del artista",
            "genero": "Género",
            "descripcion": "Descripción",
            "foto": "Foto",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del artista"}
            ),
            "genero": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Género del artista"}
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción del artista",
                }
            ),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }

        def __init__(self, *args, **kwargs):
            super(ArtistaForm, self).__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].required = False

