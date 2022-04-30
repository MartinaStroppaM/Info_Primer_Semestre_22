# Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

import glob
import os
def funcion1(archivo, ruta):
    os.listdir(ruta)
    lista_txt = glob.glob("*.txt")

    with open(archivo, "a") as s:
        for f in lista_txt:
            file = open(f, "r")
            s.write(file.read())
            file.close()

funcion1("Archivos_txt.txt", r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Repo\Info_Primer_Semestre_22\Manipulacion_de_archivos\Práctica")