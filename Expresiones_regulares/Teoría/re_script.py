import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"

re.match(patron, texto)
print(re.search(patron, texto))
print(texto[22:26])
print(re.search(patron, texto).group(0))
print(re.findall(patron, texto))

print(re.match(patron, texto)) 
#Busca la primera palabra; tendría que ser "Lorem"

