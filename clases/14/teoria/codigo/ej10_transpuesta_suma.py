"""
Clase 14 - Transpuesta y suma de matrices.

Las dos operaciones crean una matriz NUEVA; las originales no cambian.
La transpuesta de una matriz de N x M es de M x N: T[j][i] = A[i][j].
La suma solo se define para matrices del mismo tamano.
"""

A = [[1, 2, 3],
     [4, 5, 6]]
B = [[10, 20, 30],
     [40, 50, 60]]
N = 2
M = 3

# Transpuesta: M filas y N columnas
T = [0] * M
for j in range(M):
    T[j] = [0] * N
for i in range(N):
    for j in range(M):
        T[j][i] = A[i][j]
print("Transpuesta:", T)

# Suma: C[i][j] = A[i][j] + B[i][j]
C = [0] * N
for i in range(N):
    C[i] = [0] * M
for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
print("Suma:", C)
print("A no cambio:", A)
