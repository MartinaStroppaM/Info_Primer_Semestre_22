# Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). 
# El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. 
# El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. 
# El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. 
# Si un gorrión nunca comió, los coeficientes deben ser `None`.
# Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2

class Gorrión:
    def __init__(self):
        self.gramos = 0
        self.kms = 0
        self.lista_gramos = []
        self.lista_kms = []

    def comer(self, gramos):
        self.gramos += gramos 
        self.lista_gramos.append(gramos)
    
    def volar(self, kms):
        self.kms += kms
        self.lista_kms.append(kms)

    def CSS(self):
        if self.gramos > 0:
            return self.kms/self.gramos
        else:
            return None

    def CSSP(self):
        if self.gramos > 0:    
            return max(self.lista_kms)/max(self.lista_gramos)
        else:
            return None

    def CSSV(self):
        if self.gramos > 0:   
            return len(self.lista_kms)/len(self.lista_gramos)
        else:
            return None

    def esta_en_equilibrio(self):
        return 0.5 < self.CSS() < 2

agus = Gorrión()
print("CSS de Agus: ", agus.CSS())
agus.comer(50)
agus.volar(10)
print("CSSV de Agus: ", agus.CSS())
            

