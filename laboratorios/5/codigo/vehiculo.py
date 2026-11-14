"""
Laboratorio 5 - Parqueadero: la clase Vehiculo.

Un vehículo tiene una placa y un tipo (carro o moto). Es la clase más
sencilla del laboratorio: no conoce a ninguna otra, y por eso es la
primera que se completa y se prueba.

ARCHIVO POR COMPLETAR. La estructura de la clase y la documentación de
cada método ya están escritas. Hay que reemplazar cada "pass" por el
código que cumple lo que dice la documentación (Supone / Garantiza).
No cambie los nombres de los métodos ni sus parámetros: las pruebas y
el programa principal los usan tal como están.

Autor(es): Nombre Apellido, Nombre Apellido
Fecha: dd/mm/aaaa
"""


class Vehiculo:
    CARRO = "carro"
    MOTO = "moto"

    def __init__(self, placa, tipo):
        """
        Supone: placa es un texto; tipo es Vehiculo.CARRO o Vehiculo.MOTO.
        Garantiza: crea un vehículo con esa placa y ese tipo, guardados en
        los atributos privados placa y tipo.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_placa(self):
        """Garantiza: retorna la placa del vehículo."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_tipo(self):
        """Garantiza: retorna el tipo del vehículo: "carro" o "moto"."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def __str__(self):
        """
        Garantiza: retorna la placa y, entre paréntesis, el tipo. Por
        ejemplo: "ABC123 (carro)".
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass
