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
-Instalas djangorestFramework, lo agregas a la aplicaciones utilizadas en el setting
-Creas los Serializadores (serializer.py)
-Creas las view (view.py)
-Creas un router con las url(url.py)