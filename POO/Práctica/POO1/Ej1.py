# Dada la siguiente clase, identificá la interfaz y el estado de la misma:

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

"""
La interfaz es el conjunto de "mensajes" o métodos que entiende el objeto.
En este caso la interfaz de Perro sería energía, comer, acariciar y estaDebil.
Sus estados son: alimento y caricias.
"""