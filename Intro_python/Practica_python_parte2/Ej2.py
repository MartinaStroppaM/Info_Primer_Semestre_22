# Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

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