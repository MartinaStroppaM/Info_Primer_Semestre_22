# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (**|**).

import re

def reemplazar(string):
    return re.sub("[\s_:]", "|", string)

print(reemplazar("hola: __¿Como estas?"))