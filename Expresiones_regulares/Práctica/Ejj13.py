# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

import re

def replace_primeros(string):
    return re.sub("\W{2}", "__", string)

print(replace_primeros("¡¡2022!!"))