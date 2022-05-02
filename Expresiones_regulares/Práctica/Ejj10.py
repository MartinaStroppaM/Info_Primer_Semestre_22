# Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres _@_ o _&_.

import re

def substrings(string):
    lista = re.findall("[@|&](.*?)[@|&]", string)
    return lista, re.search("[@|&](.*?)[@|&]", string)

print(substrings("@hola@ @como estas& @como"))

#No se como hacer para que el search me devuelva la posición sin los delimitadores y además todas las posiciones no solo la primera aparición.
