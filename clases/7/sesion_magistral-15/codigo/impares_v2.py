# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:02:56 2026

@author: Soportedrai
"""


cant_pares = 0
cant_impares = 0
sum_pares = 0
sum_impares = 0
i = 0 
N = int(input("Digite la cantidad de numeros a ingresar: "))
while i < N:
    # print(i)   # Para mirar el estado de i
    num = int(input(f"Ingrese el numero {i + 1}: "))
    if num%2 == 0:
        # Caso numero par
        cant_pares += 1    # cant_pares = cant_pares + 1
        sum_pares += num   # sum_pares = sum_pares + num
    else:
        # Caso numero impar
        cant_impares += 1
        sum_impares += num
    i = i + 1


if (cant_impares == 0) and (cant_pares == 0):
    # No se ingresaron numeros
    print("No se ingresaron numeros")
elif cant_pares == 0:
    # Todos los numeros ingresados fueron impares
    print("No se ingresaron pares")
    prom_impares = sum_impares/cant_impares
    print(f"El promedio de los {cant_impares} ingresados fue {prom_impares:.2f}")
elif cant_impares == 0:
    # Todos los numeros ingresados fueron pares
    print("No se ingresaron impares")
    prom_pares = sum_pares/cant_pares
    print(f"El promedio de los {cant_pares} ingresados fue {prom_pares:.2f}")
else:
    # Se ingresaron tanto numeros pares como impares
    prom_pares = sum_pares/cant_pares
    prom_impares = sum_impares/cant_impares
    print(f"El promedio de los {cant_pares} ingresados fue {prom_pares:.2f}")
    print(f"El promedio de los {cant_impares} ingresados fue {prom_impares:.2f}")