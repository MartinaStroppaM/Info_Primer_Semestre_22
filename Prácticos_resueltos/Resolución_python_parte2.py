# Práctica de introducción a Python - Parte 2

#EJERCICIO 1:

cadena = input("Frase de tu canción favorita: ")
def primera_letra(cadena):
    if cadena[0] == cadena[0].upper():
        print("Empieza con mayúscula")
    else:
        print("Empieza con minúscula")

primera_letra(cadena)

#EJERCICIO 2

numero = int(input("Número: "))
def analisis_del_numero(numero):
    if numero > 0 and numero%2 == 0:
        print("El número " + str(numero) + " es positivo y par")
    elif numero> 0 and numero%2 != 0:
        print("El número " + str(numero) + " es positivo e impar")
    elif numero<0 and numero%2 == 0:
        print("El número " + str(numero) + " es negativo y par")
    elif numero == 0 and numero%2 == 0:
        print("El número 0 es par")
    else:
        print("El número " + str(numero) + " es negativo e impar")

analisis_del_numero(numero)

#EJERCICIO 3:

numero = input("Número del 1 al 6: ")
def opuesto_dado(numero):
    if 1 < numero <= 6:
        print()
    else:
        print("El número ingresado es incorrecto")

