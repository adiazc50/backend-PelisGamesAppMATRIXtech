from rest_framework import serializers
from .models import Cliente
from .models import Juegos
from .models import Prestamo

class ClienteSerializer(serializers.ModelSerializer):
    class MetaCliente:
        model = Cliente
        fields = ('idCliente', 'nombreCliente', 'direccion','telefono','celular','email')

class JuegosSerializer(serializers.ModelSerializer):
    class MetaJuegos:
        model = Juegos
        fields = ('idCliente', 'nombreCliente', 'direccion','telefono','celular','email')

class PrestamoSerializer(serializers.ModelSerializer):
    class MetaPrestamo:
        model = Prestamo
        fields = ('idCliente', 'nombreCliente', 'direccion','telefono','celular','email')
