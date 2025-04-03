from rest_framework import serializers
from api.models import Plat


class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = ["id", "plate", "description", "image"]