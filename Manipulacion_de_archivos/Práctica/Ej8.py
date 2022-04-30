# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def guardar_contenido(archivo1, archivo2):
    with open(archivo1, "r") as miarch1:
        contenido1 = miarch1.read()
    with open(archivo2, "r") as miarch2:
        contenido2 = miarch2.read()
    agregar = contenido1 + "\n" + contenido2
    with open(r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Repo\Info_Primer_Semestre_22\Manipulacion_de_archivos\Práctica\Doc_ya_existente.txt", "r+") as nuevoArch:
        nuevoArch.write(agregar)
        nuevoArch.read()

guardar_contenido(r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Repo\Info_Primer_Semestre_22\Manipulacion_de_archivos\Teoría\bio.txt", r"C:\Users\marti\OneDrive\Escritorio\Martina\UCEMA\2022_Primer_Cuatri\Informática\Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt")

