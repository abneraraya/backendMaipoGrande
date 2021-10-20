## COMANDOS PARA INSTALAR LIBRERIA DJANGO
python.exe -m pip install Django

## CREACIÓN DE PROYECTO WEB
django-admin startproject bazar_web

## DESPLEGAR APLICACIÓN WEB
python.exe .\manage.py runserver

## DESPLEGAR CON IP DE RED LOCAL
python.exe .\manage.py runserver  192.168.43.216:8000

## INSTALAR LIBRERIA PARA CONEXIÓN CON MYSQL
python.exe -m pip install mysqlclient

## INSPECCIÓN DB + CREACIÓN MODELS
python.exe .\manage.py inspectdb

## Como crear una api
-Instalas djangorestFramework, lo agregas a la aplicaciones utilizadas en el setting.

-Creas los Serializadores (serializer.py).

-Creas las view (view.py).

-Creas un router con las url(url.py).

## url de api ya creadas 

En la siguiente lista aparecen las url de las api creadas hasta el momento, la lista desplegada a continuacion  se diviran en dos grupos.

El primer grupo de ellos son entidades base es decir que no necesitan que existan creadas otras entidades con anticipacion para poder crear nuevos registros en si mismas 

--------------Entidades base---------------------------------

.- http://127.0.0.1:8000/api/productor/ : Esta url pertenece a la entidad productores, en esta se pueden
hacer las acciones basicas de un crud que son la creacion, la lectura , la actualizacion y el eliminado de los mismos, es decir que soporta metodos post,get,put y delete, todo mediante protocolos http.
   
.- http://127.0.0.1:8000/api/administrador : Esta url pertenece a la entidad administrador, en esta se pueden
hacer las acciones basicas de un crud que son la creacion, la lectura , la actualizacion y el eliminado de los mismos, es decir que soporta metodos post,get,put y delete, todo mediante protocolos http.
   
.- http://127.0.0.1:8000/api/clienteextranjero : Esta url pertenece a la entidad cliente extranjero, en esta se pueden hacer las acciones basicas de un crud que son la creacion, la lectura , la actualizacion y el eliminado de los mismos, es decir que soporta metodos post,get,put y delete, todo mediante protocolos http.
   
.- http://127.0.0.1:8000/api/clientenacional : Esta url pertenece a la entidad cliente nacional, en esta se pueden hacer las acciones basicas de un crud que son la creacion, la lectura , la actualizacion y el eliminado de los mismos, es decir que soporta metodos post,get,put y delete, todo mediante protocolos http

.-http://127.0.0.1:8000/api/transportista : Esta url pertenece a la entidad transportista, en esta se pueden hacer las acciones basicas de un crud que son la creacion, la lectura , la actualizacion y el eliminado de los mismos, es decir que soporta metodos post,get,put y delete, todo mediante protocolos http.

----------------------- Fin de entidades base ------------------------------


----------------------- Entidades secundarias ------------------------------

Las siguientes url descrita a continuacion  pertenecen a entidades secundarias, es decir para poder insertar datos (es decir hacer post ) es necesario que existan entidades previamente llenadas  como por ejemplo en la entidad pedido nacional 

Pedido nacional necesita que sea hecho por un cliente nacional  es decir que  primero deben haber creado un cliente nacional para que este pueda hacer el pedido perse

http://127.0.0.1:8000/api/vehiculo : Esta url pertenece a la entidad vehiculo, en esta se pueden hacer las acciones basicas de un crud que son la creacion, la lectura , la actualizacion y el eliminado de los mismos, es decir que soporta metodos post,get,put y delete, todo mediante protocolos http.

Para poder crear algun registro dentro de esta entidad Primeramente debe existir algun registro en la entidad transportista ya que  todo vehiculo esta asociado a un transportistasin embargo si no existen transportistas registrados no se podra registrar ningun tipo de vehiculo ya que no existira con quien asociar  el vehiculo en si.

.- http://127.0.0.1:8000/api/pedidonacional

.- http://127.0.0.1:8000/api/productos

.- http://127.0.0.1:8000/api/contratoventaextranjero

.- http://127.0.0.1:8000/api/pedidointernacional

.- http://127.0.0.1:8000/api/contratoproductor

----------------------- Entidades secundarias ------------------------------

.- http://127.0.0.1:8000/api/concretacionventa

.- http://127.0.0.1:8000/api/subastatransportenacional/


"subastapedidonacional": "http://127.0.0.1:8000/api/subastapedidonacional/",

"subastatransporteinternacional": "http://127.0.0.1:8000/api/subastatransporteinternacional/"

"postulacioninternacional": "http://127.0.0.1:8000/api/postulacioninternacional/",

"postulacionnacional": "http://127.0.0.1:8000/api/postulacionnacional/"

"subastapedidointernacional": "http://127.0.0.1:8000/api/subastapedidointernacional/",

"postulaciontransportenacional": "http://127.0.0.1:8000/api/postulaciontransportenacional/",

"postulaciontransporteinternacional": "http://127.0.0.1:8000/api/postulaciontransporteinternacional/",

"informedeventaglobal": "http://127.0.0.1:8000/api/informedeventaglobal/",

"informeventapersonal": "http://127.0.0.1:8000/api/informeventapersonal/"