# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P")

def empieza_con(letra, archivo):
    with open(archivo, "r") as miarch:
        contar = 0
        for linea in miarch:
            if linea.startswith(letra.upper()) or linea.startswith(letra.lower()):
                pass
            else:
                contar += 1
        return("El número de lineas que no empiezan con " + letra + " es " + str(contar))

print(empieza_con("P", r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"))