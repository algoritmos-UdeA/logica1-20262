"""
Administración de notas de un curso (versión POO): la clase Curso.

El curso guarda un arreglo de objetos Estudiante de tamaño cupo y cuántos
están inscritos (cantidad). Solo las posiciones 0 a cantidad - 1 tienen
estudiantes; el resto vale None.

El Curso no crea estudiantes: los recibe ya creados en agregar_estudiante.
Por eso la relación es de agregación (Curso ◇── Estudiante) y este archivo
no necesita importar estudiante.py.
"""
from ordenamientos import intercambiar


class Curso:
    def __init__(self, cupo):
        """
        Supone: cupo > 0.
        Garantiza: crea un curso vacío con capacidad para cupo estudiantes.
        """
        self.__estudiantes = [None] * cupo
        self.__cantidad = 0

    def get_cantidad(self):
        return self.__cantidad

    def get_estudiante(self, posicion):
        """
        Supone: 0 <= posicion < cantidad.
        Garantiza: retorna el estudiante de esa posición.
        """
        return self.__estudiantes[posicion]

    def buscar_id(self, id):
        """
        Garantiza: retorna la posición del estudiante con ese Id
        (búsqueda lineal), o -1 si no está inscrito.
        """
        pos = -1
        for i in range(self.__cantidad):
            if self.__estudiantes[i].get_id() == id:
                pos = i
                break
        return pos

    def agregar_estudiante(self, estudiante):
        """
        Garantiza: si hay cupo y su Id no está inscrito, guarda el
        estudiante al final de los inscritos y retorna True. Si no, no
        cambia nada y retorna False.
        """
        agregado = False
        if (self.__cantidad < len(self.__estudiantes)
                and self.buscar_id(estudiante.get_id()) == -1):
            self.__estudiantes[self.__cantidad] = estudiante
            self.__cantidad = self.__cantidad + 1
            agregado = True
        return agregado

    def eliminar_estudiante(self, id):
        """
        Garantiza: si el Id está inscrito, lo elimina corriendo a la
        izquierda los estudiantes que estaban después y retorna True.
        Si no, no cambia nada y retorna False.
        """
        pos = self.buscar_id(id)
        eliminado = False
        if pos != -1:
            for i in range(pos, self.__cantidad - 1):
                self.__estudiantes[i] = self.__estudiantes[i + 1]
            self.__cantidad = self.__cantidad - 1
            self.__estudiantes[self.__cantidad] = None
            eliminado = True
        return eliminado

    def actualizar_nota(self, id, nota):
        """
        Garantiza: si el Id está inscrito y la nota es válida (la valida
        set_nota), cambia su nota y retorna True. Si no, retorna False.
        """
        pos = self.buscar_id(id)
        actualizada = False
        if pos != -1:
            actualizada = self.__estudiantes[pos].set_nota(nota)
        return actualizada

    def mostrar_listado(self):
        """Garantiza: imprime una línea por estudiante inscrito. No retorna nada."""
        print("Id", "\t", "Nombre", "\t", "Nota")
        for i in range(self.__cantidad):
            print(self.__estudiantes[i])

    def posicion_mayor_nota(self, inicio=0):
        """
        Supone: 0 <= inicio < cantidad.
        Garantiza: retorna la posición de la mayor nota entre inicio y
        cantidad - 1 (si se repite, la primera).
        """
        pos_mayor = inicio
        for j in range(inicio + 1, self.__cantidad):
            if (self.__estudiantes[j].get_nota()
                    > self.__estudiantes[pos_mayor].get_nota()):
                pos_mayor = j
        return pos_mayor

    def ordenar_por_nota(self):
        """
        Garantiza: los inscritos quedan de mayor a menor nota (selección).
        Cada intercambio mueve un estudiante completo. No retorna nada.
        """
        for i in range(self.__cantidad - 1):
            pos_mayor = self.posicion_mayor_nota(i)
            intercambiar(self.__estudiantes, i, pos_mayor)

    def posicion_menor_nombre(self, inicio=0):
        """
        Supone: 0 <= inicio < cantidad. Los nombres empiezan con mayúscula
        y no llevan tilde (si no, < no sigue el orden del diccionario).
        Garantiza: retorna la posición del nombre que va primero en orden
        alfabético entre inicio y cantidad - 1.
        """
        pos_menor = inicio
        for j in range(inicio + 1, self.__cantidad):
            if (self.__estudiantes[j].get_nombre()
                    < self.__estudiantes[pos_menor].get_nombre()):
                pos_menor = j
        return pos_menor

    def ordenar_por_nombre(self):
        """
        Garantiza: los inscritos quedan en orden alfabético (selección).
        No retorna nada.
        """
        for i in range(self.__cantidad - 1):
            pos_menor = self.posicion_menor_nombre(i)
            intercambiar(self.__estudiantes, i, pos_menor)
