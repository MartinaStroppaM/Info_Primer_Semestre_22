# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def word_counter(archivo):
    frecuencias = dict()
    with open(archivo, "r") as miarch:
        word_list = miarch.read().split()
        for word in word_list:
            if word in frecuencias:
                frecuencias[word] += 1
            else: 
                frecuencias[word] = 1
        for palabra in frecuencias.keys():
            frecuencias[palabra] = round(frecuencias[palabra] / len(word_list),3)
        print(frecuencias)

print(word_counter(r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"))
