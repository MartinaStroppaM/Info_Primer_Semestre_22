#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada

import re

def string_en_frase(lista_strings, frase_dada):
    for string in lista_strings:
        if re.search(string, frase_dada) is not None:
            return True
        else:
            return False

print(string_en_frase(["Había", "una-vez-truz", "del-fin"], "Había una-vez-truz y un del-fin"))
print(string_en_frase(["Hola", "estás"], "Hola, cómo estás?"))
print(string_en_frase(["Hola", "Martina"], "¿Qué tal"))