"""Ejemplo 1: Rectangulo con atributos públicos (diapositivas 26-31)."""


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura


# Diapositiva 30: dos objetos, identidad y pruebas
r1 = Rectangulo(3.0, 4.0)
r2 = Rectangulo(5.0, 2.0)
assert r1.calcular_area() == 12.0
assert r2.calcular_area() == 10.0
assert r1.calcular_perimetro() == 14.0
assert r2.calcular_perimetro() == 14.0

r3 = Rectangulo(3.0, 4.0)
print(r1 is r3)
print("Rectangulo: todas las pruebas pasaron")

# Diapositiva 31: el problema de los atributos públicos
r1.base = -5.0
print(r1.calcular_area())        # -20.0: nadie revisó el valor
print(r1.calcular_perimetro())   # -2.0
