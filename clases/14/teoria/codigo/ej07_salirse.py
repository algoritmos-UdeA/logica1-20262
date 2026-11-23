"""
Clase 14 - Cuidado con salirse de la matriz.

La matriz tiene N = 4 filas y M = 3 columnas. Si se intercambian N y M
en los ciclos, j llega a 3 y notas[0][3] no existe: IndexError.
"""

notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]
N = 4
M = 3

for i in range(M):          # ERROR: deberia ser range(N)
    for j in range(N):      # ERROR: deberia ser range(M)
        print(notas[i][j])
