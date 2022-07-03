import pandas as pd
import seaborn as sns
import scipy.stats as ss

personas = pd.read_csv(r"C:\Users\marti\Downloads\personas_2011.csv", sep=";") 
#El sep solamente va a ser necesario en el caso que los separadores no sean comas

print(personas.head())
print(personas.info()) 
#Con Info sabemos que tipos de datos tenemos en cada columna.

print(personas.describe())
#Conocer los valores más comunes de una base de datos. Puedo saber si mis datos tienen una media y mediana similares.

# Averiguá para qué sirven los parámetro sep, index_col, nrows y header.

"""
El argumento sep se utiliza como separador que separa los objects que imprime la función print().
Index_col es un parámetro en read_csv. Se utiliza para especificar el valor de índice de la tabla.
Nrows:
Header:
"""

# DesafíoIV 

print(personas["seniority_level"].count("C"), "contar C")
