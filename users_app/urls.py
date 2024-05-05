from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListarReservasFestivalUsuario,ListarReservasUsuario,ListarReservasAutobusUsuario,ListarReservasParkingUsuario
from django.contrib.auth.decorators import login_required
from .views import register

urlpatterns = [
    
    path("reservas/",
        login_required(ListarReservasUsuario.as_view()),
        name="listar_reservas_usuario"
        ),
    path(
        "reservas/festivales",
        login_required(ListarReservasFestivalUsuario.as_view()),
        name="listar_reservas_festival_usuario",
    ),
    path(
        "reservas/autobuses",
        login_required(ListarReservasAutobusUsuario.as_view()),
        name="listar_reservas_autobus_usuario",
    ),
    path(
        "reservas/parkings",
        login_required(ListarReservasParkingUsuario.as_view()),
        name="listar_reservas_parking_usuario",
    ),

    path("register/", register, name="register"),
    
]
