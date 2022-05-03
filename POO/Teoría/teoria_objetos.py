from aves import pepita, anastasia, roberta, juanita, chimuelo, hipo

print(pepita.volar_en_circulos())
#print(pepita.cantar_boleros())
print(pepita.comer_alpiste(10))
print(pepita.energia)
print("pepita come", pepita.comer_alpiste(10)) 
print("Energía de pepita después de comer", pepita.energia) 
print("Pepita vuela", pepita.volar_en_circulos())
print("Energía de pepita después de volar", pepita.energia)
print("Pepita come", pepita.comer_alpiste(1)) #¿Cuánto le aumenta el alpiste en energía?
print("Energía de pepita después de volar", pepita.energia) #Aumenta en 4
print("Pepita vuela", pepita.volar_en_circulos()) #¿Cuánta energía consume pepita volando?
print("Energía de pepita después de volar", pepita.energia) #Disminuye en 10

print(anastasia == pepita) #No son el mismo objeto, por lo tanto los objetos tienen identidad
print(anastasia.energia)
print(anastasia)
print("Anastasia come", anastasia.comer_alpiste(10))
print("Energía de Anastasia después de comer", anastasia.energia) #Suma 40
print("Anastasia vuela", anastasia.volar_en_circulos())
print("Energía de Anastasia después de volar", anastasia.energia) #Consume 10 de energía
#Se comportan igual, pero podrían comportarse diferente.

print(roberta)
print(roberta.energia)
print("Roberta vuela", roberta.volar_en_circulos()) #Consume 1 de energía
print("Energía de Roberta después de volar", roberta.energia)
#print("Roberta come", roberta.comer_alpiste(10))
print("Roberta escupe fuego", roberta.escupir_fuego())
print("Energía de Roberta después de escupir fuego", roberta.energia) #Consume 20 de energía
print("Roberta come", roberta.comer_peces(10))
print("Energía de Roberta después de comer", roberta.energia) #Aumenta en 1000
print("Roberta come una unidad", roberta.comer_peces(1))
print("Energía de Roberta después de comer 1 pez", roberta.energia) #Una unidad aumenta en 100
#Roberta comparte interfaz parcialmente con Pepita, por ejemplo entiende volar en círculos, pero no comer alpiste. 
print("Cantidad de dientes de Roberta", roberta.cantidad_dientes)

print("¿Pepita es igual a Juanita?", pepita == juanita)
print("Pepita", pepita) #Tienen distinto cógigo
print("Juanita", juanita)

print("¿Pepita está débil?", pepita.esta_débil())
print("Energía de Pepita", pepita.energia) #Pepita tiene más de 10 de energía
print("¿Roberta está débil?", roberta.esta_débil())
print("Energía de Roberta", roberta.energia) #Roberta tiene más de 50 de energía

print("¿Pepita está feliz?", pepita.esta_feliz()) #No está feliz porque su energía no supera los 500
print("¿Roberta está feliz?", roberta.esta_feliz()) #Ya es un atributo porque lo hereda de AnimalAlado

print("Hipo:", hipo)
print("¿Cuál es el equipo?", hipo.el_equipo)
print("¿Cuál es el equipo?", hipo.equipo)
print("Agrego a chimuelo", hipo.agregar_animal_alado(chimuelo))
print("¿Cuál es el equipo?", hipo.equipo)
print("Energía de Chimuelo", chimuelo.energia)
print("Energía de Roberta", roberta.energia)
hipo.entrenar_equipo()
#hipo.entrenar_dragon(chimuelo)
print("Energía de Chimuelo después", chimuelo.energia)
print("Energía de Roberta después", roberta.energia)