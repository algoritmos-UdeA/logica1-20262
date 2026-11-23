"""
Clase 15 - Sala de cine con archivo: la clase Sala.

Es la Sala de la clase 14 con dos metodos nuevos, guardar y cargar, y una
funcion del modulo, cargar_sala, que crea una Sala a partir de un archivo.
Asi, al cerrar el programa, las ventas no se pierden.

Formato del archivo (texto):
    primera linea: filas,sillas_por_fila,precio      por ejemplo 5,6,5000
    una linea por fila de la sala, con X (ocupada) u O (libre) por silla
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

    def guardar(self, nombre_archivo):
        """
        Garantiza:
            CREA el archivo (o lo REEMPLAZA) con el tamano y el precio en
            la primera linea y una linea por fila de la sala, con el texto
            de cada silla (X u O). No modifica la sala. No retorna nada.
        """
        archivo = open(nombre_archivo, "w")
        archivo.write(f"{self.__filas},{self.__sillas_por_fila},{self.__precio}\n")
        for i in range(self.__filas):
            for j in range(self.__sillas_por_fila):
                archivo.write(str(self.__sillas[i][j]))
            archivo.write("\n")
        archivo.close()

    def cargar(self, nombre_archivo):
        """
        Supone:
            el archivo existe, tiene el formato del modulo y el mismo tamano
            de esta sala.
        Garantiza:
            MODIFICA la sala: cada silla queda ocupada si en el archivo hay
            una X y libre si hay una O, y las ventas quedan contadas. No
            retorna nada.
        """
        archivo = open(nombre_archivo, "r")
        archivo.readline()                    # el tamano: ya lo conoce la sala
        self.__vendidas = 0
        for i in range(self.__filas):
            linea = archivo.readline().strip()
            for j in range(self.__sillas_por_fila):
                if linea[j] == "X":
                    self.__sillas[i][j].ocupar()
                    self.__vendidas = self.__vendidas + 1
                else:
                    self.__sillas[i][j].liberar()
        archivo.close()

    def __str__(self):
        texto = "  "
        for j in range(self.__sillas_por_fila):
            texto = texto + f" {j + 1}"
        for i in range(self.__filas):
            texto = texto + "\n" + Sala.LETRAS[i] + " "
            for j in range(self.__sillas_por_fila):
                texto = texto + " " + str(self.__sillas[i][j])
        return texto


def cargar_sala(nombre_archivo):
    """
    Supone:
        el archivo existe y tiene el formato del modulo.
    Garantiza:
        Retorna una Sala NUEVA con el tamano, el precio y las sillas
        ocupadas que dice el archivo.
    """
    archivo = open(nombre_archivo, "r")
    partes = archivo.readline().strip().split(",")
    archivo.close()
    sala = Sala(int(partes[0]), int(partes[1]), int(partes[2]))
    sala.cargar(nombre_archivo)
    return sala
