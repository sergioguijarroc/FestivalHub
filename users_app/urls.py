from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListarReservasUsuario
from django.contrib.auth.decorators import login_required
from .views import register

urlpatterns = [
    path(
        "reservas/",
        login_required(ListarReservasUsuario.as_view()),
        name="listar_reservas_usuario",
    ),
    path("register/", register, name="register"),
]
