"""
Aplicación de transporte: la clase Plataforma.

La plataforma guarda tres listas: los clientes, los conductores y los
viajes.

- Los clientes y los conductores llegan ya creados a registrar_cliente y
  registrar_conductor (agregación: Plataforma ◇── Cliente,
  Plataforma ◇── Conductor). Por eso este archivo no importa cliente.py
  ni conductor.py.
- Los viajes los crea la plataforma en solicitar_viaje (composición:
  Plataforma ◆── Viaje), y por eso sí importa viaje.py.
"""
from viaje import Viaje


class Plataforma:
    def __init__(self):
        """Garantiza: crea una plataforma sin clientes, conductores ni viajes."""
        self.__clientes = []
        self.__conductores = []
        self.__viajes = []

    def registrar_cliente(self, cliente):
        """
        Supone: cliente es un objeto Cliente y su cédula no está registrada.
        Garantiza: el cliente queda al final de la lista de clientes.
        """
        self.__clientes.append(cliente)

    def registrar_conductor(self, conductor):
        """
        Supone: conductor es un objeto Conductor y su cédula no está
        registrada.
        Garantiza: el conductor queda al final de la lista de conductores.
        """
        self.__conductores.append(conductor)

    def buscar_cliente(self, cedula):
        """
        Garantiza: retorna el cliente con esa cédula, o None si no está
        registrado.
        """
        encontrado = None
        for cliente in self.__clientes:
            if cliente.get_cedula() == cedula:
                encontrado = cliente
                break
        return encontrado

    def buscar_conductor(self, cedula):
        """
        Garantiza: retorna el conductor con esa cédula, o None si no está
        registrado.
        """
        encontrado = None
        for conductor in self.__conductores:
            if conductor.get_cedula() == cedula:
                encontrado = conductor
                break
        return encontrado

    def conductor_mas_cercano(self, punto):
        """
        Supone: punto es un objeto Punto.
        Garantiza: retorna el conductor disponible que está a menor
        distancia del punto, o None si no hay ninguno disponible. Si dos
        están a la misma distancia, retorna el que se registró primero.
        """
        mas_cercano = None
        menor_distancia = 0.0
        for conductor in self.__conductores:
            if conductor.esta_disponible():
                distancia = conductor.get_posicion().calcular_distancia(punto)
                if mas_cercano == None or distancia < menor_distancia:
                    mas_cercano = conductor
                    menor_distancia = distancia
        return mas_cercano

    def buscar_viaje_activo(self, cedula):
        """
        Garantiza: retorna el viaje sin finalizar del cliente con esa
        cédula, o None si no tiene.
        """
        encontrado = None
        for viaje in self.__viajes:
            if (not viaje.esta_finalizado()
                    and viaje.get_cliente().get_cedula() == cedula):
                encontrado = viaje
                break
        return encontrado

    def solicitar_viaje(self, cedula, x_destino, y_destino):
        """
        Garantiza: si el cliente está registrado, no tiene un viaje sin
        finalizar y hay un conductor disponible, crea el viaje con el
        conductor disponible más cercano al cliente, lo guarda y lo
        retorna. Si no, no cambia nada y retorna None.
        """
        viaje = None
        cliente = self.buscar_cliente(cedula)
        if cliente != None and self.buscar_viaje_activo(cedula) == None:
            conductor = self.conductor_mas_cercano(cliente.get_posicion())
            if conductor != None:
                viaje = Viaje(cliente, conductor, x_destino, y_destino)
                self.__viajes.append(viaje)
        return viaje

    def finalizar_viaje(self, cedula):
        """
        Garantiza: si el cliente con esa cédula tiene un viaje sin
        finalizar, lo finaliza y retorna True. Si no, no cambia nada y
        retorna False.
        """
        finalizado = False
        viaje = self.buscar_viaje_activo(cedula)
        if viaje != None:
            viaje.finalizar()
            finalizado = True
        return finalizado

    def mostrar_clientes(self):
        """Garantiza: imprime los clientes, uno por línea."""
        if len(self.__clientes) == 0:
            print("(no hay clientes)")
        for cliente in self.__clientes:
            print(cliente)

    def mostrar_conductores(self):
        """Garantiza: imprime los conductores, uno por línea."""
        if len(self.__conductores) == 0:
            print("(no hay conductores)")
        for conductor in self.__conductores:
            print(conductor)

    def mostrar_viajes(self):
        """Garantiza: imprime los viajes, uno por línea."""
        if len(self.__viajes) == 0:
            print("(no hay viajes)")
        for viaje in self.__viajes:
            print(viaje)
