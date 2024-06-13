from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    FestivalListView,
    FestivalCreateView,
    FestivalDetailView,
    FestivalUpdateView,
    FestivalDeleteView,
    AutobusCreateView,
    AutobusListView,
    FestivalesConAutobusesListView,
    FestivalConParkingListView,
    ParkingCreateView,
    ParkingListView,
    ArtistasFestivalListView,
    ListarFestivalesMasVendidos,
    ConciertosDeUnFestival,
    
    
)

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #Festivales
    path("", FestivalListView.as_view(), name="festival_list"),
    path("create/", staff_member_required(FestivalCreateView.as_view()), name="festival_create"),
    path("<int:pk>/", FestivalDetailView.as_view(), name="festival_detail"),
    path("update/<int:pk>", staff_member_required(FestivalUpdateView.as_view()), name="festival_update"),
    path("delete/<int:pk>", staff_member_required(FestivalDeleteView.as_view()), name="festival_delete"),
    path("list_con_autobuses/", FestivalesConAutobusesListView.as_view(), name="festival_list_con_autobuses"),
    path("list_con_parking/", FestivalConParkingListView.as_view(), name="festival_list_con_parking"),
    path("artistas/<int:pk>/", ArtistasFestivalListView.as_view(), name="artistas_festival"),
    path("listar_festivales_mas_vendidos/", ListarFestivalesMasVendidos.as_view(), name="listar_festivales_mas_vendidos"),
    path("conciertos_del_festival/<int:festival_pk>",ConciertosDeUnFestival.as_view(), name="conciertos_festival"),
    #Autobuses
    path("autobus/create/<int:festival_pk>/", staff_member_required(AutobusCreateView.as_view()), name="autobus_create"),
    path("autobus/list/<int:festival_pk>/", AutobusListView.as_view(), name="autobus_list"),
    #Parkings
    path("parking/create/<int:festival_pk>/", staff_member_required(ParkingCreateView.as_view()), name="parking_create"),
    path("parking/list/<int:festival_pk>/", ParkingListView.as_view(), name="parking_list"),
    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)