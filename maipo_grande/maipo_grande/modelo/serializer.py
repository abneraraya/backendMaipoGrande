from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Administrador, Clientenacional, Contratoproductor, Contratoventaextranjero, Pedidointernacional, Pedidonacional, Productor, Clienteextranjero,Concretacionventa, Productos,Transportista,Vehiculo,Subastatransportenacional,Subastapedidonacional,Subastatransinternacional,Postulacioninternacional,Postulacionnacional,Subastapedidointernacional,Postulaciontransnacional,Postulaciontransinternacional,Informeventaglobal, Informeventapersonal

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

## Serializador de Postulacion Internacional
class PostulacioninternacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postulacioninternacional
        fields=['idpostulacioninternacional',
                'idproductor',
                'idsubastapedidointernacional',
                'fruta1',
                'cantidad1',
                'precio1',
                'fruta2',
                'cantidad2',
                'precio2', 
                'fruta3',
                'cantidad3',
                'precio3', 
                'fruta4',
                'cantidad4',
                'precio4', 
                'fruta5',
                'cantidad5',
                'precio5', 
                'fruta6',
                'cantidad6',
                'precio6', 
                'fruta7',
                'cantidad7',
                'precio7', 
                'fruta8',
                'cantidad8',
                'precio8', 
                'fruta9',
                'cantidad9',
                'precio9', 
                'fruta10',
                'cantidad10',
                'precio10',
                'ganadora'  
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

## Serializador Subasta transporte internacional
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

## Serializador postulacion nacional
class PostulacionnacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postulacionnacional
        fields=['idpostulacionnacional',
                'idproductor',
                'idsubastapedidonacional',
                'fruta1',
                'cantidad1',
                'precio1',
                'fruta2',
                'cantidad2',
                'precio2', 
                'fruta3',
                'cantidad3',
                'precio3', 
                'fruta4',
                'cantidad4',
                'precio4', 
                'fruta5',
                'cantidad5',
                'precio5', 
                'fruta6',
                'cantidad6',
                'precio6', 
                'fruta7',
                'cantidad7',
                'precio7', 
                'fruta8',
                'cantidad8',
                'precio8', 
                'fruta9',
                'cantidad9',
                'precio9', 
                'fruta10',
                'cantidad10',
                'precio10',
                'ganadora'  
            ]

## Serializador subasta pedido internacional
class SubastapedidointernacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subastapedidointernacional
        fields=['idsubastapedidointernacional',
                'fechainicio',
                'fechatermino',
                'fechaentregadeproductos',
                'idadministrador',
                'idpedidointernacional'
               ]

## Serializador Postulacion transporte nacional
class PostulaciontransnacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postulaciontransnacional
        fields=['idpostulacionnacional',
                'idtransportista',
                'idsubastatransportenacional',
                'tipovehiculo1',
                'patente1',
                'cadenadefrio1',
                'tipovehiculo2',
                'patente2',
                'cadenadefrio2',
                'tipovehiculo3',
                'patente3',
                'cadenadefrio3',
                'tipovehiculo4',
                'patente4',
                'cadenadefrio4',
                'tipovehiculo5',
                'patente5',
                'cadenadefrio5',
                'ganadora'
               ]
 
## Serializador postulacion transporte internacional
class PostulaciontransinternacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postulaciontransinternacional
        fields=['idpostulacion',
                'idtransportista',
                'idsubastatransinternacional',
                'tipovehiculo1',
                'patente1',
                'cadenadefrio1',
                'tipovehiculo2',
                'patente2',
                'cadenadefrio2',
                'tipovehiculo3',
                'patente3',
                'cadenadefrio3',
                'tipovehiculo4',
                'patente4',
                'cadenadefrio4',
                'tipovehiculo5',
                'patente5',
                'cadenadefrio5',
                'ganadora'
               ]

## Serializador de informes de venta globales
class InformeventaglobalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Informeventaglobal
        fields=['idinformeventaglobal',
                'precioventa',
                'cantidadvendida',
                'gananciatotal',
                'idcontratoventaextranjero',
                'idproductor',
                'idconcretacionventa'
               ]

class  InformeventapersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model= Informeventapersonal
        fields=['idinformeventapersonal',
                'precioventa',
                'cantidadvendida',
                'gananciapersonal',
                'idcontratoventaextranjero',
                'idproductor',
                'idconcretacionventa'
               ]