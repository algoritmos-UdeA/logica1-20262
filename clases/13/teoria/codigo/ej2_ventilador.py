"""Ejemplo 2: Ventilador (diapositivas 35-39). Constantes de clase, valores por defecto, __str__."""


class Ventilador:
    LENTO = 1
    MEDIO = 2
    RAPIDO = 3

    def __init__(self, velocidad=1, radio=5.0, color="azul", encendido=False):
        self.__velocidad = velocidad
        self.__radio = radio
        self.__color = color
        self.__encendido = encendido

    def get_velocidad(self):
        return self.__velocidad

    def get_radio(self):
        return self.__radio

    def get_color(self):
        return self.__color

    def esta_encendido(self):
        return self.__encendido

    def set_velocidad(self, velocidad):
        cambiada = False
        if (velocidad >= Ventilador.LENTO and
                velocidad <= Ventilador.RAPIDO):
            self.__velocidad = velocidad
            cambiada = True
        return cambiada

    def set_color(self, color):
        self.__color = color

    def encender(self):
        self.__encendido = True

    def apagar(self):
        self.__encendido = False

    def __str__(self):
        estado = "apagado"
        if self.__encendido:
            estado = "encendido"
        return ("Ventilador " + self.__color
                + ", radio " + str(self.__radio)
                + ", velocidad " + str(self.__velocidad)
                + ", " + estado)


# Diapositiva 37
v1 = Ventilador(Ventilador.RAPIDO, 10.0, "amarillo", True)
v2 = Ventilador()
print(v1.get_velocidad(), v1.get_radio(), v1.get_color(), v1.esta_encendido())
print(v2.get_velocidad(), v2.get_radio(), v2.get_color(), v2.esta_encendido())

# Diapositiva 38
v3 = Ventilador()
print(v3)
v3.set_velocidad(Ventilador.MEDIO)
print(v3.encender())             # None: encender no devuelve nada
print(v3)

# Diapositiva 39
v4 = Ventilador()
assert v4.set_velocidad(4) == False
assert v4.set_velocidad(Ventilador.RAPIDO) == True
assert str(v4) == "Ventilador azul, radio 5.0, velocidad 3, apagado"
print("Ventilador: todas las pruebas pasaron")
