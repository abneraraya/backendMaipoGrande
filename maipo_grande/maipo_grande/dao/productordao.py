from maipo_grande.modelo.models import  Productor
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet

def buscarProductor(id):
    try:
     productor =Productor.objects.get(idproductor=id)
     print(productor)
     print(list(productor.values()))
     print("resultadoExitoso")
    except EmptyResultSet as e:
        print("no se encuentran registros")

def buscarTodosLosProductores():
    try: 
       productores =Productor.objects.all().order_by('idproductor')
       print(productores)
       print(list(productores.values()))
    except EmptyResultSet as e:
        print("no se encuentran registros")        

def eliminarProductorPorId(id):
   try:
       productor=Productor.objects.get(id=id)
       productor.delete()
   except EmptyResultSet as e:
        print("no se encuentran registros") 

def agregarProductor(productor):
    try:
        productor
    except EmptyResultSet as e:
        print ("no se pudo guardar el productor")    
