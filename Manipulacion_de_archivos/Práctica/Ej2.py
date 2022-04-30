# Escribí un programa que lea un archivo e imprima las primeras n líneas.

def primeras_lineas(numero, archivo):
    with open(archivo, "r") as miarch:
        lineas = [lineas.strip("\n") for lineas in miarch.readlines()]
        print("Primeras " + str(numero) + " lineas:")
        return lineas[:numero]

print(primeras_lineas(6, r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"))