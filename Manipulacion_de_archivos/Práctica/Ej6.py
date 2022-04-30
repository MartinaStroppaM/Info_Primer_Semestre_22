# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def eliminar_saltos(archivo):
    with open(archivo, "r") as miarch:
        lineas = [lineas.strip("\n") for lineas in miarch.readlines()]
        with open("Eliminar_saltos.txt", "w") as nuevoArch:
            nuevoArch.write(str(lineas))
            

eliminar_saltos(r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")