from funciones import calcular_area_circulo, calcular_area_rectangulo, calcular_area_triangulo

# Rectángulo
assert calcular_area_rectangulo(4, 3) == 12
assert calcular_area_rectangulo(0, 5) == 0

# Triángulo
assert calcular_area_triangulo(6, 2) == 6
assert calcular_area_triangulo(0, 5) == 0

# Círculo (con round por los decimales)
assert round(calcular_area_circulo(5), 2) == 78.54
assert calcular_area_circulo(0) == 0