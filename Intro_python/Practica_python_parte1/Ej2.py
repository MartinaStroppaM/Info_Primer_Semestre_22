# Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula 
# (Asegurarse de que el string tenga la cantidad de caracteres suficientes).

string = input("Apellido: ").upper()
if len(string) >= 6:
    print(string[4:6])
else:
    print("Su apellido no tiene suficientes caracteres")