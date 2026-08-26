# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:15:38 2026

@author: Soportedrai
"""

# Constantea
PRECIO_HOMBRES = 10000
PRECIO_MUJERES = PRECIO_HOMBRES/2

# Entradas
sexo = input("Digite el sexo (M: Hombre / F: Mujer): ")

# Proceso
if sexo == 'M':
    precio = PRECIO_HOMBRES
else:
    precio = PRECIO_MUJERES

# Salidas
print(f"Valor: {precio}")
