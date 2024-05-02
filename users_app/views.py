from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from concerts_app.models import Concierto
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.utils import timezone
from tickets_app.models import ReservaFestival

# Create your views here.


class ListarReservasFestivalUsuario(View):
    def get(self, request):
        reservas = ReservaFestival.objects.filter(cliente_reserva=self.request.user)
        # fecha_actual = datetime.now()
        fecha_actual = timezone.now()
        return render(
            request,
            "users_app/festival_usuario_list.html",
            {"reservas": reservas, "fecha_actual": fecha_actual},
        )
        
class ListarReservasUsuario(View):
    def get(self,request):
        return render(request,"users_app/reservas_usuario.html")


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("festival_list")
    else:
        form = RegisterForm()
    return render(request, "users_app/register.html", {"form": form})
