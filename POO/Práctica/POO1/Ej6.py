# Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. 
# Este objeto debe entender los siguientes mensajes:

"""
* cargar(numero)

* sumar(numero)

* restar(numero)

* multiplicar(numero)

* valorActual()
"""

class Calculadora:
    def cargar(self, numero):
        self.inicial = numero

    def sumar(self, numero):
        self.inicial += numero

    def restar(self,numero):
        self.inicial -= numero
    
    def multiplicar(self, numero):
        self.inicial = self.inicial * numero

    def valorActual(self):
        return self.inicial

calculadora = Calculadora()

calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
print("El valor actual es igual a ", calculadora.valorActual())

