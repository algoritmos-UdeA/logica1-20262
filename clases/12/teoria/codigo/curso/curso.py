"""
Clase 12 - Integrador: administración de notas de un curso.

El curso se guarda en tres arreglos paralelos de tamaño N (el cupo):
ids, nombres y notas. La posición i de los tres corresponde al mismo
estudiante. Solo las posiciones 0 a cantidad - 1 tienen datos; el resto
está libre.
"""
from ordenamientos import intercambiar


def buscar_id(ids, cantidad, id_buscado):
    """
    Busca un Id entre los estudiantes inscritos (búsqueda lineal).

    Supone:
        0 <= cantidad <= len(ids).
    Garantiza:
        Retorna la posición de id_buscado entre 0 y cantidad - 1,
        o -1 si no está. No modifica ids.
    """
    pos = -1
    for i in range(cantidad):
        if ids[i] == id_buscado:
            pos = i
            break
    return pos


def agregar_estudiante(ids, nombres, notas, cantidad, id_nuevo, nombre, nota):
    """
    Agrega un estudiante al final de los inscritos.

    Supone:
        ids, nombres y notas tienen el mismo tamaño (el cupo).
        0 <= cantidad <= len(ids).
    Garantiza:
        Si hay cupo y id_nuevo no está inscrito, MODIFICA ids, nombres y
        notas (guarda los datos en la posición cantidad) y retorna
        cantidad + 1. Si no, no modifica nada y retorna cantidad.
    """
    if cantidad < len(ids) and buscar_id(ids, cantidad, id_nuevo) == -1:
        ids[cantidad] = id_nuevo
        nombres[cantidad] = nombre
        notas[cantidad] = nota
        cantidad = cantidad + 1
    return cantidad


def eliminar_estudiante(ids, nombres, notas, cantidad, id_buscado):
    """
    Elimina un estudiante por Id, corriendo los siguientes a la izquierda.

    Supone:
        0 <= cantidad <= len(ids).
    Garantiza:
        Si id_buscado está inscrito, MODIFICA ids, nombres y notas (los
        estudiantes que estaban después quedan una posición a la
        izquierda y la última ocupada se libera) y retorna cantidad - 1.
        Si no está, no modifica nada y retorna cantidad.
    """
    pos = buscar_id(ids, cantidad, id_buscado)
    if pos != -1:
        for i in range(pos, cantidad - 1):
            ids[i] = ids[i + 1]
            nombres[i] = nombres[i + 1]
            notas[i] = notas[i + 1]
        cantidad = cantidad - 1
        ids[cantidad] = ""
        nombres[cantidad] = ""
        notas[cantidad] = 0.0
    return cantidad


def actualizar_nota(ids, notas, cantidad, id_buscado, nota):
    """
    Cambia la nota de un estudiante.

    Supone:
        0 <= cantidad <= len(ids).
    Garantiza:
        Si id_buscado está inscrito, MODIFICA notas (su nota pasa a ser
        nota) y retorna True. Si no, no modifica nada y retorna False.
    """
    pos = buscar_id(ids, cantidad, id_buscado)
    encontrado = False
    if pos != -1:
        notas[pos] = nota
        encontrado = True
    return encontrado


def mostrar_listado(ids, nombres, notas, cantidad):
    """
    Supone: 0 <= cantidad <= len(ids).
    Garantiza: imprime una línea por estudiante inscrito (Id, nombre y
    nota). No modifica nada. No retorna nada.
    """
    print("Id", "\t", "Nombre", "\t", "Nota")
    for i in range(cantidad):
        print(ids[i], "\t", nombres[i], "\t", notas[i])


def intercambiar_estudiantes(ids, nombres, notas, i, j):
    """
    Supone: i y j son posiciones válidas de los tres arreglos.
    Garantiza: MODIFICA ids, nombres y notas: los estudiantes de las
    posiciones i y j quedan intercambiados en los tres. No retorna nada.
    """
    intercambiar(ids, i, j)
    intercambiar(nombres, i, j)
    intercambiar(notas, i, j)


def posicion_mayor_nota(notas, inicio, cantidad):
    """
    Supone: 0 <= inicio < cantidad <= len(notas).
    Garantiza: retorna la posición de la mayor nota entre inicio y
    cantidad - 1 (si se repite, la primera). No modifica notas.
    """
    pos_mayor = inicio
    for j in range(inicio + 1, cantidad):
        if notas[j] > notas[pos_mayor]:
            pos_mayor = j
    return pos_mayor


def ordenar_por_nota(ids, nombres, notas, cantidad):
    """
    Ordena el curso de mayor a menor nota (selección).

    Supone:
        0 <= cantidad <= len(ids).
    Garantiza:
        MODIFICA ids, nombres y notas: los inscritos quedan de mayor a
        menor nota, y cada estudiante conserva su Id, nombre y nota.
        Las posiciones libres no cambian. No retorna nada.
    """
    for i in range(cantidad - 1):
        pos_mayor = posicion_mayor_nota(notas, i, cantidad)
        intercambiar_estudiantes(ids, nombres, notas, i, pos_mayor)


def posicion_menor_nombre(nombres, inicio, cantidad):
    """
    Supone: 0 <= inicio < cantidad <= len(nombres). Los nombres empiezan
    con mayúscula y no llevan tilde (si no, < no sigue el orden del
    diccionario).
    Garantiza: retorna la posición del nombre que va primero en orden
    alfabético entre inicio y cantidad - 1. No modifica nombres.
    """
    pos_menor = inicio
    for j in range(inicio + 1, cantidad):
        if nombres[j] < nombres[pos_menor]:
            pos_menor = j
    return pos_menor


def ordenar_por_nombre(ids, nombres, notas, cantidad):
    """
    Ordena el curso alfabéticamente por nombre (selección).

    Supone:
        0 <= cantidad <= len(ids).
    Garantiza:
        MODIFICA ids, nombres y notas: los inscritos quedan en orden
        alfabético, y cada estudiante conserva su Id, nombre y nota.
        Las posiciones libres no cambian. No retorna nada.
    """
    for i in range(cantidad - 1):
        pos_menor = posicion_menor_nombre(nombres, i, cantidad)
        intercambiar_estudiantes(ids, nombres, notas, i, pos_menor)
