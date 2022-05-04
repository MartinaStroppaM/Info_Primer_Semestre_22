#Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada _Resultado_ 
#Por otro, que lea todos los archivos con extensión `.txt` y escriba el contenido de todos en un único archivo llamado *texto_completo.txt*,
#que tiene que estar dentro de la carpeta _Resultado_. 
# **NO se pueden usar rutas absolutas**

import os
import glob

def resultado_txt():
        os.mkdir("Resultado")
        txt = glob.glob("*.txt")

        with open(r"Resultado\texto_completo.txt", "a") as nuevoArch:
            for i in txt:
                arch = open(i, "r")
                nuevoArch.write(arch.read())
                arch.close()

resultado_txt()

