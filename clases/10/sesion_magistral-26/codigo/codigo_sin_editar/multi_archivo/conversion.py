

def celsius_a_fahrenheit(temp_c):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Supone:
        temp_c es un numero (int o float) mayor o igual a -273.15.
    Garantiza:
        Retorna la temperatura equivalente en grados Fahrenheit (float).
    """
    temp_f = (9/5)*temp_c + 32
    return temp_f


def celsius_a_kelvin(temp_c):
    """
    Convierte una temperatura de grados Celsius a Kelvin.

    Supone:
        temp_c es un numero (int o float) mayor o igual a -273.15.
    Garantiza:
        Retorna la temperatura equivalente en Kelvin (float), mayor o igual a 0.
    """
    temp_k = temp_c + 273.15
    return temp_k

def kelvin_a_celsius(temp_k):
    """
    Especificacion de la funcion

    Supone:

    Garantiza:

    """
    return temp_k - 273.15 