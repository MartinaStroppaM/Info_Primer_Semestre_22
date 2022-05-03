# Creá una clase `Notebook` cuyo estado sea: marca, modelo y precio.
# y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) 
# y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. 
# Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, porcentaje_descuento):
        return self.precio - (self.precio * porcentaje_descuento) / 100

HP = Notebook("HP", 2018, 10000)
ASUS = Notebook("Asus", 2022, 20000)

print("El modelo de la notebook HP es: ", HP.modelo)
print(ASUS.marca)
print("Precio de la notebook ASUS con descuento: ", ASUS.descuento(20))
print("Precio de la notebook HP con descuento: ", HP.descuento(50))