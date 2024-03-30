from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    FestivalListView,
    FestivalCreateView,
)

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", FestivalListView.as_view(), name="festival_list"),
    path("create/", staff_member_required(FestivalCreateView.as_view()), name="festival_create"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)