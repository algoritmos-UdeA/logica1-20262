# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:21:24 2026

@author: Soportedrai
"""

nota_num = 82
nota_letra = 'X' # Nota desconocia

if (nota_num < 0) or (nota_num > 100):
    print("ERROR: Nota fuera de rango")
    # rango [0,100]
elif (nota_num >= 90):
    # rango [90,100]
    nota_letra = 'A'
elif (nota_num >= 80):
    # rango [80,90]
    nota_letra = 'B'
elif (nota_num >= 70):
    # rango [70,80]
    nota_letra = 'C'
elif (nota_num >= 60):
    # rango [60,70]
    nota_letra = 'D'
else:
    # rango [0,60)
    nota_letra = 'E'

print(nota_letra)
    