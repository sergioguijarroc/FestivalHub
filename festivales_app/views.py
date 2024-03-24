from django.shortcuts import render
from datetime import datetime
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
# Create your views here.
from .models import Festival
from .forms import FestivalFiltroForm
from typing import Any

# region Conciertos
# Usuarios normales
class FestivalListView(ListView):
    model = Festival
    template_name = "festivales_app/festivales/festival_list.html"
    form_class = FestivalFiltroForm
    queryset = Festival.objects.all()

    # queryset = Concierto.objects.filter(fecha__gt=datetime.now())

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        form = self.form_class(
            self.request.GET
        )  # Esto es para que nos venga relleno el formulario
        context["form"] = form
        if form.is_valid():
            nombre_festival = form.cleaned_data.get("nombre_festival")
            genero_principal = form.cleaned_data.get("genero_principal")
            ubicacion = form.cleaned_data.get("ubicacion_festival")
            fecha_ascendente = form.cleaned_data.get("fecha_ascendente")
            fecha_descendente = form.cleaned_data.get("fecha_descendente")
            
            festivalesFuturos = self.queryset.filter(fecha__gt=datetime.now())
            festivalesPasados = self.queryset.filter(fecha__lt=datetime.now())

            if nombre_festival != "":
                festivalesFuturos = festivalesFuturos.filter(
                    nombre__icontains=nombre_festival
                )
                festivales_pasados = festivalesPasados.filter(
                    nombre__icontains=nombre_festival
                )

            if genero_principal is not None:
                festivalesFuturos = festivalesFuturos.filter(genero_principal=genero_principal)
                festivalesPasados = festivalesPasados.filter(genero_principal=genero_principal)
            if ubicacion is not None:
                festivalesFuturos = festivalesFuturos.filter(
                    ubicacion_festival=ubicacion
                )
                festivalesPasados = festivalesPasados.filter(
                    ubicacion_festival=ubicacion
                )
            if fecha_ascendente:
                festivalesFuturos = festivalesFuturos.order_by("fecha")
                festivalesPasados = festivalesPasados.order_by("fecha")
            
            if fecha_descendente:
                festivalesFuturos = festivalesFuturos.order_by("-fecha")
                festivalesPasados = festivalesPasados.order_by("-fecha")
            
            context["festivalesFuturos"] = festivalesFuturos
            context["festivalesPasados"] = festivalesPasados
        return context


"""
class ConciertoDetailView(DetailView):
    model = Festival
    template_name = "festivales_app/festivales/festival_detail.html"

# Staff
class ConciertoCreateView(CreateView):
    model = Concierto
    form_class = CrearConciertoForm
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_create.html"

    def form_valid(
        self, form
    ):  # Se sobreescribe el método para que se pueda modificar el número de boletos disponibles
        concierto = form.save(
            commit=False
        )  # Con esto evitamos que se guarde el concierto hasta que se modifique el número de boletos disponibles, pero me lo traigo a la vista para modificarlo
        concierto.boletos_disponibles = concierto.ubicacion_concierto.capacidad
        concierto.save()
        return super().form_valid(
            form
        )  # Se guarda el concierto personalizado con el número de boletos disponibles modificado,se llama al método de la clase padre para que guarde el concierto


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