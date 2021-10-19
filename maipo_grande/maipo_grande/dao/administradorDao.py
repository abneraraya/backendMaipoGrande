from maipo_grande.modelo.models import  Administrador
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet

def buscarAdminsitrador (id):
      try:
         administrador =Administrador.objects.get(idproductor=id)
         print(administrador)
         print(list(administrador.values()))
         print("resultadoExitoso")
      except EmptyResultSet as e:
         print("no se encuentran registros")

