import requests, json

pedido = requests.get('https://macowins-server.herokuapp.com/ventas')
print(pedido)

# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# data =  { "tipo": "pantalon", "talle": "XS" }
# pedido = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)
# print(pedido.status_code)
# print(requests.get('https://macowins-server.herokuapp.com/prendas').json())

lista = []
for i in range(len(pedido.json())):
     lista.append(pedido.json()[i]["id"])

print(lista)

print(len(pedido.json()))

data = {"producto": {"id": 3, "tipo": "pantalon", "talle": "50" }}
nueva_venta = requests.post('https://macowins-server.herokuapp.com/ventas/504', data=data)
print(pedido.json())