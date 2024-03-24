from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente


class RegisterForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "edad",
            "direccion",
        ]
        labels = {
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
            "edad": "Edad",
            "direccion": "Dirección",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de usuario"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Correo electrónico"}
            ),
            "password1": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Contraseña"}
            ),
            "password2": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Confirmar contraseña"}
            ),
            "edad": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Edad"}
            ),
            "direccion": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Dirección"}
            ),
        }
