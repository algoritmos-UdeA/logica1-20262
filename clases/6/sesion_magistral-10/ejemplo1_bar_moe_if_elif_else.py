# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:10:35 2026

@author: Soportedrai
"""

# Constantea
PRECIO_HOMBRES = 10000
PRECIO_MUJERES = PRECIO_HOMBRES//2

#

# Entradas
sexo = input("Digite el sexo (M: Hombre / F: Mujer): ")

# Proceso
if (sexo == 'M') or (sexo == 'm'):
    # Hombre
    precio = PRECIO_HOMBRES
elif(sexo == 'F') or (sexo == 'f'):
    # Mujer
    precio = PRECIO_MUJERES
else:
    # Otro
    print("ERROR: Genero no valido. Se conbra lo normal")
    precio = PRECIO_HOMBRES
# Salidas
print(f"Valor: {precio}")
