from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from .forms import ReservaFestivalForm,ReservaAutobusForm
from festivales_app.models import Autobus
from .models import ReservaAutobus, ReservaFestival

# Create your views here.

""" 
class ComprarEntradas(View):  # Hay que meterle que esté logueado
    def get(self, request, pk):
        concierto = get_object_or_404(Concierto, pk=pk)
        formulario = ReservaForm()
        return render(
            request,
            "tickets_app/comprar_entradas.html",
            {"concierto": concierto, "formulario": formulario},
        )

    def post(self, request, pk):
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            concierto = get_object_or_404(Concierto, pk=pk)
            unidades = formulario.cleaned_data["cantidad_tickets"]
            return redirect(
                "confirmar_compra",
                pk,  # Le paso la pk del concierto para recogerla luego en ConfirmaciónCompra
                unidades,
            )
        return render(
            request,
            "tickets_app/comprar_entradas.html",
            {"concierto": concierto, "formulario": formulario},
        )


class ConfirmacionCompra(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        concierto = get_object_or_404(Concierto, pk=pk)
        unidades = kwargs.get("unidades", None)
        usuario = request.user
        importe = concierto.precio_entrada * unidades

        return render(
            request,
            "tickets_app/confirmacion_compra.html",
            {
                "concierto": concierto,
                "unidades": unidades,
                "usuario": usuario,
                "importe": importe,
            },
        )

    def post(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        concierto = get_object_or_404(Concierto, pk=pk)
        unidades = kwargs.get("unidades", None)
        usuario = self.request.user
        importe = concierto.precio_entrada * unidades

        concierto.boletos_disponibles -= unidades
        concierto.save()

        reservaExistente = Reserva.objects.filter(
            concierto_reserva=concierto, cliente_reserva=usuario
        ).first()
        if reservaExistente:
            reservaExistente.actualizarReservaYaExistente(unidades, importe)
        else:
            Reserva.objects.create(
                concierto_reserva=concierto,
                cliente_reserva=usuario,
                cantidad_tickets=unidades,
                importe=importe,
            )
        return redirect("listar_reservas_usuario") """

class ComprarEntradasBus(View):
    def get(self, request, pk):
        autobus = get_object_or_404(Autobus, pk=pk)
        formulario = ReservaAutobusForm()
        return render(
            request,
            "tickets_app/comprar_entradas_bus.html",
            {"autobus": autobus, "formulario": formulario},
        )

    def post(self, request, pk):
        formulario = ReservaAutobusForm(request.POST)
        if formulario.is_valid():
            autobus = get_object_or_404(Autobus, pk=pk)
            unidades = formulario.cleaned_data["cantidad_tickets"]
            return redirect(
                "confirmar_compra_bus",
                pk,  # Le paso la pk del autobus para recogerla luego en ConfirmaciónCompra
                unidades,
            )
        return render(
            request,
            "tickets_app/comprar_entradas_bus.html",
            {"autobus": autobus, "formulario": formulario},
        )
    
class ConfirmacionCompraBus(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        autobus = get_object_or_404(Autobus, pk=pk)
        unidades = kwargs.get("unidades", None)
        usuario = request.user
        importe = autobus.precio * unidades

        return render(
            request,
            "tickets_app/confirmacion_compra_bus.html",
            {
                "autobus": autobus,
                "unidades": unidades,
                "usuario": usuario,
                "importe": importe,
            },
        )

    def post(self, **kwargs):
        pk = kwargs.get("pk", None)
        autobus = get_object_or_404(Autobus, pk=pk)
        unidades = kwargs.get("unidades", None)
        usuario = self.request.user
        importe = autobus.precio * unidades

        autobus.plazas_disponibles -= unidades
        autobus.save()
        ReservaAutobus.objects.create(
            autobus_reserva=autobus,
            cliente_reserva=usuario,
            cantidad_tickets=unidades,
            importe=importe,
        )
        return redirect("listar_reservas_usuario")