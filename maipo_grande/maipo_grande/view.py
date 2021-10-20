from django.db.models import query
from rest_framework import serializers, viewsets
from maipo_grande.modelo.models import Administrador, Clienteextranjero, Clientenacional, Concretacionventa, Contratoventaextranjero, Pedidointernacional, Pedidonacional, Productor,Contratoproductor,Productos,Transportista,Vehiculo,Subastatransportenacional,Subastapedidonacional,Subastatransinternacional
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

class PedidonacionalViewSet(viewsets.ModelViewSet):
    queryset=Pedidonacional.objects.all()
    serializer_class=serializer.PedidonacionalSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset=Productos.objects.all()
    serializer_class=serializer.ProductosSerializer

class TransportistaViewSet(viewsets.ModelViewSet):
    queryset=Transportista.objects.all()
    serializer_class=serializer.TransportistaSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset=Vehiculo.objects.all()
    serializer_class=serializer.VehiculoSerializer 

class SubastatransportenacionalViewSet(viewsets.ModelViewSet):
    queryset=Subastatransportenacional.objects.all()
    serializer_class=serializer.SubastatransportenacionalSerializer

class SubastapedidonacionalViewSet(viewsets.ModelViewSet):
    queryset=Subastapedidonacional.objects.all()
    serializer_class=serializer.SubastapedidonacionalSerializer

class SubastatransinternacionaleViewSet(viewsets.ModelViewSet):
    queryset=Subastatransinternacional.objects.all()
    serializer_class=serializer.SubastatransinternacionalSerializer