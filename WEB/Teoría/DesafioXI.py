import requests

wpp = requests.get("https://web.whatsapp.com/")
print(wpp)
print(wpp.headers)
#'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT'

pinterest = requests.get("https://ar.pinterest.com/")
print(pinterest)
print(pinterest.headers)

github = requests.get("https://github.com/AJVelezRueda/Fundamentos_de_informatica/tree/master/Python_intro")
print(github)
print(github.headers)

instagram = requests.get("https://www.instagram.com/?hl=en")
print(instagram)
print(instagram.headers)