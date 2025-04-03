from rest_framework import generics
from .models import Plat
from .serializers import PlatSerializer

class PlatListCreate(generics.ListCreateAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer







