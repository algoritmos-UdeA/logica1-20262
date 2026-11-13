"""
Aplicación de transporte: la clase Viaje.

Un viaje relaciona a un cliente con un conductor. Los dos llegan ya
creados al constructor, y el viaje solo los conoce (asociación:
Viaje ──> Cliente, Viaje ──> Conductor). Por eso este archivo no
importa cliente.py ni conductor.py.

El origen y el destino, en cambio, son objetos Punto que el viaje crea
(composición: Viaje ◆── Punto), y por eso sí importa punto.py.
"""
from punto import Punto


class Viaje:
    TARIFA_BASE = 4000
    VALOR_POR_KM = 1500

    def __init__(self, cliente, conductor, x_destino, y_destino):
        """
        Supone: cliente es un objeto Cliente y conductor es un objeto
        Conductor que está disponible.
        Garantiza: crea un viaje sin finalizar, desde la posición actual
        del cliente hasta (x_destino, y_destino), y ocupa al conductor.
        """
        self.__cliente = cliente
        self.__conductor = conductor
        posicion = cliente.get_posicion()
        self.__origen = Punto(posicion.get_x(), posicion.get_y())
        self.__destino = Punto(x_destino, y_destino)
        self.__finalizado = False
        conductor.ocupar()

    def get_cliente(self):
        return self.__cliente

    def get_conductor(self):
        return self.__conductor

    def get_origen(self):
        return self.__origen

    def get_destino(self):
        return self.__destino

    def esta_finalizado(self):
        return self.__finalizado

    def calcular_distancia(self):
        """Garantiza: retorna los kilómetros entre el origen y el destino."""
        return self.__origen.calcular_distancia(self.__destino)

    def calcular_valor(self):
        """
        Garantiza: retorna el valor del viaje, que es la tarifa base más
        el valor por kilómetro multiplicado por la distancia.
        """
        return Viaje.TARIFA_BASE + Viaje.VALOR_POR_KM * self.calcular_distancia()

    def finalizar(self):
        """
        Supone: el viaje no ha finalizado.
        Garantiza: el cliente y el conductor quedan en el destino, el
        conductor vuelve a estar disponible y el viaje queda finalizado.
        """
        x = self.__destino.get_x()
        y = self.__destino.get_y()
        self.__cliente.set_posicion(x, y)
        self.__conductor.set_posicion(x, y)
        self.__conductor.liberar()
        self.__finalizado = True

    def __str__(self):
        estado = "en curso"
        if self.__finalizado:
            estado = "finalizado"
        return (f"{self.__cliente.get_nombre()} con "
                f"{self.__conductor.get_nombre()}: "
                f"{self.__origen} -> {self.__destino} | "
                f"{self.calcular_distancia():.2f} km | "
                f"${self.calcular_valor():.0f} | {estado}")
