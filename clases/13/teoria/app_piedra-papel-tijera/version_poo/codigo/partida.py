"""
Piedra, papel o tijera (versión POO): la clase Partida.

La partida recibe a los dos jugadores ya creados (agregación:
Partida ◇── Jugador) y crea cada ronda dentro de jugar_ronda
(composición: Partida ◆── Ronda). Por eso este archivo importa ronda.py
pero no jugador.py.
"""
from reglas import GANA_USUARIO, GANA_MAQUINA
from ronda import Ronda


class Partida:
    def __init__(self, usuario, maquina, rondas_para_ganar=3):
        """
        Supone: usuario y maquina son objetos Jugador con 0 puntos;
        rondas_para_ganar > 0.
        Garantiza: crea una partida que todavía no tiene rondas.
        """
        self.__usuario = usuario
        self.__maquina = maquina
        self.__rondas_para_ganar = rondas_para_ganar
        self.__ultima_ronda = None
        self.__cantidad_rondas = 0

    def get_ultima_ronda(self):
        """Garantiza: retorna la última ronda jugada, o None si no hay."""
        return self.__ultima_ronda

    def get_cantidad_rondas(self):
        return self.__cantidad_rondas

    def jugar_ronda(self, jugada_usuario, jugada_maquina):
        """
        Supone: la partida no ha terminado; las jugadas son válidas.
        Garantiza: crea la ronda, le suma un punto a quien la gana (a
        nadie si es empate) y retorna su resultado.
        """
        ronda = Ronda(self.__usuario, jugada_usuario,
                      self.__maquina, jugada_maquina)
        resultado = ronda.get_resultado()
        if resultado == GANA_USUARIO:
            self.__usuario.sumar_punto()
        elif resultado == GANA_MAQUINA:
            self.__maquina.sumar_punto()
        self.__ultima_ronda = ronda
        self.__cantidad_rondas = self.__cantidad_rondas + 1
        return resultado

    def terminada(self):
        """
        Garantiza: retorna True si alguno de los dos ya ganó
        rondas_para_ganar rondas, y False si no.
        """
        return (self.__usuario.get_puntos() == self.__rondas_para_ganar
                or self.__maquina.get_puntos() == self.__rondas_para_ganar)

    def get_ganador(self):
        """
        Supone: la partida terminó.
        Garantiza: retorna el jugador que tiene más puntos.
        """
        ganador = self.__maquina
        if self.__usuario.get_puntos() > self.__maquina.get_puntos():
            ganador = self.__usuario
        return ganador

    def __str__(self):
        """Garantiza: retorna el marcador, por ejemplo "Ana 2 - 1 Máquina"."""
        return (self.__usuario.get_nombre() + " "
                + str(self.__usuario.get_puntos()) + " - "
                + str(self.__maquina.get_puntos()) + " "
                + self.__maquina.get_nombre())
