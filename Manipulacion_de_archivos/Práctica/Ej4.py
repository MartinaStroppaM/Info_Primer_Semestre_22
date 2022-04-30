# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def cantidad_de_palabras(archivo):
    with open(archivo, "r") as miarch:
        for line in miarch:
            lineas = miarch.read()
            return "El archivo tiene " + str(len(lineas.split())) + " palabras."

print(cantidad_de_palabras(r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"))