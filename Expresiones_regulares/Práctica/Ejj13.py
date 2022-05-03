# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

import re

def replace_primeros(string):
    return re.sub("\W", "_", string, 2)

print(replace_primeros("¡¡2022!!"))

"/w*/W/w*/W/."
#Busca el primer caracter alfanumerico 0 o mas veces hasta encontar un noalfanumerico. Después le puede seguir un alfa 1 o más hasta encontrar un noalf