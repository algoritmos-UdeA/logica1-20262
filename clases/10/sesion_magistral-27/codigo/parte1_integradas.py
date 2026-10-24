# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 1: funciones integradas.

Funciones que vienen con Python y se usan sin importar nada.
Igual que las funciones propias, reciben argumentos y retornan un valor.
"""

# Valor absoluto
print(abs(-7))            # 7
print(abs(3.5))           # 3.5

# Redondeo al entero mas cercano, o con n decimales
print(round(-2.34))       # -2
print(round(2.38))        # 2
print(round(2.38, 1))     # 2.4

# Mayor y menor entre varios valores
print(max(2, 3, 10, 6))   # 10
print(min(2, 3, 10, 6))   # 2

# Adelanto de la clase 11: max y min tambien reciben una lista
notas = [2.0, 3.5, 4.8, 3.0]
print(f"Nota maxima: {max(notas)}")
print(f"Nota minima: {min(notas)}")
