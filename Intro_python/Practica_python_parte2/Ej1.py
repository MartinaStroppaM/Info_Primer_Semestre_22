# Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

cadena = input("Frase de tu canción favorita: ")
def primera_letra(cadena):
    if cadena[0] == cadena[0].upper():
        print("Empieza con mayúscula")
    else:
        print("Empieza con minúscula")

primera_letra(cadena)