from rest_framework import generics
from .models import Plat
from .serializers import PlatSerializer
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_api(request):
    return Response({"message": "Connexion réussie depuis Django !"})

class PlatListCreate(generics.ListCreateAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer

@api_view(['GET'])
def test_api(request):
    return Response({"message": "Connexion réussie depuis Django !"})







