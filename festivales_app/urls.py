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
)

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", FestivalListView.as_view(), name="festival_list"),
    path("create/", staff_member_required(FestivalCreateView.as_view()), name="festival_create"),
    path("<int:pk>/", FestivalDetailView.as_view(), name="festival_detail"),
    path("update/<int:pk>", staff_member_required(FestivalUpdateView.as_view()), name="festival_update"),
    path("delete/<int:pk>", staff_member_required(FestivalDeleteView.as_view()), name="festival_delete"),
    #Autobuses
    
    path("autobus/create/<int:festival_pk>/", AutobusCreateView.as_view(), name="autobus_create"),
    path("autobus/list/<int:festival_pk>/", AutobusListView.as_view(), name="autobus_list"),
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)