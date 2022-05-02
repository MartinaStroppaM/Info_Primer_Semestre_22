# Creá un programa que verifique las siguientes condiciones:
    
# * si un string dado tiene una h seguida de ninguna o más e.

# * si un string dado tiene una h seguida de una o más e.

# * si un string dado tiene una h seguida de dos o tres e.

import re 

def encontrar_patron(string):
    return bool(re.search("he*", string))

print(encontrar_patron("helado"))
print(encontrar_patron("higo"))

def encontrar_patron1(string):
    return bool(re.search("he+", string))

print(encontrar_patron1("helado"))
print(encontrar_patron1("higo"))

def encontrar_patron2(string):
    return bool(re.search("he{2,3}", string))

print(encontrar_patron2("heelado"))
print(encontrar_patron2("heeelado"))
print(encontrar_patron2("hhelado"))
print(encontrar_patron2("helado"))
