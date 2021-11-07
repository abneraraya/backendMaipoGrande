from maipo_grande.modelo.models import  Administrador
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet

def buscarAdminsitrador (id):
         administrador =Administrador.objects.filter(idadministrador=2)
         print(administrador)
         return{
            administrador
         }

