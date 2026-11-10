"""Pruebas de curso.py. Se ejecutan con: python test_curso.py"""
from estudiante import Estudiante
from curso import Curso

N = 10


def curso_inicial():
    """Garantiza: retorna un Curso de cupo N con los 4 estudiantes de ejemplo."""
    curso = Curso(N)
    curso.agregar_estudiante(Estudiante("000", "Ana", 3.0))
    curso.agregar_estudiante(Estudiante("123", "Beto", 4.5))
    curso.agregar_estudiante(Estudiante("987", "Carla", 2.0))
    curso.agregar_estudiante(Estudiante("007", "Dario", 4.0))
    return curso


def ids_del_curso(curso):
    """Garantiza: retorna una lista con los Id de los inscritos, en orden."""
    ids = [""] * curso.get_cantidad()
    for i in range(curso.get_cantidad()):
        ids[i] = curso.get_estudiante(i).get_id()
    return ids


def nombres_del_curso(curso):
    """Garantiza: retorna una lista con los nombres de los inscritos, en orden."""
    nombres = [""] * curso.get_cantidad()
    for i in range(curso.get_cantidad()):
        nombres[i] = curso.get_estudiante(i).get_nombre()
    return nombres


def notas_del_curso(curso):
    """Garantiza: retorna una lista con las notas de los inscritos, en orden."""
    notas = [0.0] * curso.get_cantidad()
    for i in range(curso.get_cantidad()):
        notas[i] = curso.get_estudiante(i).get_nota()
    return notas


# buscar_id
curso = curso_inicial()
assert curso.get_cantidad() == 4
assert curso.buscar_id("987") == 2          # típico
assert curso.buscar_id("000") == 0          # límite: el primero
assert curso.buscar_id("007") == 3          # límite: el último
assert curso.buscar_id("555") == -1         # no está
assert Curso(N).buscar_id("000") == -1      # curso vacío

# agregar_estudiante
curso = curso_inicial()
assert curso.agregar_estudiante(Estudiante("555", "Elena", 3.8)) == True
assert curso.get_cantidad() == 5 and curso.get_estudiante(4).get_nombre() == "Elena"
assert curso.agregar_estudiante(Estudiante("123", "Otro", 1.0)) == False   # Id repetido
assert curso.get_cantidad() == 5 and curso.get_estudiante(1).get_nombre() == "Beto"
for k in range(5, N):                       # llenar el cupo
    curso.agregar_estudiante(Estudiante("X" + str(k), "E" + str(k), 1.0))
assert curso.get_cantidad() == N
assert curso.agregar_estudiante(Estudiante("999", "Lleno", 5.0)) == False  # sin cupo
assert curso.get_cantidad() == N and curso.buscar_id("999") == -1

# eliminar_estudiante
curso = curso_inicial()
assert curso.eliminar_estudiante("123") == True                 # del medio
assert ids_del_curso(curso) == ["000", "987", "007"]
assert nombres_del_curso(curso) == ["Ana", "Carla", "Dario"]
assert notas_del_curso(curso) == [3.0, 2.0, 4.0]
assert curso.eliminar_estudiante("007") == True                 # el último
assert ids_del_curso(curso) == ["000", "987"]
assert curso.eliminar_estudiante("555") == False                # no está
assert curso.get_cantidad() == 2

# actualizar_nota
curso = curso_inicial()
assert curso.actualizar_nota("987", 3.5) == True
assert curso.get_estudiante(2).get_nota() == 3.5
assert curso.actualizar_nota("555", 5.0) == False               # no está
assert curso.actualizar_nota("987", 7.0) == False               # nota inválida
assert notas_del_curso(curso) == [3.0, 4.5, 3.5, 4.0]

# ordenar_por_nota (de mayor a menor)
curso = curso_inicial()
curso.ordenar_por_nota()
assert notas_del_curso(curso) == [4.5, 4.0, 3.0, 2.0]
assert nombres_del_curso(curso) == ["Beto", "Dario", "Ana", "Carla"]
assert ids_del_curso(curso) == ["123", "007", "000", "987"]

# ordenar_por_nombre (alfabético)
curso = curso_inicial()
curso.ordenar_por_nota()                    # se desordena primero
curso.ordenar_por_nombre()
assert nombres_del_curso(curso) == ["Ana", "Beto", "Carla", "Dario"]
assert ids_del_curso(curso) == ["000", "123", "987", "007"]
assert notas_del_curso(curso) == [3.0, 4.5, 2.0, 4.0]

# ordenar_por_nota con notas repetidas: cada nombre sigue con su nota
curso = Curso(3)
curso.agregar_estudiante(Estudiante("1", "Ana", 4.0))
curso.agregar_estudiante(Estudiante("2", "Beto", 3.0))
curso.agregar_estudiante(Estudiante("3", "Carla", 4.0))
curso.ordenar_por_nota()
assert notas_del_curso(curso) == [4.0, 4.0, 3.0]
assert nombres_del_curso(curso) == ["Ana", "Carla", "Beto"]

# Casos especiales de ordenar: curso vacío y un solo estudiante
curso = Curso(N)
curso.ordenar_por_nota()
assert curso.get_cantidad() == 0
curso.agregar_estudiante(Estudiante("000", "Ana", 3.0))
curso.ordenar_por_nombre()
assert nombres_del_curso(curso) == ["Ana"]

print("Pruebas de curso: todas pasaron")
