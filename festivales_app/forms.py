from django import forms
from .models import Festival, Ubicacion


class FestivalFiltroForm(forms.Form):
    
    nombre_festival = forms.CharField(
        required = False,
        label = "Nombre del festival",
        widget = forms.TextInput(
            attrs = {"class": "form-control", "placeholder": "Nombre del festival"}
        ),
    )
    genero_principal = forms.CharField(
        required = False,
        label = "Género principal",
        widget = forms.TextInput(
            attrs = {"class": "form-control", "placeholder": "Género principal"}
        ),
    )
    ubicacion_festival = forms.ModelChoiceField(
        queryset = Ubicacion.objects.all(),
        required = False,
        empty_label = "Todas las ubicaciones",
        widget = forms.Select(attrs = {"class": "form-control"}),
    )
    fecha_orden = forms.ChoiceField(
        required=False,
        label="Ordenar por fecha",
        choices=(
            ("ascendente", "Ascendente"),
            ("descendente", "Descendente"),
        ),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

class CrearFestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = [
            "nombre",
            "fecha",
            "ubicacion_festival",
            "boletos_disponibles",
            "descripcion",
            "foto",
            "valoracion_media",
            "disponibilidad_autobuses",
            "disponibilidad_parking",
            "precio_entrada",
            "genero_principal",
        ]
        labels = {
            "nombre": "Nombre del festival",
            "fecha": "Fecha",
            "ubicacion_festival": "Ubicación",
            "boletos_disponibles": "Boletos disponibles",
            "descripcion": "Descripción",
            "foto": "Foto",
            "valoracion_media": "Valoración media",
            "disponibilidad_autobuses": "Disponibilidad de autobuses",
            "disponibilidad_parking": "Disponibilidad de parking",
            "precio_entrada": "Precio de entrada",
            "genero_principal": "Género principal",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del festival"}
            ),
            "fecha": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "ubicacion_festival": forms.Select(
                attrs={"class": "form-control"}
            ),
            "boletos_disponibles": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción del festival",
                }
            ),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "valoracion_media": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "disponibilidad_autobuses": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "disponibilidad_parking": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "precio_entrada": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "genero_principal": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Género principal"}
            ),
        }