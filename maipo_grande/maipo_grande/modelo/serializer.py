from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Administrador, Clientenacional, Contratoproductor, Contratoventaextranjero, Pedidointernacional, Pedidonacional, Productor, Clienteextranjero,Concretacionventa, Productos,Transportista,Vehiculo,Subastatransportenacional,Subastapedidonacional,Subastatransinternacional

## Serializador de productor
class ProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productor
        fields =['idproductor',
                 'rut',
                 'nombre',
                 'alias',
                 'direccion',
                 'telefono',
                 'username',
                 'userpass'
                ]

## Serializador de adminitrador
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Administrador
        fields =['idadministrador',
                 'run', 
                 'nombre',
                 'puesto',
                 'username',
                 'userpass'
                ]

## Serializador de cliente extranjero
class ClienteExtranjeroSerializer (serializers.ModelSerializer):
    class Meta:
        model=Clienteextranjero
        fields=['idclienteextranjero',
                'nombre',
                'direccion',
                'username',
                'userpass'
               ]

## Serializador de cliente nacional
class ClienteNacionalSerializer (serializers.ModelSerializer):
    class Meta:
        model=Clientenacional
        fields=['idclientenacional',
                'nombre',
                'direccion',
                'username',
                'userpass'
               ]

## Serializador de concretacionventa
class ConcretacionventaSerializer (serializers.ModelSerializer):
    class Meta:
        model =Concretacionventa
        fields =['idconcretacionventa',
                 'embalaje',
                 'cantidad',
                 'fechapago',
                 'nombreseguro',
                 'tipoenvio',
                 'costostransportes',
                 'impuestosaduanero',
                 'pagodeservicios',
                 'comisionempresa',
                 'idcontratoventaextranjero'
                ]

## Serializador de contrato venta extranjero
class ContratoventaextranjeroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contratoventaextranjero
        fields=['idcontratoventaextranjero',
                'fechainicio',
                'fechatermino',
                'esrenovable',
                'fechadepago',
                'obligaciones',
                'idadministrador',
                'idpedidointernacional',
                'idclienteextranjero']

## Serializador  de contrato productor
class ContratoproductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratoproductor
        fields=['idcontratoproductor',
                'fechainicio',
                'fechatermino',
                'esrenovable',
                'fechadepago',
                'obligaciones',
                'idproductor'
               ]

## Serializador de pedido internacionacional
class PedidoInternacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pedidointernacional
        fields=['idpedidointernacional',
                'idclienteextranjero',
                'producto1',
                'cantidad1',
                'embalaje1',
                'producto2',
                'cantidad2',
                'embalaje2',
                'producto3',
                'cantidad3',
                'embalaje3',
                'producto4',
                'cantidad4',
                'embalaje4',
                'producto5',
                'cantidad5',
                'embalaje5',
                'producto6',
                'cantidad6',
                'embalaje6',
                'producto7',
                'cantidad7',
                'embalaje7',
                'producto8',
                'cantidad8',
                'embalaje8',
                'producto9',
                'cantidad9',
                'embalaje9',
                'producto10',
                'cantidad10',
                'embalaje10',
               ]

## Serializador de pedido nacional
class PedidonacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model =Pedidonacional
        fields=['idpedidonacional',
                'idclientenacional',
                'producto1',
                'cantidad1',
                'embalaje1',
                'producto2',
                'cantidad2',
                'embalaje2',
                'producto3',
                'cantidad3',
                'embalaje3',
                'producto4',
                'cantidad4',
                'embalaje4',
                'producto5',
                'cantidad5',
                'embalaje5',
                'producto6',
                'cantidad6',
                'embalaje6',
                'producto7',
                'cantidad7',
                'embalaje7',
                'producto8',
                'cantidad8',
                'embalaje8',
                'producto9',
                'cantidad9',
                'embalaje9',
                'producto10',
                'cantidad10',
                'embalaje10',
               ]

## Serializador de productos
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields=['idproductos',
                'descripcion',
                'calidad',
                'precio',
                'estado',
                'embalaje',
                'cantidad',
                'idproductor'
               ]

## Serializador de transportista
class TransportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transportista
        fields=['idtransportista',
                'rut',
                'nombre',
                'direccion',
                'username',
                'userpass'
               ]

## Serializador de vehiculo
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehiculo
        fields=['idvehiculo',
                'tipovehiculo',
                'patente',
                'cargamaxima',
                'tipodecarga',
                'cadenadefrio',
                'idtransportista'
               ] 

## Serializador de subasta transporte nacional           
class SubastatransportenacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subastatransportenacional
        fields=['idsubastatransportenacional',
                'fechainicio',
                'fechatermino',
                'fecharealizacion',
                'direccionorigen',
                'direccionentrega',
                'idadministrador',
                'idpedidonacional'
               ]

## Serializador subasta pedido nacional
class SubastapedidonacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subastapedidonacional
        fields=['idsubastapedidonacional',
                'fechainicio',
                'fechatermino',
                'fechaentregadeproductos',
                'idadministrador',
                'idpedidonacional'
               ]

class SubastatransinternacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subastatransinternacional
        fields=['idsubastatransinternacional',
                'fechainicio',
                'fechatermino',
                'fecharealizacion',
                'direccionorigen',
                'idcontratoventaextranjero',
                'direccionentrega',
                'idadministrador',
               ]