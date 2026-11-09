"""Ejemplo 3: Celular, "Hágalo usted mismo" (diapositivas 40-41). Setters sin validar (diseño por contrato)."""


class Celular:
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_precio(self):
        return self.__precio

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_precio(self, precio):
        self.__precio = precio

    # Reto (solución en la diapositiva 41): en el UML pasa a ser
    # + set_precio(precio: float) : bool
    # def set_precio(self, precio):
    #     cambiado = False
    #     if precio > 0:
    #         self.__precio = precio
    #         cambiado = True
    #     return cambiado


c1 = Celular("Xiaomi", "Redmi 13", 650000.0)
assert c1.get_marca() == "Xiaomi"
assert c1.get_precio() == 650000.0
c1.set_precio(599000.0)
assert c1.get_precio() == 599000.0
print("Celular: todas las pruebas pasaron")
