from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
# Create your views here.
from .models import Festival,Autobus, Parking
from .forms import CrearFestivalForm, FestivalFiltroForm,CrearAutobusForm, FestivalNombreFiltroForm,CrearParkingForm
from typing import Any

from concerts_app.models import Artista, Concierto


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
        
        festivalesFuturos = Festival.objects.filter(fecha__gte=timezone.now())
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

    def form_valid(self, form):
        festival = form.save(commit=False)
        festival.boletos_disponibles = festival.ubicacion_festival.capacidad
        festival.save()
        return super().form_valid(form)

class FestivalDetailView(DetailView):
    model = Festival
    template_name = "festivales/festival_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        festival = self.object
        conciertos = Concierto.objects.filter(festival_relacionado=festival)
        context['conciertos'] = conciertos.exists()  #Esto es únicamente para poner el lineup en la plantilla
        return context

class FestivalUpdateView(UpdateView):
    model = Festival
    form_class = CrearFestivalForm
    success_url = reverse_lazy("festival_list")
    template_name = "festivales/festival_update.html"
    def form_valid(self, form):
        if 'foto' not in form.changed_data:
            form.instance.foto = self.get_object().foto
        return super().form_valid(form)


class FestivalDeleteView(DeleteView):
    model = Festival
    success_url = reverse_lazy("festival_list")
    template_name = "festivales/festival_confirm_delete.html"

class AutobusListView(View):
    template_name = "autobuses/autobus_list.html"
    
    def get(self, request, festival_pk):
        festival = get_object_or_404(Festival, pk=festival_pk)
        autobuses = Autobus.objects.filter(festival_relacionado=festival)
        return render(request, self.template_name, {"autobuses": autobuses, "festival": festival})
class AutobusCreateView(CreateView):
    model = Autobus
    form_class = CrearAutobusForm
    template_name = "autobuses/autobus_create.html"
    success_url = reverse_lazy("festival_list")
    
    def form_valid(self,form):
        autobus = form.save(commit=False)
        autobus.plazas_disponibles = autobus.capacidad
        festival_pk = self.kwargs['festival_pk']
        festival = get_object_or_404(Festival, pk=festival_pk)
        form.instance.festival_relacionado = festival
        festival.save()
        return super().form_valid(form)

class ParkingCreateView(CreateView):
    model = Parking
    form_class = CrearParkingForm
    template_name = "parkings/parking_create.html"
    success_url = reverse_lazy("festival_list")
    
    def form_valid(self,form):
        parking = form.save(commit=False)
        parking.plazas_disponibles = parking.capacidad
        festival_pk = self.kwargs['festival_pk']
        festival = get_object_or_404(Festival, pk=festival_pk)
        form.instance.festival_relacionado = festival
        festival.save()
        return super().form_valid(form)

class ParkingListView(View):
    template_name = "parkings/parking_list.html"
    
    def get(self, request, festival_pk):
        festival = get_object_or_404(Festival, pk=festival_pk)
        parkings = Parking.objects.filter(festival_relacionado=festival)
        return render(request, self.template_name, {"parkings": parkings, "festival": festival})
    
class FestivalesConAutobusesListView(ListView):
    model = Festival
    template_name = "festivales/festival_list_con_autobuses.html"
    form_class = FestivalNombreFiltroForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.GET)
        context["form"] = form
        
        festivales_con_bus = Festival.objects.filter(disponibilidad_autobuses=True)
        
        if form.is_valid():
            nombre_festival = form.cleaned_data.get("nombre_festival")
            
            if nombre_festival:
                festivales_con_bus = festivales_con_bus.filter(nombre__icontains=nombre_festival)

            context["festivales_con_bus"] = festivales_con_bus
            
        return context

class FestivalConParkingListView(ListView):
    model = Festival
    template_name = "festivales/festival_list_con_parking.html"
    form_class = FestivalNombreFiltroForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(self.request.GET)
        context["form"] = form
        
        festivales_con_parking = Festival.objects.filter(disponibilidad_parking=True)
        
        if form.is_valid():
            nombre_festival = form.cleaned_data.get("nombre_festival")
            
            if nombre_festival:
                festivales_con_parking = festivales_con_parking.filter(nombre__icontains=nombre_festival)

            context["festivales_con_parking"] = festivales_con_parking
            
        return context
    

class ArtistasFestivalListView(View):
    template_name = "festivales/artistas_festival_list.html"
    
    def get(self, request, festival_pk):
        festival = get_object_or_404(Festival, pk=festival_pk)
        artistas = Artista.objects.filter(concierto__festival_concierto=festival).distinct()
        return render(request, self.template_name, {"artistas": artistas, "festival": festival})