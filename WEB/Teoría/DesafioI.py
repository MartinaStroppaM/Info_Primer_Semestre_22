import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
print(pedido.json())
