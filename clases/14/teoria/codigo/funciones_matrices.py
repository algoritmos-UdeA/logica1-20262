"""
Clase 14 - Funciones con matrices: los tres casos.

Caso 1: recibe una matriz y retorna un valor (no la modifica).
Caso 2: retorna una matriz nueva.
Caso 3: modifica la matriz que recibe (y no retorna nada).

Las funciones no reciben N ni M: los obtienen con len(matriz), que da
el numero de filas, y len(matriz[0]), que da el numero de columnas.
"""

NOTA_MAXIMA = 5.0


def calcular_promedio_fila(notas, i):
    """
    Supone:
        notas es una matriz de numeros con al menos una columna, e i es
        una fila valida (0 <= i < len(notas)).
    Garantiza:
        Retorna el promedio de la fila i (float). No modifica notas.
    """
    suma = 0.0
    for j in range(len(notas[i])):
        suma = suma + notas[i][j]
    promedio = suma / len(notas[i])
    return promedio


def leer_notas(n, m):
    """
    Supone:
        n y m son enteros mayores que 0.
    Garantiza:
        Retorna una matriz nueva de n filas y m columnas con las notas
        leidas, en el orden en que se escribieron (por filas).
    """
    notas = [0.0] * n
    for i in range(n):
        notas[i] = [0.0] * m
    for i in range(n):
        for j in range(m):
            notas[i][j] = float(input(f"Estudiante {i + 1}, parcial {j + 1}: "))
    return notas


def aplicar_bonificacion(notas, j, puntos):
    """
    Supone:
        notas es una matriz de numeros entre 0.0 y 5.0, j es una columna
        valida y puntos >= 0.
    Garantiza:
        MODIFICA la matriz notas: a cada nota de la columna j le suma
        puntos, y si el resultado pasa de 5.0, la deja en 5.0. Las demas
        columnas no cambian. No retorna nada.
    """
    for i in range(len(notas)):
        notas[i][j] = notas[i][j] + puntos
        if notas[i][j] > NOTA_MAXIMA:
            notas[i][j] = NOTA_MAXIMA
