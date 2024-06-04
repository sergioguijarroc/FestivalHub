from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ListarConciertosFestival,
    ConciertoCreateView,
    ConciertoDetailView,
    ConciertoDeleteView,
    ConciertoUpdateView,
    ConciertoReview,
    ListarConciertosMasVendidos,
    ArtistaListView,
    ArtistaCreateView,
    ArtistaDetailView,
    ArtistaDeleteView,
    ArtistaUpdateView,
)
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


urlpatterns = [
    #path("list/<int:pk>", ListarConciertosFestival.as_view(), name="concierto_list"),
    path("list/", ListarConciertosFestival.as_view(), name="concierto_list"),
    path("detail/<int:pk>", ConciertoDetailView.as_view(), name="concierto_detail"),
    path(
        "create/<int:festival_pk>",
        staff_member_required(ConciertoCreateView.as_view()),
        name="concierto_create",
    ),
    path(
        "delete/<int:pk>",
        staff_member_required(ConciertoDeleteView.as_view()),
        name="concierto_delete",
    ),
    path(
        "update/<int:pk>",
        staff_member_required(ConciertoUpdateView.as_view()),
        name="concierto_update",
    ),
    path(
        "review/<int:pk>",
        login_required(ConciertoReview.as_view()),
        name="concierto_review",
    ),
    # Artistas    path("artistas/", ArtistaListView.as_view(), name="artista_list"),
    path(
        "artistas/detail/<int:pk>", ArtistaDetailView.as_view(), name="artista_detail"
    ),
    path(
        "artistas/create/",
        staff_member_required(ArtistaCreateView.as_view()),
        name="artista_create",
    ),
    path(
        "artistas/delete/<int:pk>",
        staff_member_required(ArtistaDeleteView.as_view()),
        name="artista_delete",
    ),
    path(
        "artistas/update/<int:pk>",
        staff_member_required(ArtistaUpdateView.as_view()),
        name="artista_update",
    ),
    path(
        "conciertos_mas_vendidos/",
        ListarConciertosMasVendidos.as_view(),
        name="concierto_top_ventas",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# hola
