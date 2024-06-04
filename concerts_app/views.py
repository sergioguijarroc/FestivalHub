from datetime import date
from datetime import datetime

from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Concierto, Artista
from .forms import ArtistaForm, CrearConciertoForm
from django.db.models import Sum
from festivales_app.models import Festival
from django.forms import inlineformset_factory

# Create your views here.


def index(request):
    return render(request, "concerts_app/panelControl.html")


# region Conciertos
class ListarConciertosFestival(View):
    def get(self, request, pk):
        conciertos = Festival.objects.get(pk=pk).conciertos.all()
        festival = get_object_or_404(Festival, pk=pk)
        return render(request, "concerts_app/conciertos/concierto_list.html", {"conciertos": conciertos, "festival": festival})
    


class ConciertoDetailView(DetailView):
    model = Concierto
    template_name = "concerts_app/conciertos/concierto_detail.html"


# Staff
""" class ConciertoCreateView(CreateView):
    model = Concierto
    form_class = CrearConciertoForm
    template_name = "concerts_app/conciertos/concierto_create.html"


    def form_valid(self,form):
        festival_pk = self.kwargs['festival_pk']
        festival = get_object_or_404(Festival, pk=festival_pk)
        form.instance.festival_relacionado = festival
        return super().form_valid(form) """


class ConciertoCreateView(View):
    template_name = 'concerts_app/conciertos/crear_concierto.html'

    def get(self, request, festival_pk):
        concierto_form = CrearConciertoForm()
        artista_form = ArtistaForm()
        return render(request, self.template_name, {'concierto_form': concierto_form, 'artista_form': artista_form})

    def post(self, request, festival_pk):
        concierto_form = CrearConciertoForm(request.POST, request.FILES)
        artista_form = ArtistaForm(request.POST, request.FILES)

        if concierto_form.is_valid() and artista_form.is_valid():
            festival = get_object_or_404(Festival, pk=festival_pk)
            concierto = concierto_form.save(commit=False)
            concierto.festival_relacionado = festival
            concierto.nombre = concierto_form.cleaned_data['nombre_concierto']
            
            artista = artista_form.save()
            concierto.artista_concierto = artista
            
            concierto.save()
            artista.concierto_relacionado = concierto
            artista.save()
            
            return redirect('festival_list')
        else:
            return render(request, self.template_name, {'concierto_form': concierto_form, 'artista_form': artista_form})
        

    
class ConciertoDeleteView(DeleteView):
    model = Concierto
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_confirm_delete.html"



class ConciertoUpdateView(UpdateView):
    model = Concierto
    form_class = CrearConciertoForm
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/conciertos/concierto_update.html"


class ConciertoReview(View):
    def get(self, request, pk):
        concierto = get_object_or_404(Concierto, pk=pk)
        return render(
            request,
            "concerts_app/conciertos/concierto_review.html",
            {"concierto": concierto},
        )

    def post(self, request, pk):
        reserva = Reserva.objects.filter(
            concierto_reserva__pk=pk, cliente_reserva=self.request.user
        ).first()
        concierto = Concierto.objects.get(pk=reserva.concierto_reserva.pk)
        valoracionUsuario = float(request.POST["valoracion"])

        if (
            # reserva.cliente_reserva == self.request.user
            valoracionUsuario >= 0
            and valoracionUsuario <= 10
        ):
            if (
                reserva.valoracion_usuario is not None
                and reserva.valoracion_usuario__usuario_valoracion
                == reserva.cliente_reserva
            ):
                reserva.valoracion_usuario.actualizar_rating(valoracionUsuario)
                reserva.valoracion_usuario.save()
                reserva.save()
            else:
                valoracion = Valoracion.objects.create(
                    reserva_valoracion=reserva,
                    usuario_valoracion=self.request.user,
                    rating=valoracionUsuario,
                )
                reserva.valoracion_usuario = valoracion
                reserva.save()
                valoracion.save()

            concierto.actualizar_valoracion_media()
            concierto.save()

        return redirect("listar_reservas_usuario")


class ListarConciertosMasVendidos(ListView):
    model = Concierto
    template_name = "concerts_app/conciertos/concierto_top_ventas.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        top_conciertos_ventas = Concierto.objects.annotate(
            sum_compras=Sum("reserva__cantidad_tickets")
        ).order_by(  # Sumo la cantidad de tickets de cada concierto
            "-sum_compras"
        )[
            :3
        ]  # Ordeno de mayor a menor (con el -) y me quedo con los 3 primeros
        context["conciertos_top_ventas"] = top_conciertos_ventas
        return context


# endregion
# region Artistas


# Usuarios normales


class ArtistaListView(ListView):
    model = Artista
    template_name = "concerts_app/artistas/artista_list.html"


class ArtistaDetailView(DetailView):
    model = Artista
    template_name = "concerts_app/artistas/artista_detail.html"


# Staff
class ArtistaCreateView(CreateView):
    model = Artista
    form_class = ArtistaForm
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/artistas/artista_create.html"


class ArtistaDeleteView(DeleteView):
    model = Artista
    success_url = reverse_lazy("artista_list")
    template_name = "concerts_app/artistas/artista_confirm_delete.html"


class ArtistaUpdateView(UpdateView):
    model = Artista
    fields = "__all__"
    success_url = reverse_lazy("concierto_list")
    template_name = "concerts_app/artista_update.html"
    template_name = "concerts_app/artistas/artista_update.html"



# endregion
