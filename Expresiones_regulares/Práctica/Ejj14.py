# Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

import re

def replace(string):
    return re.sub("\s", ";", string)

print(replace("     Hola, me llamo Martina"))