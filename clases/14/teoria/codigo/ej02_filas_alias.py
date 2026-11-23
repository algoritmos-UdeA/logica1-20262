"""
Clase 14 - Asi NO se crea una matriz.

[[0.0] * M] * N repite N veces la MISMA fila: las N casillas de la
lista externa apuntan a una sola lista. Al cambiar una casilla, el
cambio aparece en todas las filas, y Python no da ningun error.
"""

N = 4
M = 3

mal = [[0.0] * M] * N       # una sola fila, repetida N veces
mal[0][0] = 5.0
print(mal)                  # la columna 0 cambio en las 4 filas

bien = [0.0] * N            # la forma correcta: una fila nueva por vuelta
for i in range(N):
    bien[i] = [0.0] * M
bien[0][0] = 5.0
print(bien)                 # solo cambio la fila 0
