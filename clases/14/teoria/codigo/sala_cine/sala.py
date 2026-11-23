"""
Clase 14 - Sala de cine: la clase Sala.

La sala guarda sus sillas en una matriz de objetos Silla: la fila i de
la matriz es la fila de la sala con la letra LETRAS[i], y la columna j
es la silla numero j + 1. El publico cuenta desde 1 y con letras; la
matriz cuenta desde 0. La conversion se hace en un solo lugar:
get_silla.
"""

from silla import Silla


class Sala:

    LETRAS = "ABCDEFGHIJKL"     # la sala tiene a lo sumo 12 filas

    def __init__(self, filas, sillas_por_fila, precio):
        """
        Supone:
            1 <= filas <= 12, sillas_por_fila >= 1 y precio >= 0.
        Garantiza:
            Crea la sala con todas sus sillas libres (COMPOSICION: la
            sala crea sus sillas).
        """
        self.__filas = filas
        self.__sillas_por_fila = sillas_por_fila
        self.__precio = precio
        self.__vendidas = 0
        self.__sillas = [None] * filas
        for i in range(filas):
            self.__sillas[i] = [None] * sillas_por_fila
            for j in range(sillas_por_fila):
                self.__sillas[i][j] = Silla(Sala.LETRAS[i], j + 1)

    def get_filas(self):
        return self.__filas

    def get_sillas_por_fila(self):
        return self.__sillas_por_fila

    def indice_fila(self, letra):
        """
        Garantiza:
            Retorna el indice (desde 0) de la fila con esa letra, o -1
            si la sala no tiene esa fila.
        """
        indice = -1
        for i in range(self.__filas):
            if Sala.LETRAS[i] == letra:
                indice = i
        return indice

    def es_silla_valida(self, letra, numero):
        """Garantiza: retorna True si la sala tiene la silla letra-numero."""
        return self.indice_fila(letra) != -1 and 1 <= numero <= self.__sillas_por_fila

    def get_silla(self, letra, numero):
        """
        Supone:
            es_silla_valida(letra, numero) es True.
        Garantiza:
            Retorna el objeto Silla de esa fila y ese numero.
        """
        return self.__sillas[self.indice_fila(letra)][numero - 1]

    def vender(self, letra, numero):
        """
        Garantiza:
            Si la silla existe y esta libre, la ocupa, cuenta la venta y
            retorna True. Si no, no cambia nada y retorna False.
        """
        vendida = False
        if self.es_silla_valida(letra, numero):
            if self.get_silla(letra, numero).ocupar():
                self.__vendidas = self.__vendidas + 1
                vendida = True
        return vendida

    def liberar(self, letra, numero):
        """
        Garantiza:
            Si la silla existe y esta ocupada, la libera, descuenta la
            venta y retorna True. Si no, no cambia nada y retorna False.
        """
        liberada = False
        if self.es_silla_valida(letra, numero):
            if self.get_silla(letra, numero).liberar():
                self.__vendidas = self.__vendidas - 1
                liberada = True
        return liberada

    def contar_libres_fila(self, letra):
        """
        Supone:
            la sala tiene una fila con esa letra.
        Garantiza:
            Retorna cuantas sillas libres tiene esa fila.
        """
        i = self.indice_fila(letra)
        libres = 0
        for j in range(self.__sillas_por_fila):
            if self.__sillas[i][j].esta_libre():
                libres = libres + 1
        return libres

    def contar_libres(self):
        """Garantiza: retorna cuantas sillas libres tiene toda la sala."""
        libres = 0
        for i in range(self.__filas):
            libres = libres + self.contar_libres_fila(Sala.LETRAS[i])
        return libres

    def get_recaudo(self):
        """Garantiza: retorna el dinero de las boletas vendidas."""
        return self.__vendidas * self.__precio

    def __str__(self):
        texto = "  "
        for j in range(self.__sillas_por_fila):
            texto = texto + f" {j + 1}"
        for i in range(self.__filas):
            texto = texto + "\n" + Sala.LETRAS[i] + " "
            for j in range(self.__sillas_por_fila):
                texto = texto + " " + str(self.__sillas[i][j])
        return texto
