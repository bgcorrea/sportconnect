from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Deporte, Cancha
from .serializers import DeporteSerializer, CanchaSerializer


class DeporteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Deporte.objects.all()
    serializer_class = DeporteSerializer
    permission_classes = [AllowAny]


class CanchaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cancha.objects.filter(activa=True)
    serializer_class = CanchaSerializer
    permission_classes = [AllowAny]
