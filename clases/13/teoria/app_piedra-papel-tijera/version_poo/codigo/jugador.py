"""
Piedra, papel o tijera (versión POO): la clase Jugador.

Un jugador guarda juntos su nombre y sus puntos (rondas ganadas). Los
puntos solo cambian con sumar_punto: nadie puede restarlos ni ponerlos
en un valor cualquiera desde afuera.
"""


class Jugador:
    def __init__(self, nombre):
        """Garantiza: crea un jugador con ese nombre y 0 puntos."""
        self.__nombre = nombre
        self.__puntos = 0

    def get_nombre(self):
        return self.__nombre

    def get_puntos(self):
        return self.__puntos

    def sumar_punto(self):
        """Garantiza: los puntos aumentan en 1. No retorna nada."""
        self.__puntos = self.__puntos + 1

    def __str__(self):
        """Garantiza: retorna 'nombre: puntos', por ejemplo 'Ana: 2'."""
        return self.__nombre + ": " + str(self.__puntos)
