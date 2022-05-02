# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9

import re

def todos_caracteres_permitidos(string):
    return re.search("[^\w*]", string) is None

print(todos_caracteres_permitidos("H0laa"))
print(todos_caracteres_permitidos("--¿Hola?--"))
print(todos_caracteres_permitidos("--¿?--"))