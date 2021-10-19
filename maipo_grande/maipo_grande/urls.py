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
from maipo_grande.test_de_impresion import printaproductor
from maipo_grande.dao.productordao import buscarProductor
from maipo_grande.view import AdministradorViewSet, ClienteExtranjeroViewSet, ClienteNacionalViewSet, ConcretacionventaViewSet, ProductorViewSet, ContratoventaextranjeroViewSet, PedidointernacionalViewSet,ContratoproductorViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register('productor',ProductorViewSet)
router.register('administrador',AdministradorViewSet)
router.register('clienteextranjero',ClienteExtranjeroViewSet)
router.register('clientenacional',ClienteNacionalViewSet)
router.register('concretacionventa',ConcretacionventaViewSet)
router.register('contratoventaextranjero',ContratoventaextranjeroViewSet)
router.register('pedidointernacional',PedidointernacionalViewSet)
router.register('contratoproductor',ContratoproductorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('test',printaproductor),
    path('api/',include(router.urls)),
]