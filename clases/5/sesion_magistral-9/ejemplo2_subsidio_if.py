# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:43:51 2026

@author: Soportedrai
"""

# Constantes
SAL_MINIMO = 2_000_000

# Inicializacion
subsidio = 0

# Entradas
cedula = input("Digite la cedula: ")
sal_base = float(input("Digite el salario base: "))

# Proceso
if sal_base < SAL_MINIMO:
    subsidio = 0.3*sal_base

sal_neto = sal_base + subsidio

# Salidas
print("-----------------------")
print(f"{cedula} recibe ${sal_neto}")
print("-----------------------")

