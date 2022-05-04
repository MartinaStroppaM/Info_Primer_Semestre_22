# Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. 
# Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. 
# Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: 
# hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos.

# Se propone:

# implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). 
# Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. 
# Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().
# comprobar el código que se escribió con esta secuencia:
	# definir un ornitólogo, dos golondrinas y dos gorriones,
	# inicializar las aves con valores conocidos,
	# decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
	# decirle al ornitólogo que realice su rutina sobre aves,
	# verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.

class Ornitologo:
    def __init__(self):
        self.aves = []

    def  estudiarAve(self, ave): 
        self.aves.append(ave)

    def avesEnEstudio(self):
        return self.aves

    def realizarRutinaSobreAves(self):
        [self.aves[i].comer(80) for i in range(len(self.aves))]
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer(10) for i in range(len(self.aves))]
       
    def avesEnEquilibrio(self):
        for ave in self.aves:
            return ave.esta_en_equilibrio()

class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer(self, gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms

    def esta_débil(self):
        return self.energia < 10
    
    def esta_en_equilibrio(self):
        return 150 <= self.energia <= 300

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

    def esta_en_equilibrio(self):
        return self.gramos > 100


perry = Ornitologo()
pepita = Golondrina(100)
juanita = Golondrina(100)
agus = Gorrión()
tincho = Gorrión()

perry.estudiarAve("pepita")
perry.estudiarAve("agus")
perry.estudiarAve("tincho")
print("Aves que estudia Perry: ", perry.aves)
perry.realizarRutinaSobreAves()
print(pepita)
print(juanita)
print(juanita.esta_en_equilibrio())


   