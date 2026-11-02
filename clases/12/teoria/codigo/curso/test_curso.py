"""Pruebas de curso.py. Se ejecutan con: python test_curso.py"""
from curso import (buscar_id, agregar_estudiante, eliminar_estudiante,
                   actualizar_nota, ordenar_por_nota, ordenar_por_nombre)

N = 10


def empieza_con(lista, esperado):
    """
    Supone: len(esperado) <= len(lista).
    Garantiza: retorna True si las primeras posiciones de lista son
    iguales, una por una, a las de esperado. No modifica nada.
    """
    iguales = True
    for k in range(len(esperado)):
        if lista[k] != esperado[k]:
            iguales = False
    return iguales


def curso_inicial():
    """Garantiza: retorna (ids, nombres, notas, cantidad) con los 4 estudiantes de ejemplo."""
    ids = [""] * N
    nombres = [""] * N
    notas = [0.0] * N
    cantidad = 0
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "000", "Ana", 3.0)
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "123", "Beto", 4.5)
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "987", "Carla", 2.0)
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "007", "Dario", 4.0)
    return ids, nombres, notas, cantidad


# buscar_id
ids, nombres, notas, cantidad = curso_inicial()
assert cantidad == 4
assert buscar_id(ids, cantidad, "987") == 2         # típico
assert buscar_id(ids, cantidad, "000") == 0         # límite: el primero
assert buscar_id(ids, cantidad, "007") == 3         # límite: el último
assert buscar_id(ids, cantidad, "555") == -1        # no está
assert buscar_id(ids, cantidad, "") == -1           # las casillas libres no cuentan

# agregar_estudiante
ids, nombres, notas, cantidad = curso_inicial()
cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "555", "Elena", 3.8)
assert cantidad == 5 and ids[4] == "555" and nombres[4] == "Elena" and notas[4] == 3.8
cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "123", "Otro", 1.0)
assert cantidad == 5 and nombres[1] == "Beto"       # Id repetido: no agrega
for k in range(5, N):                               # llenar el cupo
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "X" + str(k), "E" + str(k), 1.0)
assert cantidad == N
cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "999", "Lleno", 5.0)
assert cantidad == N and buscar_id(ids, cantidad, "999") == -1   # sin cupo: no agrega

# eliminar_estudiante
ids, nombres, notas, cantidad = curso_inicial()
cantidad = eliminar_estudiante(ids, nombres, notas, cantidad, "123")   # del medio
assert cantidad == 3
assert empieza_con(ids, ["000", "987", "007", ""])
assert empieza_con(nombres, ["Ana", "Carla", "Dario", ""])
assert empieza_con(notas, [3.0, 2.0, 4.0, 0.0])
cantidad = eliminar_estudiante(ids, nombres, notas, cantidad, "007")   # el último
assert cantidad == 2 and empieza_con(ids, ["000", "987", ""])
cantidad = eliminar_estudiante(ids, nombres, notas, cantidad, "555")   # no está
assert cantidad == 2

# actualizar_nota
ids, nombres, notas, cantidad = curso_inicial()
assert actualizar_nota(ids, notas, cantidad, "987", 3.5) == True
assert notas[2] == 3.5
assert actualizar_nota(ids, notas, cantidad, "555", 5.0) == False
assert empieza_con(notas, [3.0, 4.5, 3.5, 4.0])

# ordenar_por_nota (de mayor a menor)
ids, nombres, notas, cantidad = curso_inicial()
ordenar_por_nota(ids, nombres, notas, cantidad)
assert empieza_con(notas, [4.5, 4.0, 3.0, 2.0])
assert empieza_con(nombres, ["Beto", "Dario", "Ana", "Carla"])
assert empieza_con(ids, ["123", "007", "000", "987"])
for k in range(4, N):
    assert notas[k] == 0.0                          # las libres no se tocan

# ordenar_por_nombre (alfabético)
ids, nombres, notas, cantidad = curso_inicial()
ordenar_por_nota(ids, nombres, notas, cantidad)     # se desordena primero
ordenar_por_nombre(ids, nombres, notas, cantidad)
assert empieza_con(nombres, ["Ana", "Beto", "Carla", "Dario"])
assert empieza_con(ids, ["000", "123", "987", "007"])
assert empieza_con(notas, [3.0, 4.5, 2.0, 4.0])

# Casos especiales de ordenar: curso vacío y un solo estudiante
ids = [""] * N
nombres = [""] * N
notas = [0.0] * N
ordenar_por_nota(ids, nombres, notas, 0)
assert notas == [0.0] * N
cantidad = agregar_estudiante(ids, nombres, notas, 0, "000", "Ana", 3.0)
ordenar_por_nombre(ids, nombres, notas, cantidad)
assert nombres[0] == "Ana"

print("Pruebas de curso: todas pasaron")
