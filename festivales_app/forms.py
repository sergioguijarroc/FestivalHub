from datetime import datetime,timezone
from django import forms
from .models import Festival, Parking, Ubicacion, Autobus
from django.forms import ValidationError


class FestivalFiltroForm(forms.Form):
    nombre_festival = forms.CharField(
        required=False,
        label="Nombre del festival",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre del festival"}
        ),
    )
    genero_principal = forms.ChoiceField(choices=[], required=False, widget=forms.Select(attrs={"class": "form-control"}))
    ubicacion_festival = forms.ModelChoiceField(
        queryset=Ubicacion.objects.all(),
        required=False,
        empty_label="Todas las ubicaciones",
        widget=forms.Select(attrs={"class": "form-control"}),
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genero_principal'].choices = [('', 'Todos los géneros')] + [(g, g) for g in Festival.objects.order_by().values_list('genero_principal', flat=True).distinct()]

class CrearFestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = [
            "nombre",
            "fecha",
            "ubicacion_festival",
            "descripcion",
            "foto",
            "disponibilidad_autobuses",
            "disponibilidad_parking",
            "genero_principal",
        ]
        labels = {
            "nombre": "Nombre del festival",
            "fecha": "Fecha",
            "ubicacion_festival": "Ubicación",
            "descripcion": "Descripción",
            "foto": "Foto",
            "disponibilidad_autobuses": "Disponibilidad de autobuses",
            "disponibilidad_parking": "Disponibilidad de parking",
            "genero_principal": "Género principal",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del festival"}),
            "fecha": forms.DateTimeInput(attrs={"class": "form-control", "type": "date"}),
            "ubicacion_festival": forms.Select(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción del festival"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }
        
    def clean_fecha(self):
        fecha = self.cleaned_data.get("fecha")
        if fecha < datetime.now(timezone.utc).date():
            raise ValidationError("La fecha del festival no puede ser en el pasado.")
        return fecha
            
        

""" class Autobus(models.Model):
    ubicacion_parada = models.CharField(max_length=255)
    capacidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_salida = models.DateTimeField()
    festival_relacionado = models.ForeignKey("Festival", on_delete=models.CASCADE)
"""
class CrearAutobusForm(forms.ModelForm):
    class Meta:
        model = Autobus
        fields = [
            "ubicacion_parada",
            "capacidad",
            "precio",
            "fecha_salida",
        ]
        labels = {
            "ubicacion_parada": "Ubicación de la parada",
            "capacidad": "Capacidad",
            "precio": "Precio",
            "fecha_salida": "Fecha de salida",
        }
        widgets = {
            "ubicacion_parada": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ubicación de la parada"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Capacidad"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Precio"}),
            "fecha_salida": forms.DateInput(attrs={"class": "form-control", "type": "datetime-local"}),
        }
        
        def clean_fecha_salida(self):
            fecha_salida = self.cleaned_data.get("fecha_salida")
            if fecha_salida < datetime.now(timezone.utc).date():
                raise ValidationError("La fecha de salida del autobús no puede ser en el pasado.")
            return fecha_salida
    
class CrearParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = [
            "ubicacion_parking",
            "capacidad",
            "precio",
        ]
        labels = {
            "ubicacion_parking": "Ubicación del parking",
            "capacidad": "Capacidad",
            "precio": "Precio",
        }
        widgets = {
            "ubicacion_parking": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ubicación del parking"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Capacidad"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Precio"}),
        }
        
        def clean_precio(self):
            precio = self.cleaned_data.get("precio")
            if precio < 0:
                raise ValidationError("El precio del parking no puede ser negativo.")
            return precio


class FestivalNombreFiltroForm(forms.Form):
    nombre_festival = forms.CharField(
        required=False,
        label="Nombre del festival",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre del festival"}
        ),
    )
