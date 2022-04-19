#Manipulación de archivos

#Ejercicio 1:

def empieza_con(letra, archivo):
    with open(archivo, "r") as miarch:
        count = 0
        for line in miarch:
            if line.startswith(letra.upper()) or line.startswith(letra.lower()):
                pass
            else:
                count += 1
    print("El número de líneas que no empiezan con " + letra + " es " + str(count))

empieza_con("A", r"Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt")

#EJERCICIO 2:

def primeras_n_lineas(archivo, número):
    with open(archivo, "r") as miarch:
        lineas = [lineas.strip("\n") for lineas in miarch.readlines()]
        print("Primeras " + str(número) + " líneas: ") 
        print(lineas[:número])

primeras_n_lineas(r"Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt", 10)

#EJERCICIO 3:

def n_ultimas_lineas(archivo, número):
    with open(archivo, "r") as miarch:
           lineas2 = [lineas2.strip("\n") for lineas2 in miarch.readlines()]
           print("Últimas " + str(número) + " líneas: ") 
           print(lineas2[-(número):])

n_ultimas_lineas(r"Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt", 5)

def n_ultimas_lineas2(archivo, número):
    with open(archivo, "r") as miarch:
        for line in miarch:
            lineas3 = miarch.readlines()
            print("Últimas " + str(número) + " líneas: ")  
            print(lineas3[-(número):])

n_ultimas_lineas2(r"Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt", 5)
#Esta última te devuelve las últimas línas pero con "\n" que indicaría donde se encuentra el salto de línea

#EJERCICIO 4:

def cantidad_de_palabras(archivo):
    with open(archivo, "r") as miarch:
        for line in miarch:
            lineas4 = miarch.read()
            print("La cantidad de palabras que tiene el archivo es de " + str(len(lineas4.split())))

cantidad_de_palabras(r"Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")

#EJERCICIO 5: No lo entiendo  

#EJERCICIO 6:

def eliminar_saltos(archivo):
    with open(archivo, "r") as miarch:
        lines = [lines.strip("\n") for lines in miarch.readlines()]
        with open("nuevo_archivo.py", "w") as nuevo_archivo:
            nuevo_archivo.write(str(lines))

eliminar_saltos(r"Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")
#No se como crear el archivo en la carpeta donde estoy parada

#EJERCICIO 7:

def palabra_mas_larga(archivo):
    with open(archivo, "r") as miarch:
        word_list1 = []
        
        miarch.read().split()
        palabra = word_list1[0]
        for i in word_list1:
            if len(word_list1[i]) > len(palabra):
              palabra = word_list1[i]  
            return "La palabra más larga es: " + palabra + "con " + len(palabra) + " caracteres."
        
palabra_mas_larga(r"Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")

#EJERCICIO 8:

#EJERCICIO 9:

def word_counter (archivo):
    frecuencias = dict()
    with open (archivo, "r") as f:
        word_list = f.read().split()
        for i in word_list:
            if i in frecuencias:
                frecuencias[i] += 1
            else:
                frecuencias [i]= 1
        for word in frecuencias.keys():
            frecuencias[word] = round(frecuencias[word] / len(word_list),3)
    print(frecuencias)

    word_counter(r"Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")
    #No se que devuelve

#EJERCICIO 10:

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