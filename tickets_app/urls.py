from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ConfirmacionCompraParking, ReservarPlazaBus, ConfirmacionCompraBus, ReservarPlazaParking,ComprarEntradasFestival,ConfirmacionCompraFestival,MapaZonasFestival,AñadirEntradasFestival
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #Festival
    path("mapa_interactivo/<int:pk>",MapaZonasFestival.as_view(),name="mapa_interactivo"),
    path("añadir_entradas_festival/<int:pk>",AñadirEntradasFestival.as_view(),name="añadir_entradas_festival"),
    path(
        "comprar_entradas_festival/<int:pk><str:tipo_entrada>",
        login_required(ComprarEntradasFestival.as_view()),
        name="comprar_entradas_festival",
    ),
    path(
        "confirmar_compra_festival/<int:pk>/<int:unidades>/<str:tipo_entrada>",
        login_required(ConfirmacionCompraFestival.as_view()),
        name="confirmar_compra_festival",
    ),
    
    #AutoBus
    path(
        "reservar_plaza_bus/<int:pk>",
        login_required(ReservarPlazaBus.as_view()),
        name="reservar_plaza_bus",
    ),
    path(
        "confirmar_compra_bus/<int:pk><int:unidades>",
        login_required(ConfirmacionCompraBus.as_view()),
        name="confirmar_compra_bus",
    ),
    
    #Parking
    path(
        "reservar_plaza_parking/<int:pk>",
        login_required(ReservarPlazaParking.as_view()),
        name="reservar_plaza_parking",
    ),
    path(
        "confirmar_compra_parking/<int:pk><int:unidades>",
        login_required(ConfirmacionCompraParking.as_view()),
        name="confirmar_compra_parking",
    ),
]
