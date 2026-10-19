# -*- coding: utf-8 -*-
"""
Clase 11 - Modulo notas: funciones para el problema de las notas.

Problema: leer las notas de los estudiantes de un curso y mostrar
cuantas notas son mayores que el promedio (y en que posiciones estan).
"""


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


def contar_mayores_que(notas, valor):
    """
    Cuenta cuantas notas son mayores que un valor.

    Supone:
        notas es una lista de numeros (puede estar vacia) y valor es un numero.
    Garantiza:
        Retorna la cantidad de notas estrictamente mayores que valor (int).
        No modifica notas.
    """
    cantidad = 0
    for i in range(len(notas)):
        if notas[i] > valor:
            cantidad = cantidad + 1
    return cantidad


def posiciones_mayores_que(notas, valor):
    """
    Busca las posiciones de las notas mayores que un valor.

    Supone:
        notas es una lista de numeros (puede estar vacia) y valor es un numero.
    Garantiza:
        Retorna una lista nueva con las posiciones (int), en orden creciente,
        de las notas estrictamente mayores que valor. No modifica notas.
    """
    # Primero se cuenta, para crear un arreglo del tamano exacto
    cantidad = contar_mayores_que(notas, valor)
    posiciones = [0] * cantidad

    # Luego se llena: k indica la siguiente casilla libre de posiciones
    k = 0
    for i in range(len(notas)):
        if notas[i] > valor:
            posiciones[k] = i
            k = k + 1
    return posiciones


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
