# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:35:22 2026

@author: Soportedrai
"""


VALOR_BUSCADO = 0
encontrado = False
i = 0

N = int(input('Ingrese el número de números: '))
while (i < N):
    i += 1   # i = i + 1
    num = int(input(f'Ingrese el número {i}: '))    
    if num == VALOR_BUSCADO:
        encontrado = True      
        break

if encontrado:
    print(str(VALOR_BUSCADO) +  
          " encontrado en la posición " +  
          str(i))
else:
    print(str(VALOR_BUSCADO) + " no encontrado")