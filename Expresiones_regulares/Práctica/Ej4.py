# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios)

import re

def palabras_unidas(strings):
    return re.search("\w*(_)\w*", strings)

print(palabras_unidas("Informatica_1erSemestre"))