import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prendas?talle=XS")
print(pedido.json())