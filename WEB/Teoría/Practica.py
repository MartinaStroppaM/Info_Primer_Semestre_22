import requests

pedido = requests.get('https://macowins-server.herokuapp.com/prendas/')
print(pedido) #Decuelve Response [200]
# # print(pedido.json())
# # print(pedido.headers)
# # print(pedido.status_code)
print(pedido.content)

# wpp = requests.get("https://web.whatsapp.com/")
# print(wpp)
# print(wpp.headers)
# #'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT'

# pinterest = requests.get("https://ar.pinterest.com/")
# print(pinterest)
# print(pinterest.headers)

# github = requests.get("https://github.com/AJVelezRueda/Fundamentos_de_informatica/tree/master/Python_intro")
# print(github)
# print(github.headers)

# instagram = requests.get("https://www.instagram.com/?hl=en")
# print(instagram)
# print(instagram.headers)

data = {'id': 21}
pedido = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)

print(pedido)

data =  { "tipo": "chomba", "talle": "XS" }
pedido = requests.post('https://macowins-server.herokuapp.com/prendas', data=data)

print(pedido)
print(pedido.content)

import json, requests
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data =  { "tipo": "chomba", "talle": "XS" }
pedido = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)
print(pedido.status_code)

print(requests.get('https://macowins-server.herokuapp.com/prendas').json())