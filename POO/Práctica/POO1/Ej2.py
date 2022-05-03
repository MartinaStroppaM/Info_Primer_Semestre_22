# Modificá el método **volar** de la clase `Golondrina` visto en la clase de teoría,
# de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

import re


class Golondrina(AnimalAlado):
    def __init__(self, energia):
        self.energia = energia

    def volar(self, kms):
        if (self.energia - (10 + kms)) > 0: 
            self.energia -= 10 + kms
        else:
            return "No puede volar"

