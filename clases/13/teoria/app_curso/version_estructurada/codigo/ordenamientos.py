"""
Clase 12 - Métodos de ordenamiento (todos ordenan de menor a mayor).

Funciones de apoyo: intercambiar (caso 3) y posicion_menor (caso 1).
Métodos: ordenar_seleccion, ordenar_burbuja y ordenar_insercion (caso 3).
"""


def intercambiar(lista, i, j):
    """
    Intercambia los elementos de las posiciones i y j de una lista.

    Supone:
        i y j son posiciones válidas de lista (0 a len(lista) - 1).
    Garantiza:
        MODIFICA lista: el valor que estaba en i queda en j, y el que
        estaba en j queda en i. No retorna nada.
    """
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp


def posicion_menor(lista, inicio):
    """
    Busca el menor elemento desde la posición inicio hasta el final.

    Supone:
        0 <= inicio < len(lista).
    Garantiza:
        Retorna la posición del menor valor entre lista[inicio] y el
        último elemento (si se repite, la primera). No modifica lista.
    """
    pos_menor = inicio
    for j in range(inicio + 1, len(lista)):
        if lista[j] < lista[pos_menor]:
            pos_menor = j
    return pos_menor


def ordenar_seleccion(lista):
    """
    Ordena una lista de menor a mayor con el método de selección.

    Supone:
        Los elementos de lista se pueden comparar con <.
    Garantiza:
        MODIFICA lista: queda ordenada de menor a mayor. No retorna nada.
    """
    for i in range(len(lista) - 1):
        pos_menor = posicion_menor(lista, i)
        intercambiar(lista, i, pos_menor)


def ordenar_burbuja(lista):
    """
    Ordena una lista de menor a mayor con el método de la burbuja.

    Supone:
        Los elementos de lista se pueden comparar con >.
    Garantiza:
        MODIFICA lista: queda ordenada de menor a mayor. Se detiene antes
        si en una pasada no hubo intercambios. No retorna nada.
    """
    n = len(lista)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                intercambiar(lista, j, j + 1)
                hubo_intercambio = True
        if not hubo_intercambio:
            break


def ordenar_insercion(lista):
    """
    Ordena una lista de menor a mayor con el método de inserción.

    Supone:
        Los elementos de lista se pueden comparar con >.
    Garantiza:
        MODIFICA lista: queda ordenada de menor a mayor. No retorna nada.
    """
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = actual


def main():
    for ordenar in (ordenar_seleccion, ordenar_burbuja, ordenar_insercion):
        X = [29, 10, 14, 37, 13]
        ordenar(X)
        print(f"{ordenar.__name__}: {X}")


if __name__ == "__main__":
    main()
