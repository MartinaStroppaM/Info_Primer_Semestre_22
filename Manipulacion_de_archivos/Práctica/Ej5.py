# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

def replace(letra, archivo):
    with open(archivo, "r") as miarch:
        reemplazar = miarch.read().replace(letra, letra + "\n")
        with open("Replace.txt", "w") as nuevoArch:
            nuevoArch.write(reemplazar)

replace("a", r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")

