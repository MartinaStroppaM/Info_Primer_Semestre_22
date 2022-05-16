import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
"""
Hacer un get: en términos de http o protocolo. Lo hago a una url que almacena recursos. 
Le pido que me traiga todos los recursos que tenga esa aplicación.
Filtra la tabla y me trae un elemento en particular.
Request: me devuelve el código
"""
print(pedido)
print(pedido.json())
"""
Json: es como un diccionario de python. 
Tipo de formato en el cual el servidor me devuelve las cosas.
"""
print(len(pedido.json()))
print(pedido.headers)
"""
Headers: (atributo) me dice toda la metadata, la info relativa del pedido.
"""
print(pedido.status_code)
"""
Status code: habla de como fue la conexión, el estado de ese pedido.
"""



