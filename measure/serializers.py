from rest_framework import serializers
from .models import Cliente
from .models import Juegos
from .models import Prestamo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('idCliente', 'nombreCliente', 'direccion','telefono','celular','email')
 


class JuegosSerializer(serializers.ModelSerializer):
    class MetaJuegos:
        model = Juegos
        fields = ('titulo', 'nombreJuego', 'ano','protagonistas','director','productor','plataforma','precio')

class PrestamoSerializer(serializers.ModelSerializer):
    class MetaPrestamo:
        model = Prestamo
        fields = ('idPrestamos', 'nombreCliente', 'idCliente','nombreJuego','fechaPrestamo','fechaVence','Correo')
