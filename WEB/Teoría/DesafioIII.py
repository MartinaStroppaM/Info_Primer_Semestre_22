import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prendas/1")
print(pedido.headers)

# Cambió el Content-Length

print(pedido.status_code)