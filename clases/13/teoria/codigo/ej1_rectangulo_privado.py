"""Ejemplo 1 mejorado: Rectangulo con atributos privados, getters y setters (diapositivas 32-34)."""


class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def set_base(self, base):
        cambiada = False
        if base > 0:
            self.__base = base
            cambiada = True
        return cambiada

    def set_altura(self, altura):
        cambiada = False
        if altura > 0:
            self.__altura = altura
            cambiada = True
        return cambiada

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return 2 * self.__base + 2 * self.__altura


# Diapositiva 34: típico (5.0), límite (0.0) y especial (-5.0)
r1 = Rectangulo(3.0, 4.0)
assert r1.set_base(5.0) == True
assert r1.calcular_area() == 20.0
assert r1.set_base(0.0) == False
assert r1.set_base(-5.0) == False
assert r1.get_base() == 5.0
print("Rectangulo: todas las pruebas pasaron")

# Observación de la diapositiva 34: __ cambia el nombre, no es un candado
r2 = Rectangulo(3.0, 4.0)
r2.__base = -5.0                 # no da error: crea OTRO atributo
print(r2.get_base())             # 3.0
print(r2.calcular_area())        # 12.0
print(r2.__base)                 # -5.0
print(r2._Rectangulo__base)      # 3.0: el nombre real
