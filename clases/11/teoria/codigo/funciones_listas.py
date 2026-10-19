# -*- coding: utf-8 -*-
"""
Clase 11 - Funciones con listas (diapositivas 24 a 29).

Tres casos:
    1. La funcion recibe una lista y devuelve un valor: calcular_promedio
    2. La funcion devuelve una lista nueva: leer_notas
    3. La funcion modifica la lista que recibe: aplicar_bonificacion
"""

NOTA_MAXIMA = 5.0


############ Funciones ############

# Caso 1: recibe una lista y devuelve un valor
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


# Caso 2: devuelve una lista nueva
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


# Caso 3: modifica la lista que recibe
def aplicar_bonificacion(notas, puntos):
    """
    Suma una bonificacion a cada nota, sin pasar de la nota maxima.

    Supone:
        notas es una lista de numeros entre 0.0 y 5.0, y puntos >= 0.
    Garantiza:
        MODIFICA la lista notas: a cada nota le suma puntos, y si el
        resultado pasa de 5.0, la deja en 5.0. No retorna nada.
    """
    for i in range(len(notas)):
        notas[i] = notas[i] + puntos
        if notas[i] > NOTA_MAXIMA:
            notas[i] = NOTA_MAXIMA


############ Pruebas ##############

# calcular_promedio
assert round(calcular_promedio([3.0, 4.5, 2.0, 4.0]), 3) == 3.375  # tipico
assert calcular_promedio([3.5]) == 3.5                              # limite: un elemento
assert calcular_promedio([4.0, 4.0, 4.0]) == 4.0                    # especial: todas iguales

# calcular_promedio no modifica la lista
datos = [3.0, 4.5, 2.0, 4.0]
calcular_promedio(datos)
assert datos == [3.0, 4.5, 2.0, 4.0]

# aplicar_bonificacion: se llama y despues se revisa la lista
datos = [3.0, 4.5, 2.0, 4.0]
aplicar_bonificacion(datos, 0.5)
assert datos == [3.5, 5.0, 2.5, 4.5]          # 4.5 + 0.5 = 5.0: limite

datos = [4.8, 1.0]
aplicar_bonificacion(datos, 0.5)
assert datos == [5.0, 1.5]                    # 4.8 + 0.5 pasa de 5.0

datos = [3.0, 4.5]
aplicar_bonificacion(datos, 0)
assert datos == [3.0, 4.5]                    # sin bonificacion no cambia

print("Todas las pruebas pasaron")


############ Programa principal #########

def main():
    notas = [3.0, 4.5, 2.0, 4.0]
    print("Antes:  ", notas)
    aplicar_bonificacion(notas, 0.5)
    print("Despues:", notas)                  # la lista cambio, sin return


if __name__ == "__main__":
    main()
