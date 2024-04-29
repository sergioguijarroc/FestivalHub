from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ComprarEntradasBus, ConfirmacionCompraBus
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    #AutoBus
    path(
        "comprar_entradas_bus/<int:pk>",
        login_required(ComprarEntradasBus.as_view()),
        name="comprar_entradas_bus",
    ),
    path(
        "confirmar_compra_bus/<int:pk><int:unidades>",
        login_required(ConfirmacionCompraBus.as_view()),
        name="confirmar_compra_bus",
    ),
]
