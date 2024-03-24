from django.contrib import admin
from .models import Artista, Ubicacion, Concierto, Notificacion

# Register your models here.
admin.site.register(Artista)
admin.site.register(Ubicacion)
admin.site.register(Concierto)
admin.site.register(Notificacion)
