"""
Clase 12 - Búsqueda lineal y búsqueda binaria.
"""


def buscar_lineal(lista, valor):
    """
    Busca un valor en una lista, recorriéndola desde la posición 0.

    Supone:
        lista es una lista (no necesita estar ordenada).
    Garantiza:
        Retorna la posición de la primera aparición de valor en lista,
        o -1 si valor no está. No modifica lista.
    """
    pos = -1
    for i in range(len(lista)):
        if lista[i] == valor:
            pos = i
            break
    return pos


def buscar_binaria(lista, valor):
    """
    Busca un valor en una lista ordenada, partiéndola a la mitad en cada paso.

    Supone:
        lista está ordenada de menor a mayor.
    Garantiza:
        Retorna una posición donde está valor, o -1 si valor no está.
        No modifica lista.
    """
    inicio = 0
    fin = len(lista) - 1
    pos = -1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            pos = medio
            break
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return pos


def main():
    X = [5.0, 4.0, 3.5, 2.87]
    print(buscar_lineal(X, 3.5))
    Y = [2, 5, 10, 12, 15, 17, 20]
    print(buscar_binaria(Y, 15))


if __name__ == "__main__":
    main()
