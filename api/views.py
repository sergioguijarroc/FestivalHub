""" from django.shortcuts import render
from .serializers import ConciertoSerializer
from rest_framework import viewsets, permissions
from concerts_app.models import Concierto


class ConciertoViewSet(viewsets.ModelViewSet):
    queryset = Concierto.objects.all()
    serializer_class = ConciertoSerializer
    permission_classes = [permissions.AllowAny]
 """