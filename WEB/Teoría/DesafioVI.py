import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=remera")
print(pedido.json())