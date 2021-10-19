from rest_framework import serializers, viewsets


from maipo_grande.modelo.models import Administrador, Clienteextranjero, Clientenacional, Concretacionventa, Contratoventaextranjero, Pedidointernacional, Productor,Contratoproductor
from .modelo import serializer


class ProductorViewSet(viewsets.ModelViewSet):
    queryset= Productor.objects.all()
    serializer_class=serializer.ProductorSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset=Administrador.objects.all()
    serializer_class=serializer.AdministradorSerializer   

class ClienteExtranjeroViewSet(viewsets.ModelViewSet):
    queryset=Clienteextranjero.objects.all()
    serializer_class=serializer.ClienteExtranjeroSerializer

class ClienteNacionalViewSet(viewsets.ModelViewSet):
    queryset=Clientenacional.objects.all()
    serializer_class=serializer.ClienteNacionalSerializer

class ConcretacionventaViewSet(viewsets.ModelViewSet):
    queryset=Concretacionventa.objects.all()
    serializer_class=serializer.ConcretacionventaSerializer

class ContratoventaextranjeroViewSet(viewsets.ModelViewSet):
    queryset=Contratoventaextranjero.objects.all()
    serializer_class=serializer.ContratoventaextranjeroSerializer

class PedidointernacionalViewSet(viewsets.ModelViewSet):
    queryset=Pedidointernacional.objects.all()
    serializer_class=serializer.PedidoInternacionalSerializer

class ContratoproductorViewSet(viewsets.ModelViewSet):
    queryset=Contratoproductor.objects.all()
    serializer_class=serializer.ContratoproductorSerializer