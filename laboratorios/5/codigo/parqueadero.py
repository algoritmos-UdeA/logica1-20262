"""
Laboratorio 5 - Parqueadero: la clase Parqueadero.

El parqueadero guarda sus puestos en una MATRIZ: cada fila es un piso y
cada columna es un puesto de ese piso.

- El parqueadero crea sus puestos en el constructor y crea un recibo cada
  vez que sale un vehículo (composición: Parqueadero ◆── Puesto,
  Parqueadero ◆── Recibo). Por eso este archivo importa puesto.py y
  recibo.py.
- Los vehículos llegan ya creados a ingresar_vehiculo; el parqueadero se
  los entrega a un puesto. Por eso este archivo no importa vehiculo.py.

CUIDADO CON LOS NÚMEROS. Para el usuario, los pisos y los puestos se
cuentan desde 1. En la matriz, las filas y las columnas se cuentan desde
0. El puesto del piso 1, número 1, está en la fila 0, columna 0.

ARCHIVO POR COMPLETAR. La estructura de la clase y la documentación de
cada método ya están escritas. Hay que reemplazar cada "pass" por el
código que cumple lo que dice la documentación (Supone / Garantiza).
No cambie los nombres de los métodos ni sus parámetros: las pruebas y
el programa principal los usan tal como están.

Autor(es): Nombre Apellido, Nombre Apellido
Fecha: dd/mm/aaaa
"""
from puesto import Puesto
from recibo import Recibo


class Parqueadero:
    def __init__(self, pisos, puestos_por_piso):
        """
        Supone: pisos >= 1 y puestos_por_piso >= 1.
        Garantiza: crea un parqueadero con todos sus puestos libres y un
        recaudo de 0. Guarda cuatro atributos privados: pisos,
        puestos_por_piso, recaudo y puestos.

        puestos es una matriz de objetos Puesto, con una fila por piso y
        una columna por puesto. En la fila i, columna j, va el puesto del
        piso i + 1 y número j + 1: Puesto(i + 1, j + 1).
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_pisos(self):
        """Garantiza: retorna cuántos pisos tiene el parqueadero."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_puestos_por_piso(self):
        """Garantiza: retorna cuántos puestos tiene cada piso."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_recaudo(self):
        """Garantiza: retorna el dinero recaudado hasta ahora."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def get_puesto(self, piso, numero):
        """
        Supone: 1 <= piso <= pisos y 1 <= numero <= puestos_por_piso
        (los números que usa el usuario, que empiezan en 1).
        Garantiza: retorna el objeto Puesto de ese piso y ese número. En
        la matriz está en la fila piso - 1, columna numero - 1.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def contar_libres(self):
        """Garantiza: retorna cuántos puestos están libres en todo el parqueadero."""
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def buscar_puesto_libre(self):
        """
        Garantiza: retorna el PRIMER puesto libre, o None si el
        parqueadero está lleno. Se busca en orden: primero todo el piso 1
        (puestos 1, 2, 3...), después todo el piso 2, y así sucesivamente.
        No modifica nada.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def buscar_vehiculo(self, placa):
        """
        Garantiza: retorna el puesto ocupado por el vehículo que tiene
        esa placa, o None si no hay ningún vehículo con esa placa. No
        modifica nada.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def ingresar_vehiculo(self, vehiculo):
        """
        Supone: vehiculo es un objeto Vehiculo.
        Garantiza: si no hay otro vehículo con la misma placa y hay algún
        puesto libre, el vehículo ocupa el primer puesto libre y se
        retorna ese puesto. Si no, no cambia nada y retorna None.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass

    def retirar_vehiculo(self, placa, minutos):
        """
        Supone: minutos es un entero >= 0.
        Garantiza: si hay un vehículo con esa placa, libera su puesto,
        crea el recibo con ese vehículo y esos minutos, suma el valor del
        recibo al recaudo y retorna el recibo. Si no hay ningún vehículo
        con esa placa, no cambia nada y retorna None.
        """
        # COMPLETE: reemplace el pass por el código de este método
        pass
