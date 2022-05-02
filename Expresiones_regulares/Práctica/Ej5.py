# Escribí un programa que diga si un string empieza con un número específico.

import re

def numero_especifico(string, numero):
    return bool(re.match(str([numero]), string))

print(numero_especifico("2022", 2))
print(numero_especifico("1922", 2))