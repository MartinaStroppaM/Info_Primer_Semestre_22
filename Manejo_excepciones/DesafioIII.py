# ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? 
# Reescribí la función incorporando una declaración try-except

def division(numero, divisor):
    try:
        return(numero/divisor)
    except ZeroDivisionError:
        print("Ops!Hoy estoy quemada")

print(division(3,2))
print(division(2,0))