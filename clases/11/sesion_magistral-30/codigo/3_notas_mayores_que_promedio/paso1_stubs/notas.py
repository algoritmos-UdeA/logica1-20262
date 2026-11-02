# -*- coding: utf-8 -*-
"""
Clase 11 - Modulo notas: funciones para el problema de las notas.

Problema: leer las notas de los estudiantes de un curso y mostrar
cuantas notas son mayores que el promedio (y en que posiciones estan).

PASO 1: las dos funciones nuevas ya tienen su especificacion (el
contrato), pero todavia son stubs: retornan un valor fijo.
"""


# Reutilizada (Caso 2): ya estaba hecha y probada
def leer_notas(n):
    """
    Pide n notas al usuario y las guarda en una lista.

    Supone:
        n es un entero mayor que 0.
    Garantiza:
        Retorna una lista nueva con las n notas leidas, en el orden
        en que se escribieron.
    """
    notas = [0.0] * n
    for i in range(n):
        notas[i] = float(input(f"Nota del estudiante {i + 1}: "))
    return notas


# Reutilizada (Caso 1): ya estaba hecha y probada
def calcular_promedio(notas):
    """
    Calcula el promedio de las notas de una lista.

    Supone:
        notas es una lista de numeros con al menos un elemento.
    Garantiza:
        Retorna el promedio de las notas (float). No modifica notas.
    """
    suma = 0
    for i in range(len(notas)):
        suma = suma + notas[i]
    promedio = suma / len(notas)
    return promedio


# Nueva (Caso 1)
def contar_mayores_que(notas, valor):
    """
    Cuenta cuantas notas son mayores que un valor.

    Supone:
        notas es una lista de numeros (puede estar vacia) y valor es un numero.
    Garantiza:
        Retorna la cantidad de notas estrictamente mayores que valor (int).
        No modifica notas.
    """
    return 0  # STUB: falta implementarla


# Nueva (recibe una lista como el Caso 1 y devuelve una lista como el Caso 2)
def posiciones_mayores_que(notas, valor):
    """
    Busca las posiciones de las notas mayores que un valor.

    Supone:
        notas es una lista de numeros (puede estar vacia) y valor es un numero.
    Garantiza:
        Retorna una lista nueva con las posiciones (int), en orden creciente,
        de las notas estrictamente mayores que valor. No modifica notas.
    """
    return []  # STUB: falta implementarla


def mostrar_resultados(promedio, posiciones):
    """
    Muestra el promedio y las notas mayores que el promedio.

    Supone:
        promedio es un numero y posiciones es una lista de enteros.
    Garantiza:
        Imprime los resultados. No retorna nada.
    """
    print(f"Promedio del curso: {promedio:.2f}")
    print(f"Notas mayores que el promedio: {len(posiciones)}")
    print(f"Posiciones: {posiciones}")
