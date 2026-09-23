# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:19:40 2026

@author: Soportedrai
"""
# Inicializacion
fact = 1

# Entradas
num = int(input("Digite el numero: "))

# Proceso
for i in range(1,num+1,1):
    # print(f"i = {i}")
    fact = fact*i
    # print(f"fact = {fact}")
    # print("------")
# Salidas
if num >= 0:
    print(f"{num}! = {fact}")
else:
    print("ERROR: El numero debe ser positivo o 0")