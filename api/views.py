from rest_framework import (generics,status)
from rest_framework.response import Response
from api.models import Plat
from api.serializers import PlatSerializer
from rest_framework.views import APIView
from django.views.generic import TemplateView
from rest_framework import viewsets

class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer

class PlatListCreate(generics.ListCreateAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer

    def delete(self, request, *args, **kwargs):
        if not request.user.is_superuser:  # Limiter la suppression totale aux administrateurs
            return Response({'detail': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)

        Plat.objects.all().delete()
        return Response({'detail': 'All objects deleted'}, status=status.HTTP_204_NO_CONTENT)

class PLatView(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title', None)
        if title:
            ada_licious = Plat.objects.filter(title__icontains=title)
        else:
            ada_licious = Plat.objects.all()

        serializer = PlatSerializer(ada_licious, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)







