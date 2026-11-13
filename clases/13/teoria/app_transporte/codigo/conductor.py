"""
Aplicación de transporte: la clase Conductor.

Un conductor tiene cédula, nombre, la placa de su vehículo, la posición
donde se encuentra y si está disponible. Igual que el cliente, crea su
propio objeto Punto (Conductor ◆── Punto).
"""
from punto import Punto


class Conductor:
    def __init__(self, cedula, nombre, placa):
        """
        Garantiza: crea un conductor disponible, ubicado en (0.0, 0.0).
        """
        self.__cedula = cedula
        self.__nombre = nombre
        self.__placa = placa
        self.__posicion = Punto(0.0, 0.0)
        self.__disponible = True

    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_placa(self):
        return self.__placa

    def get_posicion(self):
        """Garantiza: retorna el objeto Punto donde está el conductor."""
        return self.__posicion

    def set_posicion(self, x, y):
        """Garantiza: el conductor queda en (x, y)."""
        self.__posicion.set_x(x)
        self.__posicion.set_y(y)

    def esta_disponible(self):
        return self.__disponible

    def ocupar(self):
        """Garantiza: el conductor deja de estar disponible."""
        self.__disponible = False

    def liberar(self):
        """Garantiza: el conductor vuelve a estar disponible."""
        self.__disponible = True

    def __str__(self):
        estado = "ocupado"
        if self.__disponible:
            estado = "disponible"
        return (f"{self.__cedula} {self.__nombre} ({self.__placa}) "
                f"en {self.__posicion} {estado}")
