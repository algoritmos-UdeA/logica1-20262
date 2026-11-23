"""
Clase 14 - Notas de un curso con una matriz: funciones.

Los nombres van en un arreglo paralelo a las FILAS de la matriz de
notas, y los pesos de los parciales en un arreglo paralelo a las
COLUMNAS. La nota final de cada estudiante es la suma de cada nota por
el peso de su parcial.
"""


def leer_nombres(n):
    """
    Supone:
        n es un entero mayor que 0.
    Garantiza:
        Retorna una lista nueva con los n nombres leidos, en orden.
    """
    nombres = [""] * n
    for i in range(n):
        nombres[i] = input(f"Nombre del estudiante {i + 1}: ")
    return nombres


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


def calcular_notas_finales(notas, pesos):
    """
    Supone:
        notas es una matriz de numeros con al menos una fila, y pesos
        es una lista con un peso por columna de notas; los pesos suman
        1.0.
    Garantiza:
        Retorna una lista nueva con la nota final de cada fila: la suma
        de notas[i][j] * pesos[j]. No modifica notas ni pesos.
    """
    n = len(notas)
    finales = [0.0] * n
    for i in range(n):
        suma = 0.0
        for j in range(len(pesos)):
            suma = suma + notas[i][j] * pesos[j]
        finales[i] = suma
    return finales


def buscar_mayor(valores):
    """
    Supone:
        valores es una lista de numeros con al menos un elemento.
    Garantiza:
        Retorna el mayor valor de la lista. No modifica valores.
    """
    mayor = valores[0]
    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    return mayor


def buscar_menor(valores):
    """
    Supone:
        valores es una lista de numeros con al menos un elemento.
    Garantiza:
        Retorna el menor valor de la lista. No modifica valores.
    """
    menor = valores[0]
    for i in range(1, len(valores)):
        if valores[i] < menor:
            menor = valores[i]
    return menor


def contar_iguales(valores, valor):
    """
    Supone:
        valores es una lista de numeros (puede estar vacia).
    Garantiza:
        Retorna cuantos elementos de valores son iguales a valor.
        No modifica valores.
    """
    cantidad = 0
    for i in range(len(valores)):
        if valores[i] == valor:
            cantidad = cantidad + 1
    return cantidad


def posiciones_iguales(valores, valor):
    """
    Supone:
        valores es una lista de numeros (puede estar vacia).
    Garantiza:
        Retorna una lista nueva con las posiciones de valores donde hay
        un elemento igual a valor, en orden creciente. No modifica
        valores.
    """
    cantidad = contar_iguales(valores, valor)     # 1. contar
    posiciones = [0] * cantidad                   # 2. crear del tamano exacto
    k = 0                                         # 3. llenar
    for i in range(len(valores)):
        if valores[i] == valor:
            posiciones[k] = i
            k = k + 1
    return posiciones


def mostrar_estudiantes(titulo, nombres, finales, valor):
    """
    Supone:
        nombres y finales tienen el mismo tamano.
    Garantiza:
        Muestra el titulo y el nombre y la nota final de cada
        estudiante cuya nota final es igual a valor (si hay empate,
        se muestran todos).
    """
    print(f"{titulo}: {valor:.2f}")
    posiciones = posiciones_iguales(finales, valor)
    for k in range(len(posiciones)):
        print(f"  {nombres[posiciones[k]]}")
