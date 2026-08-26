# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:27:48 2026

@author: Soportedrai
"""


# Constantea
PRECIO_HOMBRES = 10000
PRECIO_MUJERES = PRECIO_HOMBRES//2
precio = PRECIO_HOMBRES

# Entradas
sexo = input("Digite el sexo (M: Hombre / F: Mujer): ")

if (sexo == 'F') or (sexo == 'f'):
    precio = PRECIO_MUJERES

# Salidas
print(f"Valor: {precio}")
