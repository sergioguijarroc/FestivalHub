from django import forms
from .models import Festival, Ubicacion, Autobus


class FestivalFiltroForm(forms.Form):
    
    nombre_festival = forms.CharField(
        required=False,
        label="Nombre del festival",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre del festival"}
        ),
    )
    genero_principal = forms.ChoiceField(
        choices=[('', 'Todos los géneros')] + [(g, g) for g in Festival.objects.order_by().values_list('genero_principal', flat=True).distinct()],
        #g,g es para que el valor y el texto del option sean iguales
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
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

class CrearFestivalForm(forms.ModelForm):
    autobus_ubicacion_parada = forms.CharField(
        label="Ubicación de la parada del autobús",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ubicación de la parada del autobús"}),
    )
    autobus_capacidad = forms.IntegerField(
        label="Capacidad del autobús",
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Capacidad del autobús"}),
    )
    autobus_precio = forms.DecimalField(
        label="Precio del autobús",
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Precio del autobús"}),
    )
    autobus_fecha_salida = forms.DateField(
        label="Fecha de salida del autobús",
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

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
            "precio_entrada",
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
            "precio_entrada": "Precio de entrada",
            "genero_principal": "Género principal",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del festival"}),
            "fecha": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "ubicacion_festival": forms.Select(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción del festival"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "precio_entrada": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        disponibilidad_autobuses = cleaned_data.get("disponibilidad_autobuses")
        autobus_ubicacion_parada = cleaned_data.get("autobus_ubicacion_parada")
        autobus_capacidad = cleaned_data.get("autobus_capacidad")
        autobus_precio = cleaned_data.get("autobus_precio")
        autobus_fecha_salida = cleaned_data.get("autobus_fecha_salida")

        if disponibilidad_autobuses and not autobus_ubicacion_parada:
            self.add_error("autobus_ubicacion_parada", "Este campo es obligatorio si se marca la casilla de disponibilidad de autobuses")

        if disponibilidad_autobuses and not autobus_capacidad:
            self.add_error("autobus_capacidad", "Este campo es obligatorio si se marca la casilla de disponibilidad de autobuses")

        if disponibilidad_autobuses and not autobus_precio:
            self.add_error("autobus_precio", "Este campo es obligatorio si se marca la casilla de disponibilidad de autobuses")

        if disponibilidad_autobuses and not autobus_fecha_salida:
            self.add_error("autobus_fecha_salida", "Este campo es obligatorio si se marca la casilla de disponibilidad de autobuses")

    def save(self, commit=True):
        festival = super().save(commit=False)
        disponibilidad_autobuses = self.cleaned_data.get("disponibilidad_autobuses")

        if disponibilidad_autobuses:
            autobus_ubicacion_parada = self.cleaned_data.get("autobus_ubicacion_parada")
            autobus_capacidad = self.cleaned_data.get("autobus_capacidad")
            autobus_precio = self.cleaned_data.get("autobus_precio")
            autobus_fecha_salida = self.cleaned_data.get("autobus_fecha_salida")

            autobus = Autobus.objects.create(
                ubicacion_parada=autobus_ubicacion_parada,
                capacidad=autobus_capacidad,
                precio=autobus_precio,
                fecha_salida=autobus_fecha_salida,
                festival_relacionado=festival,
            )
            autobus.save()

        if commit:
            festival.save()
        return festival

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
            "fecha_salida": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
    