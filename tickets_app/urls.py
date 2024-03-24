from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ComprarEntradas, ConfirmacionCompra
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(
        "comprar_entradas/<int:pk>",
        login_required(ComprarEntradas.as_view()),
        name="comprar_entradas",
    ),
    path(
        "confirmar_compra/<int:pk><int:unidades>",
        login_required(ConfirmacionCompra.as_view()),
        name="confirmar_compra",
    ),
]
