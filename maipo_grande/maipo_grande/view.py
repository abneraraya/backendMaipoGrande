from django.db.models import query
from rest_framework import serializers, viewsets
from .modelo import serializer,models


class ProductorViewSet(viewsets.ModelViewSet):
    queryset= models.Productor.objects.all()
    serializer_class=serializer.ProductorSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset=models.Administrador.objects.all()
    serializer_class=serializer.AdministradorSerializer   

class ClienteExtranjeroViewSet(viewsets.ModelViewSet):
    queryset=models.Clienteextranjero.objects.all()
    serializer_class=serializer.ClienteExtranjeroSerializer

class ClienteNacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Clientenacional.objects.all()
    serializer_class=serializer.ClienteNacionalSerializer

class ConcretacionventaViewSet(viewsets.ModelViewSet):
    queryset=models.Concretacionventa.objects.all()
    serializer_class=serializer.ConcretacionventaSerializer

class ContratoventaextranjeroViewSet(viewsets.ModelViewSet):
    queryset=models.Contratoventaextranjero.objects.all()
    serializer_class=serializer.ContratoventaextranjeroSerializer

class PedidointernacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Pedidointernacional.objects.all()
    serializer_class=serializer.PedidoInternacionalSerializer

class ContratoproductorViewSet(viewsets.ModelViewSet):
    queryset=models.Contratoproductor.objects.all()
    serializer_class=serializer.ContratoproductorSerializer

class PedidonacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Pedidonacional.objects.all()
    serializer_class=serializer.PedidonacionalSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset=models.Productos.objects.all()
    serializer_class=serializer.ProductosSerializer

class TransportistaViewSet(viewsets.ModelViewSet):
    queryset=models.Transportista.objects.all()
    serializer_class=serializer.TransportistaSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset=models.Vehiculo.objects.all()
    serializer_class=serializer.VehiculoSerializer 

class SubastatransportenacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Subastatransportenacional.objects.all()
    serializer_class=serializer.SubastatransportenacionalSerializer

class SubastapedidonacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Subastapedidonacional.objects.all()
    serializer_class=serializer.SubastapedidonacionalSerializer

class SubastatransinternacionaleViewSet(viewsets.ModelViewSet):
    queryset=models.Subastatransinternacional.objects.all()
    serializer_class=serializer.SubastatransinternacionalSerializer

class PostulacioninternacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Postulacioninternacional.objects.all()
    serializer_class=serializer.PostulacioninternacionalSerializer

class PostulacionnacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Postulacionnacional.objects.all()
    serializer_class=serializer.PostulacionnacionalSerializer

class SubastapedidointernacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Subastapedidointernacional.objects.all()
    serializer_class=serializer.SubastapedidointernacionalSerializer

class PostulaciontransnacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Postulaciontransnacional.objects.all()
    serializer_class=serializer.PostulaciontransnacionalSerializer

class VehiculoTestViewSet(viewsets.ModelViewSet):
    queryset=models.Vehiculo.objects.filter(idtransportista=2)
    serializer_class=serializer.VehiculoSerializer

class PostulaciontraninternacionalViewSet(viewsets.ModelViewSet):
    queryset=models.Postulaciontransinternacional.objects.all()
    serializer_class=serializer.PostulaciontransinternacionalSerializer

class InformeventaglobalViewSet(viewsets.ModelViewSet):
    queryset=models.Informeventaglobal.objects.all()
    serializer_class=serializer.InformeventaglobalSerializer

class InformeventapersonalViewSet(viewsets.ModelViewSet):
    queryset=models.Informeventapersonal.objects.all()
    serializer_class=serializer.InformeventapersonalSerializer