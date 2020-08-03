from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .models import Juegos
from .models import Prestamo
from .serializers import ClienteSerializer

from .serializers import PrestamoSerializer
from .serializers import JuegosSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('-created')
    serializer_class = ClienteSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all().order_by('-created')
    serializer_class = PrestamoSerializer

class JuegosViewSet(viewsets.ModelViewSet):
    queryset = Juegos.objects.all().order_by('-created')
    serializer_class = JuegosSerializer