from rest_framework import serializers
from api.models import Plat


class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = '__all__'  # Inclure tous les champs
