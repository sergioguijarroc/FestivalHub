from rest_framework import serializers
from concerts_app.models import Concierto


class ConciertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concierto
        fields = "__all__"
