# Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. 
# Por ejemplo 150 minutos son 2 horas y 30 minutos.

minutos = int(input("Cantidad de minutos: "))
if ((minutos % 60)> 0):
    print(str(int(minutos/60)) + " horas y " + str(minutos % 60) + " minutos")
elif (int(minutos/60) == 1):
    print(str(int(minutos/60)) + " hora")
else: 
    print(str(int(minutos/60)) + " horas")