
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from maipo_grande.modelo.models import Productor
from django.shortcuts import render
import json

def printaproductor(request):
    try:
        productores =Productor.objects.all().order_by('idproductor')
        print(productores)
        print(list(productores.values()))
        productor={}
        asd=Productor.objects.get(idproductor=2)
        productor={#'idproductor':asd.idproductor,
                   'rut':asd.rut,
                   'nombre':asd.nombre,
                   'alias':asd.alias,
                   'direccion':asd.direccion,
                   'telefono':asd.telefono,
                   'username':asd.username,
                   'userpass':asd.userpass}
        print(productor)
        print("resultadoExitoso")
        print("aaaaaaaaaaaaaaaaaaaaaaaa")
       

    except EmptyResultSet as e:
        print("no se encuentran registros")

    return render(request.post,)
