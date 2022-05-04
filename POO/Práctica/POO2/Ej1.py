# Dadas las siguientes clases responder:
# ¿Cuáles son sus estados?
# ¿Cuáles son sus interfaces?
# ¿Comparten interfaz?
# ¿Son polimórficas?

class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0
        """Los estados de Perro son alimento y caricias"""

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
	    print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
	    self.alimento -= km / 4

    """Su interfaz es: energía, comer, alimento, acariciar, estaDebil y pasear"""

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0
        """Los estados de Gato son alimento y caricias"""

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
	    print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4

    """Su interfaz es: energía, comer, caricias, acariciar, y estaDebil"""

"""Ambas clases comparten parcialmente su interfaz; pero para ser polimorficas requieren de un espectador (3er objeto) observándolos"""