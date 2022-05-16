import re
import requests

pedido1 = requests.get("https://macowins-server.herokuapp.com/ventas")
pedido2 = requests.get("https://macowins-server.herokuapp.com/ventas/2")

print("Headers pepido1: ", pedido1.headers)
print("Headers pepido2: ", pedido2.headers)

print("Content pedido1: ", pedido1.content)
print("Content pedido2: ", pedido2.content)
