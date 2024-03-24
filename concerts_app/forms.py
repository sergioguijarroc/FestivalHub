from django import forms
from .models import Concierto, Artista, Ubicacion


class CrearConciertoForm(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = [
            "nombre",
            "artista_concierto",
            "ubicacion_concierto",
            "fecha",
            "precio_entrada",
            "descripcion",
            "foto",
        ]
        labels = {
            "nombre": "Nombre del concierto",
            "artista_concierto": "Artista",
            "ubicacion_concierto": "Ubicación",
            "fecha": "Fecha",
            "precio_entrada": "Precio de entrada",
            "descripcion": "Descripción",
            "foto": "Foto",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del concierto"}
            ),
            "artista_concierto": forms.Select(attrs={"class": "form-control"}),
            "ubicacion_concierto": forms.Select(attrs={"class": "form-control"}),
            "fecha": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "precio_entrada": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
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


class ConciertoFiltroFrom(forms.Form):

    nombreConcierto = forms.CharField(
        required=False,
        label="Nombre del concierto",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre del concierto"}
        ),
    )
    artista = forms.ModelChoiceField(
        queryset=Artista.objects.all(),
        required=False,
        empty_label="Todos los Artistas",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    ubicacion_concierto = forms.ModelChoiceField(
        queryset=Ubicacion.objects.all(),
        required=False,
        empty_label="Todas las ubicaciones",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    fecha_ascendente = forms.BooleanField(
        required=False,
        label="Ordenar por fecha más próxima",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
