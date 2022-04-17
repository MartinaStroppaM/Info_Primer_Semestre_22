#Práctica introducción a Python parte 1

#EJERCICIO 1:

string = input("¿Cómo te llamás?: ")
print(len(string))

#EJERCICIO 2:

string2 = input("Decime tu apellido: ") 
if  len(string2) >= 6:
    print(string2.upper()[4:6])
else: 
    print("No tiene la cantidad de letras suficientes")

#EJERCICIO 3:

nombre_completo = input("¿Cuál es tu nombre completo?: ")
print("¡Hola " + nombre_completo + "!")

#EJERCICIO 4:

nombre_completo2 = input("Nombre: ")[0] + " " + input("Apellido: ")[0] + " " + input("Segundo apellido: ")[0]
print(nombre_completo2.upper())

#EJERCICIO 5: 

print("Escribir 3 números")
numeros = int((input("Numero 1: "))) + int((input("Numero 2: "))) + int(input("Numero 3: "))
print("Promedio = " + str(numeros / 3))

#EJERCICIO 6:

minutos = int(input("Cantidad de minutos: "))
if ((minutos % 60)> 0):
    print(str(int(minutos/60)) + " horas y " + str(minutos % 60) + " minutos")
elif (int(minutos/60) == 1):
    print(str(int(minutos/60)) + " hora")
else: 
    print(str(int(minutos/60)) + " horas")

#EJERCICIO 7:

#EJERCICIO 8:









