"""
Aplicación de transporte: la clase Punto.

Un punto es un lugar de la ciudad, con coordenadas x e y medidas en
kilómetros. Es la clase más sencilla de la aplicación: no conoce a
ninguna otra, y por eso es la primera que se escribe y se prueba.
"""
import math


class Punto:
    def __init__(self, x=0.0, y=0.0):
        """
        Garantiza: crea el punto (x, y). Si no se dan valores, crea el
        punto (0.0, 0.0).
        """
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def calcular_distancia(self, otro):
        """
        Supone: otro es un objeto Punto.
        Garantiza: retorna la distancia en línea recta entre este punto
        y el otro. No modifica ninguno de los dos.
        """
        dx = self.__x - otro.get_x()
        dy = self.__y - otro.get_y()
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return f"({self.__x}, {self.__y})"
