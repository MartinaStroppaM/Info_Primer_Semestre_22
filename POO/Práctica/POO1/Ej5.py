# Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. 
# Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo). 
# El método para saber el último comando es `ultimoComando`, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador:
    def __init__(self, valor):
        self.valor = valor
        self.ultimo_comando = ""

    def inc(self):
        self.valor += 1
        self.ultimo_comando = "incremento"

    def dis(self):
        self.valor -= 1
        self.ultimo_comando = "disminución"

    def reset(self):
        self.valor = 0
        self.ultimo_comando = "resetear"

    def valorActual(self):
        return self.valor
    
    def valorNuevo(self, nuevo_valor):
        self.valor = nuevo_valor
        self.ultimo_comando = "actualización"
        return self.valor

    def ultimoComando(self):
        return self.ultimo_comando

contador = Contador(10)

contador.inc()
contador.inc()
print(contador.ultimoComando())
contador.dis()
print(contador.ultimoComando())
contador.inc()
print("valorActual: ", contador.valorActual())
print("valorNuevo: ", contador.valorNuevo(27))
print(contador.ultimoComando())
contador.dis()
contador.dis()
print("valorActual: ", contador.valorActual())
print(contador.ultimoComando())