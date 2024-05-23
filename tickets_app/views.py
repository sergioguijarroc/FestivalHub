from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from .forms import ReservaFestivalForm,ReservaAutobusForm,ReservaParkingForm,AñadirEntradasFestivalForm
from festivales_app.models import Autobus,Parking,Festival
from .models import ReservaAutobus, ReservaFestival,ReservaParking

# Create your views here.


class MapaZonasFestival(View):
    def get(self,request,pk):
        festival = get_object_or_404(Festival,pk=pk)
        return render(
            request,
            "tickets_app/mapa_zonas_festival.html",
            {"festival": festival}
        )
        
class AñadirEntradasFestival(View):
    def get(self,request,pk):
        festival = get_object_or_404(Festival,pk=pk)
        formulario = AñadirEntradasFestivalForm(instance=festival)
        entradas_restantes_zona = festival.boletos_disponibles - (festival.entradas_platino + festival.entradas_oro + festival.entradas_general)
        return render(
            request,
            "tickets_app/añadir_entradas_festival.html",
            {"festival" : festival , "form" : formulario,"entradas_restantes" : entradas_restantes_zona}
        )
    def post(self,request,pk):
        formulario = AñadirEntradasFestivalForm(request.POST)
        if formulario.is_valid():
            festival = get_object_or_404(Festival,pk=pk)
            entradas_platino = formulario.cleaned_data["entradas_platino"]
            entradas_oro = formulario.cleaned_data["entradas_oro"]
            entradas_general = formulario.cleaned_data["entradas_general"]
            precio_entrada_platino = formulario.cleaned_data["precio_entrada_platino"]
            precio_entrada_oro = formulario.cleaned_data["precio_entrada_oro"]
            precio_entrada_general = formulario.cleaned_data["precio_entrada_general"]
            if(entradas_platino + entradas_oro + entradas_general > festival.boletos_disponibles):
                return render(
                    request,
                    "tickets_app/añadir_entradas_festival.html",
                    {"festival" : festival , "form" : formulario , "error" : "La suma de las entradas no puede superar el número de boletos disponibles, revisa la cantidad de entradas y vuelve a intentarlo"} 
                )
            else:
                festival.precio_entrada_platino = precio_entrada_platino
                festival.precio_entrada_oro = precio_entrada_oro
                festival.precio_entrada_general = precio_entrada_general
                festival.entradas_platino = entradas_platino
                festival.entradas_oro = entradas_oro
                festival.entradas_general = entradas_general
                festival.save()
                return redirect("festival_list")
        return render(
            request,
            "tickets_app/añadir_entradas_festival.html",
            {"festival" : festival , "form" : formulario}
        )

class ComprarEntradasFestival(View):
    def get(self, request, pk, tipo_entrada):
        festival = get_object_or_404(Festival, pk=pk)
        formulario = ReservaFestivalForm()
        precio = festival.get_precio_entrada(tipo_entrada)
        entradas_restantes_zona = festival.get_entradas_disponibles(tipo_entrada)
        return render(
            request,
            "tickets_app/comprar_entradas_festival.html",
            {"festival": festival, "formulario": formulario, "precio": precio, "tipo_entrada": tipo_entrada, "entradas_restantes_zona": entradas_restantes_zona},
        )

    def post(self, request, pk, tipo_entrada):
        formulario = ReservaFestivalForm(request.POST)
        if formulario.is_valid():
            festival = get_object_or_404(Festival, pk=pk)
            unidades = formulario.cleaned_data["cantidad_tickets"]
            return redirect(
                "confirmar_compra_festival",
                pk=pk,
                unidades=unidades,
                tipo_entrada=tipo_entrada
            )
        return render(
            request,
            "tickets_app/comprar_entradas_festival.html",
            {"festival": festival, "formulario": formulario},
        )


class ConfirmacionCompraFestival(View):
    def get(self, request, pk, unidades, tipo_entrada):
        festival = get_object_or_404(Festival, pk=pk)
        precio = festival.get_precio_entrada(tipo_entrada)
        usuario = request.user
        importe = float(precio) * unidades

        return render(
            request,
            "tickets_app/confirmacion_compra_festival.html",
            {
                "festival": festival,
                "unidades": unidades,
                "usuario": usuario,
                "importe": importe,
                "tipo_entrada": tipo_entrada,
            },
        )

    def post(self, request, pk, unidades, tipo_entrada):
        festival = get_object_or_404(Festival, pk=pk)
        precio = festival.get_precio_entrada(tipo_entrada)
        usuario = request.user

        importe = float(precio) * unidades

        if tipo_entrada == "platino":
            festival.entradas_platino -= unidades
        elif tipo_entrada == "oro":
            festival.entradas_oro -= unidades
        else:
            festival.entradas_general -= unidades

        festival.boletos_disponibles -= unidades
        festival.save()

        ReservaFestival.objects.create(
            festival_reserva=festival,
            cliente_reserva=usuario,
            cantidad_tickets=unidades,
            importe=importe,
            tipo_entrada=tipo_entrada,
        )
        return redirect("listar_reservas_festival_usuario")



class ReservarPlazaBus(View):
    def get(self, request, pk):
        autobus = get_object_or_404(Autobus, pk=pk)
        formulario = ReservaAutobusForm()
        return render(
            request,
            "tickets_app/reservar_plaza_bus.html",
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
            "tickets_app/reservar_plaza_bus.html",
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

    def post(self, request,**kwargs):
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
        return redirect("listar_reservas_autobus_usuario")
    
class ReservarPlazaParking(View):
    def get(self, request, pk):
        parking = get_object_or_404(Parking, pk=pk)
        formulario = ReservaParkingForm()
        return render(
            request,
            "tickets_app/reservar_plaza_parking.html",
            {"parking": parking, "formulario": formulario},
        )

    def post(self, request, pk):
        formulario = ReservaParkingForm(request.POST)
        if formulario.is_valid():
            parking = get_object_or_404(Parking, pk=pk)
            unidades = formulario.cleaned_data["cantidad_tickets"]
            return redirect(
                "confirmar_compra_parking",
                pk, 
                unidades,
            )
        return render(
            request,
            "tickets_app/comprar_entradas_parking.html",
            {"parking": parking, "formulario": formulario},
        )
        
class ConfirmacionCompraParking(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        parking = get_object_or_404(Parking, pk=pk)
        unidades = kwargs.get("unidades", None)
        usuario = request.user
        importe = parking.precio * unidades

        return render(
            request,
            "tickets_app/confirmacion_compra_parking.html",
            {
                "parking": parking,
                "unidades": unidades,
                "usuario": usuario,
                "importe": importe,
            },
        )

    def post(self,request, **kwargs):
        pk = kwargs.get("pk", None)
        parking = get_object_or_404(Parking, pk=pk)
        unidades = kwargs.get("unidades", None)
        usuario = self.request.user
        importe = parking.precio * unidades

        parking.plazas_disponibles -= unidades
        parking.save()
        ReservaParking.objects.create(
            parking_reserva=parking,
            cliente_reserva=usuario,
            cantidad_tickets=unidades,
            importe=importe,
        )
        return redirect("listar_reservas_parking_usuario")
    
