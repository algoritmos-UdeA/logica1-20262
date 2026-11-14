"""
Laboratorio 5 - Parqueadero: la clase Recibo.

Un recibo se entrega cuando un vehículo sale. Guarda el vehículo y los
minutos que estuvo, y con esos dos datos calcula cuántas horas se cobran
y cuánto vale.

El recibo conoce al vehículo, pero no lo crea: lo recibe ya creado
(asociación: Recibo ──> Vehiculo). Este archivo importa vehiculo.py solo
para usar las constantes Vehiculo.CARRO y Vehiculo.MOTO.

ARCHIVO POR COMPLETAR. La estructura de la clase y la documentación de
cada método ya están escritas. Hay que reemplazar cada "pass" por el
código que cumple lo que dice la documentación (Supone / Garantiza).
No cambie los nombres de los métodos ni sus parámetros: las pruebas y
el programa principal los usan tal como están.

Autor(es): Nombre Apellido, Nombre Apellido
Fecha: dd/mm/aaaa
"""
from vehiculo import Vehiculo


class Recibo:
    TARIFA_CARRO = 3000
    TARIFA_MOTO = 1000

    def __init__(self, vehiculo, minutos):
        """
        Supone: vehiculo es un objeto Vehiculo; minutos es un entero >= 0.
        Garantiza: crea un recibo con ese vehículo y esos minutos,
        guardados en los atributos privados vehiculo y minutos.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_vehiculo(self):
        """Garantiza: retorna el vehículo del recibo."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_minutos(self):
        """Garantiza: retorna los minutos que el vehículo estuvo en el parqueadero."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def calcular_horas(self):
        """
        Garantiza: retorna cuántas horas se cobran. Se cobra por hora o
        fracción: 60 minutos son 1 hora, pero 61 minutos ya son 2. Como
        mínimo se cobra 1 hora, aunque el vehículo haya estado 0 minutos.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def calcular_valor(self):
        """
        Garantiza: retorna el valor a pagar: las horas que se cobran
        multiplicadas por la tarifa del tipo de vehículo (TARIFA_CARRO o
        TARIFA_MOTO).
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def __str__(self):
        """
        Garantiza: retorna el recibo en una línea. Por ejemplo:
        "ABC123 (carro) | 130 min | 3 h | $9000".
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass
