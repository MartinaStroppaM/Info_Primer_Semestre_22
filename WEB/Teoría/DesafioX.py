import requests

pedido = requests.get('https://macowins-server.herokuapp.com/home')
print(pedido.headers)

"""
El Content-Type de /home es text/html a diferencia de las anteriores
que era application/json.
De igual manera me tira un error de cliente, cuando imprimo el pedido
me retorna Response [404]
"""
