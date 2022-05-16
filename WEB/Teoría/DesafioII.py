import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prendas/400")
print(pedido.json())
