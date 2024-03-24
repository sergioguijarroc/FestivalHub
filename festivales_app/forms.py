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
    fecha_ascendente = forms.BooleanField(
        required = False,
        label = "Fecha ascendente",
        widget = forms.CheckboxInput(attrs = {"class": "form-check-input"}),
    )
    fecha_descendente = forms.BooleanField(
        required = False,
        label = "Fecha descendente",
        widget = forms.CheckboxInput(attrs = {"class": "form-check-input"}),
    )

