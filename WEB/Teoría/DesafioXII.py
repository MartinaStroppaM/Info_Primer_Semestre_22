import requests

data = {'id': 21}
# pedido = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
# print(pedido) o.

pedido2 = requests.get('https://macowins-server.herokuapp.com/prendas/')

# pedido3 = requests.delete('https://macowins-server.herokuapp.com/prendas/21')
# print(pedido3)
# print(pedido2.json())

get_ids = requests.get("https://macowins-server.herokuapp.com/prendas/")
ids = get_ids.json()

lista = []
for i in range(len(ids)):
     lista.append(ids[i]["id"])

print(lista)

# print(pedido2.json()[-4:]["id"])
ids_no_valid = lista[-4:]
print(ids_no_valid)


data = ids_no_valid
lista2 = []
for i in ids_no_valid:
    delete = requests.delete("https://macowins-server.herokuapp.com/prendas/" + str(i))
    lista2.append(delete.json())
print(lista2)

print(pedido2.json())