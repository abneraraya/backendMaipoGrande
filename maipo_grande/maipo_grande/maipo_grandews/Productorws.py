import requests
import json

def eliminar(id):
    try:
        url='http://127.0.0.1:9000/api/v1/contacto' 
        response= requests.delete(url, data={'id':id})
        codigo=response.json()['codigo']

        print('RESPONSE:{0}'.format(response.json()))

        if codigo==1:
            return  True
        else:
            return False
    except Exception as e:
        print(e) 
        print('ERROR: problemas con el servicio.')
        return False

def buscarTodo():
    try:
        url='http://127.0.0.1:9000/api/v1/contacto'

        response=requests.get(url)

        codigo=response.json()['codigo']

        print('RESPONSE:{0}'.format(response.json()))

        if codigo==1:
            return  response.json()['datos']
        else:
            return []
    except Exception as e:
        print(e)
        print('ERROR: problemas con el servicio.')
        return []