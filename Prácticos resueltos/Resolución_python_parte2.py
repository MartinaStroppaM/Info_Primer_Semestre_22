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
#Terminar

#EJERCICIO 4:

def cobro_entrega(continente, peso_paquete):
    if peso_paquete <= 5:
        if  continente == "América del Sur":
            print("El precio del paquete a " + continente + " es de " + str(10*peso_paquete) + " dólares")
        elif continente == "América Central":
            print("El precio del paquete a " + continente + " es de " + str(15*peso_paquete) + " dólares ")
        elif continente == "América del Norte":
            print("El precio del paquete a " + continente + " es de " + str(18*peso_paquete) + " dólares ")
        elif continente == "Europa":
            print("El precio del paquete a " + continente + " es de " + str(24*peso_paquete) + " dólares ")
        elif continente == "Asia":
            print("El precio del paquete a " + continente + " es de " + str(30*peso_paquete) + " dólares ")
    else:
        print("El paquete no se puede transportar")

cobro_entrega("Europa", 6)

#EJERCICIO 5:

def dia_de_semana(numero):
    if 0<numero<=7:
        if numero == 1:
            print("Lunes")
        elif numero == 2:
            print("Martes")
        elif numero == 3:
            print("Miércoles")
        elif numero == 4:
            print("Jueves")
        elif numero == 5:
            print("Viernes")
        elif numero == 6:
            print("Sabado")
        else:
            print("Domingo")
    else:
        print("El número ingresado está fuera de rango")
        
dia_de_semana(2)

#EJERCICIO 6:

