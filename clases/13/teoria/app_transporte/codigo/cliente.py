"""
Aplicación de transporte: la clase Cliente.

Un cliente tiene cédula, nombre y la posición donde se encuentra. La
posición es un objeto Punto que el cliente crea en su constructor: por
eso la relación es de composición (Cliente ◆── Punto) y este archivo
importa punto.py.
"""
from punto import Punto


class Cliente:
    def __init__(self, cedula, nombre):
        """
        Garantiza: crea un cliente ubicado en el punto (0.0, 0.0).
        """
        self.__cedula = cedula
        self.__nombre = nombre
        self.__posicion = Punto(0.0, 0.0)

    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_posicion(self):
        """Garantiza: retorna el objeto Punto donde está el cliente."""
        return self.__posicion

    def set_posicion(self, x, y):
        """
        Garantiza: el cliente queda en (x, y). No crea un punto nuevo:
        le pide a su punto que cambie sus coordenadas.
        """
        self.__posicion.set_x(x)
        self.__posicion.set_y(y)

    def __str__(self):
        return f"{self.__cedula} {self.__nombre} en {self.__posicion}"
