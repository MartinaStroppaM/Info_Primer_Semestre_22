# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def palabra_mas_larga(archivo):
    largo = 0
    mas_larga = ""
    with open(archivo, "r") as miarch:
       palabras = miarch.read().split()
       for word in palabras:
           if len(word) > largo:
               largo = len(word)
               mas_larga = word
    return "La palabra más larga es: " + mas_larga + " y tiene " + str(largo) + " caracteres."

print(palabra_mas_larga(r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"))

    