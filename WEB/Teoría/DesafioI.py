import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
print(pedido.json())


#URL ES UNA URI, UN PATH, QUE NOS PERMITE LOCALIZAR UN RECURSO A TRAVES DE INTERNET EN OTRA MÁQUINA REMOTA.