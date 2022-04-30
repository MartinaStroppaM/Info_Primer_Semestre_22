# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def ultimas_lineas(numero, archivo):
    with open(archivo, "r") as miarch:
        lineas = [lineas.strip("\n") for lineas in miarch.readlines()]
        print("Últimas " + str(numero) + " lineas:")
        return lineas[-numero:]

print(ultimas_lineas(6, r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"))