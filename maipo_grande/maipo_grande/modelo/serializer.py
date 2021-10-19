from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Administrador, Clientenacional, Contratoproductor, Contratoventaextranjero, Pedidointernacional, Productor, Clienteextranjero,Concretacionventa

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

class ClienteExtranjeroSerializer (serializers.ModelSerializer):
    class Meta:
        model=Clienteextranjero
        fields=['idclienteextranjero',
                'nombre',
                'direccion',
                'username',
                'userpass'
               ]

class ClienteNacionalSerializer (serializers.ModelSerializer):
    class Meta:
        model=Clientenacional
        fields=['idclientenacional',
                'nombre',
                'direccion',
                'username',
                'userpass'
               ]

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