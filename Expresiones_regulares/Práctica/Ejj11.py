# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. 
# Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]
import re 

def leer_lista(lista):
    nueva_lista = []
    for i in lista:
        if re.findall("(P\S*)\s(P\S*)\w", i):
         nueva_lista.append(i)
    return nueva_lista

print(leer_lista(["Práctica Python", "Práctica C++", "Práctica Fortran"]))
