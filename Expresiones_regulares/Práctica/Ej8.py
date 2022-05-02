# Escribí un programa que separe y devuelva los caracteres númericos de un string.

import re

def separador_de_numeros(string):
    return re.findall("\d", string)

print(separador_de_numeros("2022"))
print(separador_de_numeros("H0la"))