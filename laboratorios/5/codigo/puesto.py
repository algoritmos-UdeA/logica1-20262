"""
Laboratorio 5 - Parqueadero: la clase Puesto.

Un puesto sabe en qué piso está, qué número tiene y qué vehículo lo
ocupa. Cuando está libre, su vehículo es None.

El puesto conoce a su vehículo, pero no lo crea: lo recibe ya creado en
ocupar (asociación: Puesto ──> Vehiculo). Por eso este archivo no importa
vehiculo.py.

ARCHIVO POR COMPLETAR. La estructura de la clase y la documentación de
cada método ya están escritas. Hay que reemplazar cada "pass" por el
código que cumple lo que dice la documentación (Supone / Garantiza).
No cambie los nombres de los métodos ni sus parámetros: las pruebas y
el programa principal los usan tal como están.

Autor(es): Nombre Apellido, Nombre Apellido
Fecha: dd/mm/aaaa
"""


class Puesto:
    def __init__(self, piso, numero):
        """
        Supone: piso >= 1 y numero >= 1.
        Garantiza: crea un puesto LIBRE, con ese piso y ese número. Guarda
        tres atributos privados: piso, numero y vehiculo (que empieza en
        None).
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_piso(self):
        """Garantiza: retorna el piso donde está el puesto."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_numero(self):
        """Garantiza: retorna el número del puesto dentro de su piso."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_vehiculo(self):
        """
        Garantiza: retorna el vehículo que ocupa el puesto, o None si el
        puesto está libre.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def esta_libre(self):
        """Garantiza: retorna True si el puesto no tiene vehículo, y False si lo tiene."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def ocupar(self, vehiculo):
        """
        Supone: vehiculo es un objeto Vehiculo.
        Garantiza: si el puesto está libre, guarda el vehículo y retorna
        True. Si ya está ocupado, no cambia nada y retorna False.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def liberar(self):
        """
        Garantiza: el puesto queda libre. Retorna el vehículo que lo
        ocupaba, o None si ya estaba libre.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def __str__(self):
        """
        Garantiza: retorna dónde está el puesto y quién lo ocupa. Por
        ejemplo: "Piso 1, puesto 3: ABC123 (carro)" o, si está libre,
        "Piso 1, puesto 3: libre".
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass
