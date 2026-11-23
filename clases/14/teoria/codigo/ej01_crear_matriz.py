"""
Clase 14 - Crear una matriz, guardar y leer valores.

La matriz se escribe en Python como una lista de listas: una lista con
N filas, y cada fila es una lista con M casillas. Se crea en dos pasos,
sin append: primero la lista de filas y despues cada fila.
"""

N = 4   # filas: los estudiantes
M = 3   # columnas: los parciales

# Paso 1: una lista con una casilla por fila
notas = [0.0] * N
# Paso 2: cada casilla pasa a ser una fila nueva con M casillas
for i in range(N):
    notas[i] = [0.0] * M

print(notas)

# Guardar y leer una casilla: primero la fila, despues la columna
notas[2][1] = 3.0                 # Carla (fila 2), parcial 2 (columna 1)
print(notas[2][1])
print(notas)

# Crear e inicializar a la vez: cada lista interna es una fila
notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]
print(notas[1][2])                # Beto, parcial 3
suma = notas[0][0] + notas[0][1]  # las casillas se usan en expresiones
print("Suma:", suma)
