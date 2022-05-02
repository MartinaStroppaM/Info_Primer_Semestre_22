# Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

import re

def caracter_permitido(string):
     return bool(re.search("[\w]", string))

print(caracter_permitido("H0laa"))
print(caracter_permitido("--¿?--"))

def caracter_permitido2(string):
    if re.search("[\w]", string) is not None:
        return True
    else:
        return False

print(caracter_permitido2("H0laa"))
print(caracter_permitido2("--¿?--"))