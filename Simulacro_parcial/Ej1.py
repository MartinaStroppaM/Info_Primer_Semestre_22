# Escribir funciones que, dado un String, permitan obtener

# Cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios.
# La lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. 
# P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

import re

def cuantas_veces(string):
    return len(re.findall("bc9", string))

print(cuantas_veces("xsabc9cabcb3sabc9"))
print(cuantas_veces("hola amigos mios"))

def sin_c(string):
    return re.findall("aa([^c]*?)gg", string)

print(sin_c("ttaatatggttaacatgg"))