# Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

# comienzan con una cantidad que podemos establecer de _combustible_
# los autos pueden llevar 5 personas como máximo y al _recorrer_ una distancia consumen medio litro de _combustible_ por cada kilómetro recorrido
# las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;
# pueden *cargar_combustible* en la cantidad que digamos y al hacerlo suben su cantidad de _combustible_
# saben responder si _entran_ una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

# Definí las clases **Moto**, **Auto** y **MedioDeTransporte** y hace que las dos primeras hereden de la tercera.

class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible

    def cargar_combustible(self, cantidad):
        self.combustible += cantidad

    def entran_personas(self, pasajeros):
        return self.maximo_personas() >= pasajeros

class Moto(MedioDeTransporte):
    def maximo_personas(self):
      return 2
    
    def recorrer(self,  distancia):
        self.combustible -= distancia

class Auto(MedioDeTransporte):
    def maximo_personas(self):
      return 5

    def recorrer(self,  distancia):
        self.combustible -= distancia * 0.5

moto1 = Moto(100)
auto1 = Auto(100)
print("Combustible de la moto: ", moto1.combustible)
print("Combustible del auto: ", auto1.combustible)
moto1.cargar_combustible(100)
auto1.cargar_combustible(100)
print("Combustible de la moto: ", moto1.combustible)
print("Combustible del auto: ", auto1.combustible)
moto1.recorrer(10)
auto1.recorrer(10)
print("Combustible de la moto: ", moto1.combustible)
print("Combustible del auto: ", auto1.combustible)
print("¿Entran 5 en la moto?", moto1.entran_personas(5))
print("Entran 5 en el auto?", auto1.entran_personas(5))