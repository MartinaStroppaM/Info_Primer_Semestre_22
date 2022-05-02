# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

import re

def tiene_todo(texto):
     return re.search("[\w\s]", texto)


print(tiene_todo("hola, Co??M o 112 -- estas"))

