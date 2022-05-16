import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prindas/1")
print(pedido.headers)
print(pedido.status_code)

#El status es 404: Error