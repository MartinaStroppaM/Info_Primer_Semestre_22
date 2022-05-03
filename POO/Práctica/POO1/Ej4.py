# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. 
# También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. 
# Este objeto debe entender los siguientes mensajes:

"""
* inc()

* dis()

* reset()

* valorActual()

* valorNuevo(nuevoValor)
"""

class Contador:
    def __init__(self, valor):
        self.valor = valor

    def inc(self):
        self.valor += 1

    def dis(self):
        self.valor -= 1

    def reset(self):
        self.valor = 0

    def valorActual(self):
        return self.valor
    
    def valorNuevo(self, nuevo_valor):
        self.valor = nuevo_valor
        return self.valor


contador = Contador(10)

contador.inc()
contador.inc()
contador.dis()
contador.inc()
print("valorActual: ", contador.valorActual())
print("valorNuevo: ", contador.valorNuevo(27))
contador.dis()
contador.dis()
print("valorActual: ", contador.valorActual())