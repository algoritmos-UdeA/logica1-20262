# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:26:48 2026

@author: Soportedrai
"""
# Constantea
NOTA_MINIMA = 3.0

# Inicializacion de variables
est_aprob = 0
est_reprob = 0
suma_aprob = 0
suma_reprob = 0


# Entradas
N = int(input("Numero de estudiantes: "))
for i in range(N):
    # print(i)
    # Solicitud de nota
    nota = float(input("- Digite la nota: "))
    if nota >= NOTA_MINIMA:
        # Gano
        est_aprob += 1 # est_aprob = est_aprob + 1 
        suma_aprob += nota
    else:
        # perdio
        est_reprob += 1 
        suma_reprob += nota


# Validaciones
if N <= 0:
    # No hay estutiantes
    print("No hay estudiantes")
else:
    if est_reprob == 0:
        # Todos ganadon
        prom_reprob = 0
        prom_aprob = suma_aprob/est_aprob
    elif est_aprob == 0:
        # Todos perdieron
        prom_aprob = 0
        prom_reprob = suma_reprob/est_reprob
    else:
        # Hay estudiantes que ganaron y que perdieron
        prom_reprob = suma_reprob/est_reprob
        prom_aprob = suma_aprob/est_aprob

    # Promedio de notas
    prom_nota = (suma_reprob + suma_aprob)/N

    # Despliegue de resultados
    print(f"Ganaron: {est_aprob}")
    print(f"Perdieron: {est_reprob}")
    print(f"Prom reprob: {prom_reprob}")
    print(f"Prom aprob: {prom_aprob}")
    print(f"Prom nota: {prom_nota}")

    
    


