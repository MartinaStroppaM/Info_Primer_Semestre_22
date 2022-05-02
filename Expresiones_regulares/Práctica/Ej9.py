# Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"

import re

def entre_guiones(string):
    return re.findall("-(.*?)-", string)

print(entre_guiones("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))