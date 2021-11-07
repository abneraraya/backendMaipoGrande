# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.db.models.fields.related import ForeignKey

#listo
class Administrador(models.Model):
    idadministrador = models.AutoField(primary_key=True)
    run = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    userpass = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'administrador'
    
    def json_serializer_administrador(self):
     return {
             'idadministrador': self.idadministrador,
             'run': self.run,
             'nombre': self.nombre,
             'puesto': self.puesto,
             'username': self.username,
             'userpass': self.userpass,
            }


#listo
class Clienteextranjero(models.Model):
    idclienteextranjero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    userpass = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'clienteextranjero'
    
    def json_serializer_clienteextranjero(self):
        return{
               'idclienteextranjero':self.idclienteextranjero, 
               'nombre':self.nombre,
               'direccion':self.direccion,
               'username': self.username,
               'userpass': self.userpass,
        }

#listo
class Clientenacional(models.Model):
    idclientenacional = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    userpass = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clientenacional'
    
    def json_serializer_clientenacional(self):
     return{
            'idclientenacional':self.idclientenacional, 
            'nombre':self.nombre,
            'direccion':self.direccion,
            'username': self.username,
            'userpass': self.userpass,
        }
 
# listo serializador pero falta arreglar bd(ver todo)
class Concretacionventa(models.Model):
    idconcretacionventa = models.AutoField(primary_key=True)
    embalaje = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fechapago = models.DateField()
    nombreseguro = models.CharField(max_length=100)
    tipoenvio = models.CharField(max_length=100)
    costostransportes = models.IntegerField()
    impuestosaduanero = models.IntegerField()
    pagodeservicios = models.IntegerField()
    comisionempresa = models.IntegerField()
    idcontratoventaextranjero = models.ForeignKey( 'contratoventaextranjero', on_delete=models.CASCADE, db_column='idcontratoventaextranjero')

    class Meta:
        managed = False
        db_table = 'concretacionventa'
    
    def json_serializer_concretacionventa(self):
     return {
            'idconcretacionventa':self.idconcretacionventa,
            'embalaje':self.embalaje,
            'cantidad':self.cantidad,
            'fechapago':self.fechapago,
            'nombreseguro':self.nombreseguro,
            'tipoenvio':self.tipoenvio,
            'costostransporte':self.costostransportes,
            'impuestosaduaneros':self.impuestosaduanero,
            'pagodeservicios':self.pagodeservicios,
            'comisionempresa':self.comisionempresa,
            'idcontratoventaextranjero':self.idcontratoventaextranjero,
            'idinformeventaglobal':self.idinformeventaglobal
        }   

##listo
class Contratoproductor(models.Model):
    idcontratoproductor = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    esrenovable = models.IntegerField(blank=True, null=True)
    fechadepago = models.DateField()
    obligaciones = models.TextField() 
    idproductor = models.ForeignKey('Productor', on_delete=models.CASCADE, db_column='idproductor')

    class Meta:
        managed = False
        db_table = 'contratoproductor'
    
    def json_serializer_contratoProductor(self):
     return{
            'idcontratoproductor':self.idcontratoproductor,
            'fechainicio':self.fechainicio,
            'fechatermino':self.fechatermino,
            'esrenovable':self.esrenovable,
            'fechadepago':self.fechadepago,
            'obligaciones':self.obligaciones,
            'idproductor':self.idproductor
        }

##listo el serializador pero falta arreglar bd
class Contratoventaextranjero(models.Model):
    idcontratoventaextranjero = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    esrenovable = models.IntegerField(blank=True, null=True)
    fechadepago = models.DateField()
    obligaciones = models.TextField()
    idadministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, db_column='idadministrador')
    idpedidointernacional = models.OneToOneField('Pedidointernacional', on_delete=models.CASCADE, db_column='idpedidointernacional')
    idclienteextranjero = models.OneToOneField(Clienteextranjero, on_delete=models.CASCADE, db_column='idclienteextranjero')

    class Meta:
        managed = False
        db_table = 'contratoventaextranjero'
    
    def json_serializer_contratoventaextranjero(self):
     return{
            'idcontratoventaextranjero':self.idcontratoventaextranjero,
            'fechainicio':self.fechainicio,
            'fechatermino':self.fechatermino,
            'esrenovable':self.esrenovable,
            'fechadepago':self.fechadepago,
            'obligaciones':self.fechadepago,
            'idadministrador':self.idadministrador,
            'idpedidointernacional':self.idpedidointernacional,
            'idclienteextranjero':self.idclienteextranjero
     }

##listo
class Informeventaglobal(models.Model):
    idinformeventaglobal = models.AutoField(primary_key=True)
    precioventa = models.IntegerField()
    cantidadvendida = models.IntegerField()
    gananciatotal = models.IntegerField()
    idcontratoventaextranjero = models.OneToOneField(Contratoventaextranjero,on_delete=models.CASCADE, db_column='idcontratoventaextranjero')
    idproductor = models.OneToOneField('Productor', on_delete=models.CASCADE, db_column='idproductor')
    idconcretacionventa = models.OneToOneField(Concretacionventa, on_delete=models.CASCADE, db_column='idconcretacionventa')

    class Meta:
        managed = False
        db_table = 'informeventaglobal'
    
    def json_serializer_informeventaglobal(self):
     return{
            'idinformeventaglobal':self.idinformeventaglobal,
            'precioventa':self.precioventa,
            'cantidadvendida':self.cantidadvendida,
            'gananciatotal':self.gananciatotal,
            'idcontratoventaextranjero':self.idcontratoventaextranjero,
            'idproductor':self.idproductor,
            'idconcretacionventa':self.idconcretacionventa
     }


class Informeventapersonal(models.Model):
    idinformeventapersonal = models.AutoField(primary_key=True)
    precioventa = models.IntegerField()
    cantidadvendida = models.IntegerField()
    gananciapersonal = models.IntegerField()
    idcontratoventaextranjero = models.ForeignKey(Contratoventaextranjero, on_delete=models.CASCADE, db_column='idcontratoventaextranjero')
    idproductor = models.ForeignKey('Productor', on_delete=models.CASCADE, db_column='idproductor')
    idconcretacionventa = models.ForeignKey(Concretacionventa, on_delete=models.CASCADE, db_column='idconcretacionventa')

    class Meta:
        managed = False
        db_table = 'informeventapersonal'

    def json_serializer_informeventapersonal(self):
     return{
            'idinformeventaglobal':self.idinformeventapersonal,
            'precioventa':self.precioventa,
            'cantidadvendida':self.cantidadvendida,
            'gananciatotal':self.gananciapersonal,
            'idcontratoventaextranjero':self.idcontratoventaextranjero,
            'idproductor':self.idproductor,
            'idconcretacionventa':self.idconcretacionventa
     }

##listo
class Pedidointernacional(models.Model):
    idpedidointernacional = models.AutoField(primary_key=True)
    idclienteextranjero = models.OneToOneField(Clienteextranjero, on_delete=models.CASCADE, db_column='idclienteextranjero')
    producto1 = models.CharField(max_length=100)
    cantidad1 = models.IntegerField()
    embalaje1 = models.CharField(max_length=50)
    producto2 = models.CharField(max_length=100, blank=True, null=True)
    cantidad2 = models.IntegerField()
    embalaje2 = models.CharField(max_length=50, blank=True, null=True)
    producto3 = models.CharField(max_length=100, blank=True, null=True)
    cantidad3 = models.IntegerField()
    embalaje3 = models.CharField(max_length=50, blank=True, null=True)
    producto4 = models.CharField(max_length=100, blank=True, null=True)
    cantidad4 = models.IntegerField(blank=True, null=True)
    embalaje4 = models.CharField(max_length=50, blank=True, null=True)
    producto5 = models.CharField(max_length=100, blank=True, null=True)
    cantidad5 = models.IntegerField(blank=True, null=True)
    embalaje5 = models.CharField(max_length=50, blank=True, null=True)
    producto6 = models.CharField(max_length=100, blank=True, null=True)
    cantidad6 = models.IntegerField(blank=True, null=True)
    embalaje6 = models.CharField(max_length=50, blank=True, null=True)
    producto7 = models.CharField(max_length=100, blank=True, null=True)
    cantidad7 = models.IntegerField(blank=True, null=True)
    embalaje7 = models.CharField(max_length=50, blank=True, null=True)
    producto8 = models.CharField(max_length=100, blank=True, null=True)
    cantidad8 = models.IntegerField(blank=True, null=True)
    embalaje8 = models.CharField(max_length=50, blank=True, null=True)
    producto9 = models.CharField(max_length=100, blank=True, null=True)
    cantidad9 = models.IntegerField(blank=True, null=True)
    embalaje9 = models.CharField(max_length=50, blank=True, null=True)
    producto10 = models.CharField(max_length=100, blank=True, null=True)
    cantidad10 = models.IntegerField(blank=True, null=True)
    embalaje10 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidointernacional'

    def json_serializer_pedidointernacional(self):
      return{
            'idpedidointernacional':self.idpedidointernacional,
            'idclienteextranjero':self.idclienteextranjero,
            'producto1':self.producto1,
            'cantidad1':self.cantidad1,
            'embalaje1':self.embalaje1,
            'producto2':self.producto2,
            'cantidad2':self.cantidad2,
            'embalaje2':self.embalaje2,
            'producto3':self.producto3,
            'cantidad3':self.cantidad3,
            'embalaje3':self.embalaje3,
            'producto4':self.producto4,
            'cantidad4':self.cantidad4,
            'embalaje4':self.embalaje4,
            'producto5':self.producto5,
            'cantidad5':self.cantidad5,
            'embalaje5':self.embalaje5,
            'producto6':self.producto6,
            'cantidad6':self.cantidad6,
            'embalaje6':self.embalaje6,
            'producto7':self.producto7,
            'cantidad7':self.cantidad7,
            'embalaje7':self.embalaje7,
            'producto8':self.producto8,
            'cantidad8':self.cantidad8,
            'embalaje8':self.embalaje8,
            'producto9':self.producto9,
            'cantidad9':self.cantidad9,
            'embalaje9':self.embalaje9,
            'producto10':self.producto10,
            'cantidad10':self.cantidad10,
            'embalaje10':self.embalaje10,

    }

##listo
class Pedidonacional(models.Model):
    idpedidonacional = models.AutoField(primary_key=True)
    idclientenacional = models.OneToOneField(Clientenacional, on_delete=models.CASCADE, db_column='idclientenacional')
    producto1 = models.CharField(max_length=100)
    cantidad1 = models.IntegerField()
    embalaje1 = models.CharField(max_length=100)
    producto2 = models.CharField(max_length=100, blank=True, null=True)
    cantidad2 = models.IntegerField(blank=True, null=True)
    embalaje2 = models.CharField(max_length=100, blank=True, null=True)
    producto3 = models.CharField(max_length=100, blank=True, null=True)
    cantidad3 = models.IntegerField(blank=True, null=True)
    embalaje3 = models.CharField(max_length=100, blank=True, null=True)
    producto4 = models.CharField(max_length=100, blank=True, null=True)
    cantidad4 = models.IntegerField(blank=True, null=True)
    embalaje4 = models.CharField(max_length=100, blank=True, null=True)
    producto5 = models.CharField(max_length=100, blank=True, null=True)
    cantidad5 = models.IntegerField(blank=True, null=True)
    embalaje5 = models.CharField(max_length=100, blank=True, null=True)
    producto6 = models.CharField(max_length=100, blank=True, null=True)
    cantidad6 = models.IntegerField(blank=True, null=True)
    embalaje6 = models.CharField(max_length=100, blank=True, null=True)
    producto7 = models.CharField(max_length=100, blank=True, null=True)
    cantidad7 = models.IntegerField(blank=True, null=True)
    embalaje7 = models.CharField(max_length=100, blank=True, null=True)
    producto8 = models.CharField(max_length=100, blank=True, null=True)
    cantidad8 = models.IntegerField(blank=True, null=True)
    embalaje8 = models.CharField(max_length=100, blank=True, null=True)
    producto9 = models.CharField(max_length=100, blank=True, null=True)
    cantidad9 = models.IntegerField(blank=True, null=True)
    embalaje9 = models.CharField(max_length=100, blank=True, null=True)
    producto10 = models.CharField(max_length=100, blank=True, null=True)
    cantidad10 = models.IntegerField(blank=True, null=True)
    embalaje10 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidonacional'

    def json_serializer_pedidointernacional(self):
      return{
            'idpedidonacional':self.idpedidonacional,
            'idclientenacional':self.idclientenacional,
            'producto1':self.producto1,
            'cantidad1':self.cantidad1,
            'embalaje1':self.embalaje1,
            'producto2':self.producto2,
            'cantidad2':self.cantidad2,
            'embalaje2':self.embalaje2,
            'producto3':self.producto3,
            'cantidad3':self.cantidad3,
            'embalaje3':self.embalaje3,
            'producto4':self.producto4,
            'cantidad4':self.cantidad4,
            'embalaje4':self.embalaje4,
            'producto5':self.producto5,
            'cantidad5':self.cantidad5,
            'embalaje5':self.embalaje5,
            'producto6':self.producto6,
            'cantidad6':self.cantidad6,
            'embalaje6':self.embalaje6,
            'producto7':self.producto7,
            'cantidad7':self.cantidad7,
            'embalaje7':self.embalaje7,
            'producto8':self.producto8,
            'cantidad8':self.cantidad8,
            'embalaje8':self.embalaje8,
            'producto9':self.producto9,
            'cantidad9':self.cantidad9,
            'embalaje9':self.embalaje9,
            'producto10':self.producto10,
            'cantidad10':self.cantidad10,
            'embalaje10':self.embalaje10,
    }

##listo
class Postulacioninternacional(models.Model):
    idpostulacioninternacional = models.AutoField(primary_key=True)
    idproductor = models.ForeignKey('Productor',on_delete=models.CASCADE, db_column='idproductor')
    idsubastapedidointernacional = models.OneToOneField('Subastapedidointernacional', on_delete=models.CASCADE, db_column='idsubastapedidointernacional')
    fruta1 = models.CharField(max_length=50)
    cantidad1 = models.IntegerField()
    embalaje1 = models.CharField(max_length=50)
    precio1 = models.IntegerField()
    fruta2 = models.CharField(max_length=50, blank=True, null=True)
    cantidad2 = models.IntegerField(blank=True, null=True)
    embalaje2 = models.CharField(max_length=50, blank=True, null=True)
    precio2 = models.IntegerField(blank=True, null=True)
    fruta3 = models.CharField(max_length=50, blank=True, null=True)
    cantidad3 = models.IntegerField(blank=True, null=True)
    embalaje3 = models.CharField(max_length=50, blank=True, null=True)
    precio3 = models.IntegerField(blank=True, null=True)
    fruta4 = models.CharField(max_length=50, blank=True, null=True)
    cantidad4 = models.IntegerField(blank=True, null=True)
    embalaje4 = models.CharField(max_length=50, blank=True, null=True)
    precio4 = models.IntegerField(blank=True, null=True)
    fruta5 = models.CharField(max_length=50, blank=True, null=True)
    cantidad5 = models.IntegerField(blank=True, null=True)
    embalaje5 = models.CharField(max_length=50, blank=True, null=True)
    precio5 = models.IntegerField(blank=True, null=True)
    fruta6 = models.CharField(max_length=50, blank=True, null=True)
    cantidad6 = models.IntegerField(blank=True, null=True)
    embalaje6 = models.CharField(max_length=50, blank=True, null=True)
    precio6 = models.IntegerField(blank=True, null=True)
    fruta7 = models.CharField(max_length=50, blank=True, null=True)
    cantidad7 = models.IntegerField(blank=True, null=True)
    embalaje7 = models.CharField(max_length=50, blank=True, null=True)
    precio7 = models.IntegerField(blank=True, null=True)
    fruta8 = models.CharField(max_length=50, blank=True, null=True)
    cantidad8 = models.IntegerField(blank=True, null=True)
    embalaje8 = models.CharField(max_length=50, blank=True, null=True)
    precio8 = models.IntegerField(blank=True, null=True)
    fruta9 = models.CharField(max_length=50, blank=True, null=True)
    cantidad9 = models.IntegerField(blank=True, null=True)
    embalaje9 = models.CharField(max_length=50, blank=True, null=True)
    precio9 = models.IntegerField(blank=True, null=True)
    fruta10 = models.CharField(max_length=50, blank=True, null=True)
    cantidad10 = models.IntegerField(blank=True, null=True)
    embalaje10 = models.CharField(max_length=50, blank=True, null=True)
    precio10 = models.IntegerField(blank=True, null=True)
    ganadora = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'postulacioninternacional'
    
    def json_serializer_postulacioninternacional(self):
     return{
            'idpostulacioninternacional':self.idpostulacioninternacional,
            'idproductor':self.idproductor,
            'idsubastapedidointernacional':self.idsubastapedidointernacional,
            'fruta1': self.fruta1,
            'cantidad1':self.cantidad1,
            'precio1':self.precio1,
            'fruta2': self.fruta2,
            'cantidad2':self.cantidad2,
            'precio2':self.precio2, 
            'fruta3': self.fruta3,
            'cantidad3':self.cantidad3,
            'precio3':self.precio3, 
            'fruta4': self.fruta4,
            'cantidad4':self.cantidad4,
            'precio4':self.precio4, 
            'fruta5': self.fruta5,
            'cantidad5':self.cantidad5,
            'precio5':self.precio5, 
            'fruta6': self.fruta6,
            'cantidad6':self.cantidad6,
            'precio6':self.precio6, 
            'fruta7': self.fruta7,
            'cantidad7':self.cantidad7,
            'precio7':self.precio7, 
            'fruta8': self.fruta8,
            'cantidad8':self.cantidad8,
            'precio8':self.precio8, 
            'fruta9': self.fruta9,
            'cantidad9':self.cantidad9,
            'precio9':self.precio9, 
            'fruta10': self.fruta10,
            'cantidad10':self.cantidad10,
            'precio10':self.precio10,
            'ganador':self.ganadora  
     }

##listo
class Postulacionnacional(models.Model):
    idpostulacionnacional = models.AutoField(primary_key=True)
    idproductor = models.ForeignKey('Productor', on_delete=models.CASCADE, db_column='idproductor')
    idsubastapedidonacional = models.ForeignKey('Subastapedidonacional', on_delete=models.CASCADE, db_column='idsubastapedidonacional')
    fruta1 = models.CharField(max_length=50)
    cantidad1 = models.IntegerField()
    embalaje1 = models.CharField(max_length=50)
    precio1 = models.IntegerField()
    fruta2 = models.CharField(max_length=50, blank=True, null=True)
    cantidad2 = models.IntegerField(blank=True, null=True)
    embalaje2 = models.CharField(max_length=50, blank=True, null=True)
    precio2 = models.IntegerField(blank=True, null=True)
    fruta3 = models.CharField(max_length=50, blank=True, null=True)
    cantidad3 = models.IntegerField(blank=True, null=True)
    embalaje3 = models.CharField(max_length=50, blank=True, null=True)
    precio3 = models.IntegerField(blank=True, null=True)
    fruta4 = models.CharField(max_length=50, blank=True, null=True)
    cantidad4 = models.IntegerField(blank=True, null=True)
    embalaje4 = models.CharField(max_length=50, blank=True, null=True)
    precio4 = models.IntegerField(blank=True, null=True)
    fruta5 = models.CharField(max_length=50, blank=True, null=True)
    cantidad5 = models.IntegerField(blank=True, null=True)
    embalaje5 = models.CharField(max_length=50, blank=True, null=True)
    precio5 = models.IntegerField(blank=True, null=True)
    fruta6 = models.CharField(max_length=50, blank=True, null=True)
    cantidad6 = models.IntegerField(blank=True, null=True)
    embalaje6 = models.CharField(max_length=50, blank=True, null=True)
    precio6 = models.IntegerField(blank=True, null=True)
    fruta7 = models.CharField(max_length=50, blank=True, null=True)
    cantidad7 = models.IntegerField(blank=True, null=True)
    embalaje7 = models.CharField(max_length=50, blank=True, null=True)
    precio7 = models.IntegerField(blank=True, null=True)
    fruta8 = models.CharField(max_length=50, blank=True, null=True)
    cantidad8 = models.IntegerField(blank=True, null=True)
    embalaje8 = models.CharField(max_length=50, blank=True, null=True)
    precio8 = models.IntegerField(blank=True, null=True)
    fruta9 = models.CharField(max_length=50, blank=True, null=True)
    cantidad9 = models.IntegerField(blank=True, null=True)
    embalaje9 = models.CharField(max_length=50, blank=True, null=True)
    precio9 = models.IntegerField(blank=True, null=True)
    fruta10 = models.CharField(max_length=50, blank=True, null=True)
    cantidad10 = models.IntegerField(blank=True, null=True)
    embalaje10 = models.CharField(max_length=50, blank=True, null=True)
    precio10 = models.IntegerField(blank=True, null=True)
    ganadora = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'postulacionnacional'

    def json_serializer_postulacioninternacional(self):
     return{
            'idpostulacionnacional':self.idpostulacionnacional,
            'idproductor':self.idproductor,
            'idsubastapedidonacional':self.idsubastapedidonacional,
            'fruta1': self.fruta1,
            'cantidad1':self.cantidad1,
            'precio1':self.precio1,
            'fruta2': self.fruta2,
            'cantidad2':self.cantidad2,
            'precio2':self.precio2, 
            'fruta3': self.fruta3,
            'cantidad3':self.cantidad3,
            'precio3':self.precio3, 
            'fruta4': self.fruta4,
            'cantidad4':self.cantidad4,
            'precio4':self.precio4, 
            'fruta5': self.fruta5,
            'cantidad5':self.cantidad5,
            'precio5':self.precio5, 
            'fruta6': self.fruta6,
            'cantidad6':self.cantidad6,
            'precio6':self.precio6, 
            'fruta7': self.fruta7,
            'cantidad7':self.cantidad7,
            'precio7':self.precio7, 
            'fruta8': self.fruta8,
            'cantidad8':self.cantidad8,
            'precio8':self.precio8, 
            'fruta9': self.fruta9,
            'cantidad9':self.cantidad9,
            'precio9':self.precio9, 
            'fruta10': self.fruta10,
            'cantidad10':self.cantidad10,
            'precio10':self.precio10,
            'ganador':self.ganadora  
      } 

##listo
class Postulaciontransinternacional(models.Model):
    idpostulacion = models.AutoField(primary_key=True)
    idtransportista = models.ForeignKey('Transportista', on_delete=models.CASCADE, db_column='idtransportista')
    idsubastatransinternacional = models.ForeignKey('Subastatransinternacional', on_delete=models.CASCADE, db_column='idsubastatransinternacional')
    tipovehiculo1 = models.CharField(max_length=100)
    patente1 = models.CharField(max_length=100)
    cadenadefrio1 = models.CharField(max_length=100, blank=True, null=True)
    tipovehiculo2 = models.CharField(max_length=100, blank=True, null=True)
    patente2 = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio2 = models.CharField(max_length=100, blank=True, null=True)
    tipovehiculo3 = models.CharField(max_length=100, blank=True, null=True)
    patente3 = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio3 = models.CharField(max_length=100, blank=True, null=True)
    tipovehiculo4 = models.CharField(max_length=100, blank=True, null=True)
    patente4 = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio4 = models.CharField(max_length=100, blank=True, null=True)
    tipovehiculo5 = models.CharField(max_length=100, blank=True, null=True)
    patente5 = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio5 = models.CharField(max_length=100, blank=True, null=True)
    ganadora = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'postulaciontransinternacional'
    
    def json_seriaizer_postulaciontransinternacional(self):
        return{
               'idpostulacion':self.idpostulacion,
               'idtransportista':self.idtransportista,
               'idsubastatransinternacional':self.idsubastatransinternacional,
               'tipovehiculo1':self.tipovehiculo1,
               'patente1':self.patente1,
               'cadenadefrio1':self.cadenadefrio1,
               'tipovehiculo2':self.tipovehiculo2,
               'patente2':self.patente2,
               'cadenadefrio2':self.cadenadefrio2,
               'tipovehiculo3':self.tipovehiculo3,
               'patente3':self.patente3,
               'cadenadefrio3':self.cadenadefrio3,
               'tipovehiculo4':self.tipovehiculo4,
               'patente4':self.patente4,
               'cadenadefrio4':self.cadenadefrio4,
               'tipovehiculo5':self.tipovehiculo5,
               'patente5':self.patente5,
               'cadenadefrio5':self.cadenadefrio5,
               'ganadora':self.ganadora
        }

##listo   
class Postulaciontransnacional(models.Model):
    idpostulacionnacional = models.AutoField(primary_key=True)
    idtransportista = models.ForeignKey('Transportista', on_delete=models.CASCADE, db_column='idtransportista')
    idsubastatransportenacional = models.ForeignKey('Subastatransportenacional', on_delete=models.CASCADE, db_column='idsubastatransportenacional')
    tipovehiculo1 = models.CharField(max_length=100)
    patente1 = models.CharField(max_length=100)
    cadenadefrio1 = models.CharField(max_length=100, blank=True, null=True)
    tipovehiculo2 = models.CharField(max_length=100, blank=True, null=True)
    patente2 = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio2 = models.CharField(max_length=100, blank=True, null=True)
    tipovehiculo3 = models.CharField(max_length=100, blank=True, null=True)
    patente3 = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio3 = models.CharField(max_length=100, blank=True, null=True)
    tipovehiculo4 = models.CharField(max_length=100, blank=True, null=True)
    patente4 = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio4 = models.CharField(max_length=100, blank=True, null=True)
    tipovehiculo5 = models.CharField(max_length=100, blank=True, null=True)
    patente5 = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio5 = models.CharField(max_length=100, blank=True, null=True)
    ganadora = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'postulaciontransnacional'
    
    def json_seriaizer_Postulaciontransnacional(self):
        return{
               'idpostulacionnacional':self.idpostulacionnacional,
               'idtransportista':self.idtransportista,
               'idsubastatransinternacional':self.idsubastatransportenacional,
               'tipovehiculo1':self.tipovehiculo1,
               'patente1':self.patente1,
               'cadenadefrio1':self.cadenadefrio1,
               'tipovehiculo2':self.tipovehiculo2,
               'patente2':self.patente2,
               'cadenadefrio2':self.cadenadefrio2,
               'tipovehiculo3':self.tipovehiculo3,
               'patente3':self.patente3,
               'cadenadefrio3':self.cadenadefrio3,
               'tipovehiculo4':self.tipovehiculo4,
               'patente4':self.patente4,
               'cadenadefrio4':self.cadenadefrio4,
               'tipovehiculo5':self.tipovehiculo5,
               'patente5':self.patente5,
               'cadenadefrio5':self.cadenadefrio5,
               'ganadora':self.ganadora
        }

##listo
class Productor(models.Model):
    idproductor = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    username = models.CharField(max_length=50)
    userpass = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'productor'
    
    def json_serializer(self):
     return {
             'idproductor': self.idproductor,
             'rut': self.rut,
             'nombre': self.nombre,
             'alias': self.alias,
             'direccion':self.direccion,
             'telefono':self.telefono,
             'username': self.username,
             'userpass': self.userpass,
            }

##listo
class Productos(models.Model):
    idproductos = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    calidad = models.CharField(max_length=20)
    precio = models.IntegerField()
    estado = models.CharField(max_length=50)
    embalaje = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    idproductor = models.ForeignKey(Productor, on_delete=models.CASCADE, db_column='idproductor')

    class Meta:
        managed = False
        db_table = 'productos'

    def json_serializer_productos(self):
     return{
         'idproductos':self.idproductos,
         'descripcion':self.descripcion,
         'calidad':self.calidad,
         'precio':self.precio,
         'estado':self.estado,
         'embalaje':self.embalaje,
         'cantidad':self.cantidad,
         'idproductor':self.idproductor
     }

##listo
class Subastapedidointernacional(models.Model):
    idsubastapedidointernacional = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechatermino = models.DateField(blank=True, null=True)
    fechaentregadeproductos = models.DateField(blank=True, null=True)
    idadministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, db_column='idadministrador')
    idpedidointernacional = models.OneToOneField(Pedidointernacional, on_delete=models.CASCADE, db_column='idpedidointernacional')

    class Meta:
        managed = False
        db_table = 'subastapedidointernacional'
    
    def json_serializer_subastapedidoInternacional(self):
     return{
            'idsubastapedidointernacional':self.idsubastapedidointernacional,
            'fechainicio':self.fechainicio,
            'fechatermino':self.fechatermino,
            'fechaentregadeproductos':self.fechaentregadeproductos,
            'idadministrador':self.idadministrador,
            'idpedidointernacional':self.idpedidointernacional
     }

##listo
class Subastapedidonacional(models.Model):
    idsubastapedidonacional = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechatermino = models.DateField(blank=True, null=True)
    fechaentregadeproductos = models.DateField(blank=True, null=True)
    idadministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, db_column='idadministrador')
    idpedidonacional = models.OneToOneField(Pedidonacional, on_delete=models.CASCADE, db_column='idpedidonacional')

    class Meta:
        managed = False
        db_table = 'subastapedidonacional'
    
    def json_serializer_subastapedidonacional(self):
     return{
            'idsubastapedidonacional':self.idsubastapedidonacional,
            'fechainicio':self.fechainicio,
            'fechatermino':self.fechatermino,
            'fechaentregadeproductos':self.fechaentregadeproductos,
            'idadministrador':self.idadministrador,
            'idpedidonacional':self.idpedidonacional
     }

##listo
class Subastatransinternacional(models.Model):
    idsubastatransinternacional = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    fecharealizacion = models.DateField()
    direccionorigen = models.CharField(max_length=100)
    idcontratoventaextranjero = models.ForeignKey(Contratoventaextranjero,on_delete=models.CASCADE, db_column='idcontratoventaextranjero')
    direccionentrega = models.CharField(max_length=100)
    idadministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, db_column='idadministrador')

    class Meta:
        managed = False
        db_table = 'subastatransinternacional'
    
    def json_serializer_subastatransinternacional(self):
     return{
            'idsubastatransinternacional':self.idsubastatransinternacional,
            'fechainicio':self.fechainicio,
            'fechatermino':self.fechatermino,
            'fecharealizacion':self.fecharealizacion,
            'direccionorigen':self.direccionorigen,
            'idcontratoventaextranjero':self.idcontratoventaextranjero,
            'direccionentrega':self.direccionentrega,
            'idadministrador':self.idadministrador,
     }

##listo 
class Subastatransportenacional(models.Model):
    idsubastatransportenacional = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    fecharealizacion = models.DateField()
    direccionorigen = models.CharField(max_length=100)
    direccionentrega = models.CharField(max_length=100)
    idadministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, db_column='idadministrador')
    idpedidonacional = models.OneToOneField(Pedidonacional, on_delete=models.CASCADE, db_column='idpedidonacional')

    class Meta:
        managed = False
        db_table = 'subastatransportenacional'

    def json_serializer_subastatransportenacional(self):
     return{
            'idsubastatransportenacional':self.idsubastatransportenacional,
            'fechainicio':self.fechainicio,
            'fechatermino':self.fechatermino,
            'fecharealizacion':self.fecharealizacion,
            'direccionorigen':self.direccionorigen,
            'direccionentrega':self.direccionentrega,
            'idadministrador':self.idadministrador,
            'idpedidonacional':self.idpedidonacional
     }

##Listo
class Transportista(models.Model):
    idtransportista = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    userpass = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'transportista'

    def json_serializer_transportista(self):
        return{
                'idtransportista':self.idtransportista,
                'rut':self.rut,
                'nombre':self.nombre,
                'direccion':self.direccion,
                'username':self.username,
                'userpass':self.userpass
        }

##Listo
class Vehiculo(models.Model):
    idvehiculo = models.AutoField(primary_key=True)
    tipovehiculo = models.CharField(max_length=100)
    patente = models.CharField(max_length=100)
    cargamaxima = models.IntegerField(blank=True, null=True)
    tipodecarga = models.CharField(max_length=100, blank=True, null=True)
    cadenadefrio = models.IntegerField()
    idtransportista = models.ForeignKey(Transportista, on_delete=models.CASCADE, db_column='idtransportista')

    class Meta:
        managed = False
        db_table = 'vehiculo'
    
    def json_serializer_vehiculo(self):
     return{
            'idvehiculo':self.idvehiculo,
            'tipovehiculo':self.tipovehiculo,
            'patente':self.patente,
            'cargamaxima':self.cargamaxima,
            'tipodecarga':self.tipodecarga,
            'cadenadefrio':self.cadenadefrio,
            'idtransportista':self.idtransportista
     }   
