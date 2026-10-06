PI = 3.1416


def celsius_to_fahrenheit(c):
    return (9 / 5) * c + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def calcular_area_circulo(radio):
    return PI * radio ** 2


def calcular_area_rectangulo(base, altura):
    return base * altura


def mostrar_menu():
    print("--- Áreas de figuras ---")


def mostrar_area(figura, area):
    print(f"Área del {figura}: {area:.2f}")


# Invocaciones
mostrar_menu()                                               # 1. sin argumentos, sin guardar nada

temp_f = celsius_to_fahrenheit(25)                           # 2. se guarda el retorno (77.0)
print(celsius_to_fahrenheit(100))                            # 3. se usa directamente en print (212.0)
temp_c = fahrenheit_a_celsius(temp_f)                        # 4. el argumento es una variable (25.0)

area = calcular_area_circulo(5)                              # 5. un argumento (78.54)
mostrar_area("círculo", area)                                # 6. dos argumentos, sin guardar nada
mostrar_area("rectángulo", calcular_area_rectangulo(4, 3))   # 7. una llamada dentro de otra
