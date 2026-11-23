"""
Clase 14 - Llenar una matriz.

Caso 1: el valor de cada casilla se pasa por teclado.
Caso 2: el valor de cada casilla proviene de una expresion.
"""

# Caso 1: por teclado
N = 4
M = 3
notas = [0.0] * N
for i in range(N):
    notas[i] = [0.0] * M
for i in range(N):
    for j in range(M):
        notas[i][j] = float(input(f"Nota del estudiante {i + 1}, parcial {j + 1}: "))

# Caso 2: por expresion, a partir de otra matriz
aprobo = [False] * N
for i in range(N):
    aprobo[i] = [False] * M
for i in range(N):
    for j in range(M):
        aprobo[i][j] = notas[i][j] >= 3.0

for i in range(N):
    print(aprobo[i])
