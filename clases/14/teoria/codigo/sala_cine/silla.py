"""
Clase 14 - Sala de cine: la clase Silla.

Una silla sabe en que fila (una letra) y en que numero esta, y si esta
ocupada. Se cuenta desde 1, como la ve el publico: la silla A1 es la
primera de la fila A.
"""


class Silla:

    def __init__(self, fila, numero):
        """
        Supone:
            fila es una letra mayuscula y numero es un entero >= 1.
        Garantiza:
            Crea una silla libre con esa fila y ese numero.
        """
        self.__fila = fila
        self.__numero = numero
        self.__ocupada = False

    def get_fila(self):
        return self.__fila

    def get_numero(self):
        return self.__numero

    def esta_libre(self):
        """Garantiza: retorna True si la silla no esta ocupada."""
        return not self.__ocupada

    def ocupar(self):
        """
        Garantiza:
            Si la silla estaba libre, la ocupa y retorna True.
            Si ya estaba ocupada, no cambia nada y retorna False.
        """
        ocupada_ahora = False
        if not self.__ocupada:
            self.__ocupada = True
            ocupada_ahora = True
        return ocupada_ahora

    def liberar(self):
        """
        Garantiza:
            Si la silla estaba ocupada, la libera y retorna True.
            Si ya estaba libre, no cambia nada y retorna False.
        """
        liberada = False
        if self.__ocupada:
            self.__ocupada = False
            liberada = True
        return liberada

    def __str__(self):
        texto = "O"
        if self.__ocupada:
            texto = "X"
        return texto
