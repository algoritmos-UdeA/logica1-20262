"""
Clase 14 - Recorrer y acumular.

Total: un solo acumulador para toda la matriz.
Por fila: el acumulador se reinicia al empezar cada fila, y el
resultado de cada fila se guarda en un arreglo de N casillas.
Por columna: lo mismo, recorriendo por columnas, en un arreglo de M.
"""

notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]
N = 4
M = 3

# Total y promedio general
suma = 0.0
for i in range(N):
    for j in range(M):
        suma = suma + notas[i][j]
print(f"Suma: {suma}  Promedio general: {suma / (N * M):.2f}")

# Promedio de cada estudiante (por fila)
promedio_estudiante = [0.0] * N
for i in range(N):
    suma = 0.0                      # se reinicia en cada fila
    for j in range(M):
        suma = suma + notas[i][j]
    promedio_estudiante[i] = suma / M
for i in range(N):
    print(f"Estudiante {i}: {promedio_estudiante[i]:.2f}")

# Promedio de cada parcial (por columna)
promedio_parcial = [0.0] * M
for j in range(M):
    suma = 0.0                      # se reinicia en cada columna
    for i in range(N):
        suma = suma + notas[i][j]
    promedio_parcial[j] = suma / N
for j in range(M):
    print(f"Parcial {j + 1}: {promedio_parcial[j]:.2f}")

# Contar: cuantas notas son menores que 3.0
perdidas = 0
for i in range(N):
    for j in range(M):
        if notas[i][j] < 3.0:
            perdidas = perdidas + 1
print("Notas menores que 3.0:", perdidas)
