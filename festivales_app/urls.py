from django.urls import path

from .views import (
    FestivalListView
)

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", FestivalListView.as_view(), name="festival_list"),
]