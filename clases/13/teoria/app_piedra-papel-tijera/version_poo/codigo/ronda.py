"""
Piedra, papel o tijera (versión POO): la clase Ronda.

Una ronda guarda quién jugó, qué jugó cada uno y el resultado. Conoce a
los dos jugadores (asociación: Ronda ──> Jugador), pero no los crea ni
cambia sus puntos; solo usa sus nombres para describirse.
"""
from reglas import EMPATE, GANA_USUARIO, nombre_jugada, definir_ganador


class Ronda:
    def __init__(self, usuario, jugada_usuario, maquina, jugada_maquina):
        """
        Supone: usuario y maquina son objetos Jugador; las jugadas son
        PIEDRA, PAPEL o TIJERA.
        Garantiza: crea la ronda y calcula su resultado con definir_ganador.
        """
        self.__usuario = usuario
        self.__jugada_usuario = jugada_usuario
        self.__maquina = maquina
        self.__jugada_maquina = jugada_maquina
        self.__resultado = definir_ganador(jugada_usuario, jugada_maquina)

    def get_jugada_usuario(self):
        return self.__jugada_usuario

    def get_jugada_maquina(self):
        return self.__jugada_maquina

    def get_resultado(self):
        """Garantiza: retorna EMPATE, GANA_USUARIO o GANA_MAQUINA."""
        return self.__resultado

    def __str__(self):
        """
        Garantiza: retorna una línea que describe la ronda, por ejemplo
        "Ana: piedra | Máquina: tijera | gana Ana".
        """
        texto = (self.__usuario.get_nombre() + ": "
                 + nombre_jugada(self.__jugada_usuario) + " | "
                 + self.__maquina.get_nombre() + ": "
                 + nombre_jugada(self.__jugada_maquina) + " | ")
        if self.__resultado == EMPATE:
            texto = texto + "empate"
        elif self.__resultado == GANA_USUARIO:
            texto = texto + "gana " + self.__usuario.get_nombre()
        else:
            texto = texto + "gana " + self.__maquina.get_nombre()
        return texto
