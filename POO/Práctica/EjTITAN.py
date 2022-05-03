class Titan:
    def __init__(self, salud):
        self.salud = salud

    def recibir_ataque(self, daño_recibido):
        self.salud -= daño_recibido * 1.5

    def esta_vivo(self):
        return self.salud > 0

    def salud_actual(self):
        return self.salud

    def destruir_casas(self):
        if (self.cuantas_casas() > 1):
            if ((self.cuantas_casas() % 1) > 0):
                self.salud -= (self.cuantas_casas()//1)* 12.5 #Calculo el resto para que le quede algo de energía
            else:
                self.salud -= (self.cuantas_casas() - 1) * 12.5 #Le resto 1 para que le quede algo de energía y no se muera
        else:
            print("No puede destruir ninguna casa")

    def cuantas_casas(self):
        if self.esta_vivo():
            return self.salud * 0.08
        else:
            return "Titan died ☠️"

    def grito(self):
        return "¡Aaaarrrg!"


titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
print(titan1.salud_actual())
titan1.destruir_casas()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())
    