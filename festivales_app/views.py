from django.shortcuts import render
from datetime import datetime
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
# Create your views here.
from .models import Festival
from .forms import CrearFestivalForm, FestivalFiltroForm
from typing import Any

# region Conciertos
# Usuarios normales
class FestivalListView(ListView):
    model = Festival
    template_name = "festivales/festival_list.html"
    form_class = FestivalFiltroForm

    # queryset = Concierto.objects.filter(fecha__gt=datetime.now())

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        form = self.form_class(
            self.request.GET
        )  # Esto es para que nos venga relleno el formulario
        context["form"] = form
        
        festivalesFuturos = Festival.objects.filter(fecha__gt=timezone.now())
        festivalesPasados = Festival.objects.filter(fecha__lt=timezone.now())
        

        if form.is_valid():
            nombre_festival = form.cleaned_data.get("nombre_festival")
            genero_principal = form.cleaned_data.get("genero_principal")
            ubicacion = form.cleaned_data.get("ubicacion_festival")
            fecha_orden = form.cleaned_data.get("fecha_orden")
            
            

            if nombre_festival:
                festivalesFuturos = festivalesFuturos.filter(
                    nombre__icontains=nombre_festival
                )
                festivalesPasados = festivalesPasados.filter(
                    nombre__icontains=nombre_festival
                )

            if genero_principal:
                festivalesFuturos = festivalesFuturos.filter(genero_principal=genero_principal)
                festivalesPasados = festivalesPasados.filter(genero_principal=genero_principal)
            if ubicacion:
                festivalesFuturos = festivalesFuturos.filter(
                    ubicacion_festival=ubicacion
                )
                festivalesPasados = festivalesPasados.filter(
                    ubicacion_festival=ubicacion
                )
            if fecha_orden == "ascendente":
                festivalesFuturos = festivalesFuturos.order_by("fecha")
                festivalesPasados = festivalesPasados.order_by("fecha")
            else:
                festivalesFuturos = festivalesFuturos.order_by("-fecha")
                festivalesPasados = festivalesPasados.order_by("-fecha")

            
            context["festivalesFuturos"] = festivalesFuturos
            context["festivalesPasados"] = festivalesPasados
            
        
        return context

# Staff
class FestivalCreateView(CreateView):
    model = Festival
    form_class = CrearFestivalForm
    success_url = reverse_lazy("festival_list")
    template_name = "festivales/festival_create.html"

    def form_valid(
        self, form
    ):  # Se sobreescribe el método para que se pueda modificar el número de boletos disponibles
        festival = form.save(
            commit=False
        )  # Con esto evitamos que se guarde el concierto hasta que se modifique el número de boletos disponibles, pero me lo traigo a la vista para modificarlo
        festival.boletos_disponibles = festival.ubicacion_festival.capacidad
        festival.save()
        return super().form_valid(
            form
        )  # Se guarda el concierto 


"""
class ConciertoDetailView(DetailView):
    model = Festival
    template_name = "festivales_app/festivales/festival_detail.html"

personalizado con el número de boletos disponibles modificado,se llama al método de la clase padre para que guarde el concierto


class ConciertoDeleteView(DeleteView):
    model = Concierto
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_confirm_delete.html"


class ConciertoUpdateView(UpdateView):
    model = Concierto
    form_class = CrearConciertoForm
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_update.html"

"""