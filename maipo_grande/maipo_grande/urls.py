"""maipo_grande URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from maipo_grande.view import AdministradorViewSet, ClienteExtranjeroViewSet, ClienteNacionalViewSet, ConcretacionventaViewSet, ProductorViewSet, ContratoventaextranjeroViewSet, PedidointernacionalViewSet,ContratoproductorViewSet,PedidonacionalViewSet,ProductosViewSet,TransportistaViewSet,VehiculoViewSet,SubastatransportenacionalViewSet,SubastapedidonacionalViewSet,SubastatransinternacionaleViewSet,PostulacioninternacionalViewSet,PostulacionnacionalViewSet,SubastapedidointernacionalViewSet,PostulaciontransnacionalViewSet,PostulaciontraninternacionalViewSet,InformeventaglobalViewSet,InformeventapersonalViewSet
from rest_framework import routers, views


router=routers.DefaultRouter()
router.register('productor',ProductorViewSet)
router.register('administrador',AdministradorViewSet)
router.register('clienteextranjero',ClienteExtranjeroViewSet)
router.register('clientenacional',ClienteNacionalViewSet)
router.register('concretacionventa',ConcretacionventaViewSet)
router.register('contratoventaextranjero',ContratoventaextranjeroViewSet)
router.register('pedidointernacional',PedidointernacionalViewSet)
router.register('contratoproductor',ContratoproductorViewSet)
router.register('pedidonacional',PedidonacionalViewSet)
router.register('productos',ProductosViewSet)
router.register('transportista',TransportistaViewSet)
router.register('vehiculo',VehiculoViewSet)
router.register('subastatransportenacional',SubastatransportenacionalViewSet)
router.register('subastapedidonacional',SubastapedidonacionalViewSet)
router.register('subastatransporteinternacional',SubastatransinternacionaleViewSet)
router.register('postulacioninternacional',PostulacioninternacionalViewSet)
router.register('postulacionnacional',PostulacionnacionalViewSet)
router.register('subastapedidointernacional',SubastapedidointernacionalViewSet)
router.register('postulaciontransportenacional',PostulaciontransnacionalViewSet)
router.register('postulaciontransporteinternacional',PostulaciontraninternacionalViewSet)
router.register('informedeventaglobal',InformeventaglobalViewSet)
router.register('informeventapersonal',InformeventapersonalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('test',printaproductor),
    path('api/',include(router.urls)),
]
