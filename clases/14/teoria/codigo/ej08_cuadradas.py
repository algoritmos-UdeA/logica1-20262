"""
Clase 14 - Recorridos en una matriz cuadrada (N filas y N columnas).

Diagonal principal: la fila y la columna son iguales, A[i][i].
Diagonal secundaria: la columna depende de la fila, A[i][N - 1 - i].
Triangular superior: en cada fila, la columna empieza en i.
Triangular inferior: en cada fila, la columna llega hasta i.
"""

A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
N = 4

principal = 0
for i in range(N):
    principal = principal + A[i][i]
print("Diagonal principal:", principal)

secundaria = 0
for i in range(N):
    secundaria = secundaria + A[i][N - 1 - i]
print("Diagonal secundaria:", secundaria)

superior = 0
for i in range(N):
    for j in range(i, N):
        superior = superior + A[i][j]
print("Triangular superior:", superior)

inferior = 0
for i in range(N):
    for j in range(i + 1):
        inferior = inferior + A[i][j]
print("Triangular inferior:", inferior)
