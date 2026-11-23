"""
Clase 14 - La clase Matriz.

Una Matriz guarda sus datos (una lista de listas) junto con su numero
de filas y de columnas. Quien usa la clase no toca la lista de listas:
pide y guarda valores con get y set, y las operaciones son metodos.
"""


class Matriz:

    def __init__(self, filas, columnas, valor=0.0):
        """
        Supone:
            filas y columnas son enteros mayores que 0.
        Garantiza:
            Crea una matriz de filas x columnas con todas las casillas
            en valor (0.0 si no se da).
        """
        self.__filas = filas
        self.__columnas = columnas
        self.__datos = [0.0] * filas
        for i in range(filas):
            self.__datos[i] = [valor] * columnas

    def get_filas(self):
        return self.__filas

    def get_columnas(self):
        return self.__columnas

    def es_posicion_valida(self, i, j):
        """Garantiza: retorna True si (i, j) es una casilla de la matriz."""
        return 0 <= i < self.__filas and 0 <= j < self.__columnas

    def get(self, i, j):
        """
        Supone:
            (i, j) es una posicion valida.
        Garantiza:
            Retorna el valor de la casilla (i, j).
        """
        return self.__datos[i][j]

    def set(self, i, j, valor):
        """
        Garantiza:
            Si (i, j) es una posicion valida, guarda valor en esa casilla
            y retorna True. Si no, no cambia nada y retorna False.
        """
        guardado = False
        if self.es_posicion_valida(i, j):
            self.__datos[i][j] = valor
            guardado = True
        return guardado

    def sumar_fila(self, i):
        """
        Supone:
            0 <= i < filas.
        Garantiza:
            Retorna la suma de la fila i.
        """
        suma = 0.0
        for j in range(self.__columnas):
            suma = suma + self.__datos[i][j]
        return suma

    def sumar_columna(self, j):
        """
        Supone:
            0 <= j < columnas.
        Garantiza:
            Retorna la suma de la columna j.
        """
        suma = 0.0
        for i in range(self.__filas):
            suma = suma + self.__datos[i][j]
        return suma

    def es_cuadrada(self):
        """Garantiza: retorna True si la matriz tiene tantas filas como columnas."""
        return self.__filas == self.__columnas

    def transpuesta(self):
        """
        Garantiza:
            Retorna una Matriz NUEVA de columnas x filas, donde la
            casilla (j, i) tiene el valor de la casilla (i, j) de esta.
            Esta matriz no cambia.
        """
        resultado = Matriz(self.__columnas, self.__filas)
        for i in range(self.__filas):
            for j in range(self.__columnas):
                resultado.set(j, i, self.__datos[i][j])
        return resultado

    def sumar(self, otra):
        """
        Supone:
            otra es una Matriz del mismo tamano que esta.
        Garantiza:
            Retorna una Matriz NUEVA con la suma casilla por casilla.
            Ni esta matriz ni otra cambian.
        """
        resultado = Matriz(self.__filas, self.__columnas)
        for i in range(self.__filas):
            for j in range(self.__columnas):
                resultado.set(i, j, self.__datos[i][j] + otra.get(i, j))
        return resultado

    def __str__(self):
        texto = ""
        for i in range(self.__filas):
            for j in range(self.__columnas):
                texto = texto + f"{self.__datos[i][j]:6.1f}"
            if i < self.__filas - 1:
                texto = texto + "\n"
        return texto
