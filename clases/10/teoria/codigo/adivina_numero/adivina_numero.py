# -*- coding: utf-8 -*-
"""
Juego: adivina el numero.

El programa elige un numero entero al azar entre 1 y 100. El usuario
intenta adivinarlo; despues de cada intento el programa indica si el
numero secreto es mayor o menor. Al acertar, muestra cuantos intentos
fueron necesarios.

Autor(es): Nombre Apellido
Fecha: dd/mm/aaaa
Version: 1
"""
import random

MINIMO = 1
MAXIMO = 100


############ Funciones ############
def generar_secreto(minimo, maximo):
    """
    Genera el numero secreto del juego.

    Supone:
        minimo y maximo son enteros, con minimo <= maximo.
    Garantiza:
        Retorna un entero al azar entre minimo y maximo (ambos incluidos).
    """
    return random.randint(minimo, maximo)


def evaluar_intento(intento, secreto):
    """
    Compara el intento del usuario con el numero secreto.

    Supone:
        intento y secreto son enteros.
    Garantiza:
        Retorna "mayor" si el secreto es mayor que el intento,
        "menor" si el secreto es menor, y "correcto" si son iguales.
    """
    if secreto > intento:
        return "mayor"
    elif secreto < intento:
        return "menor"
    else:
        return "correcto"


############ Pruebas ##############
# evaluar_intento
assert evaluar_intento(50, 74) == "mayor"
assert evaluar_intento(80, 74) == "menor"
assert evaluar_intento(74, 74) == "correcto"
# generar_secreto: si minimo == maximo, solo hay un resultado posible
assert generar_secreto(7, 7) == 7
# generar_secreto: con la misma semilla, el mismo numero
random.seed(10)
primero = generar_secreto(MINIMO, MAXIMO)
random.seed(10)
segundo = generar_secreto(MINIMO, MAXIMO)
assert primero == segundo
assert MINIMO <= primero <= MAXIMO

############ Programa principal #########
random.seed()   # semilla aleatoria para jugar de verdad
secreto = generar_secreto(MINIMO, MAXIMO)
print(f"Adivine el numero entre {MINIMO} y {MAXIMO}")

intentos = 0
resultado = ""
while resultado != "correcto":
    intento = int(input("Su intento: "))
    intentos = intentos + 1
    resultado = evaluar_intento(intento, secreto)
    if resultado == "mayor":
        print("El numero secreto es MAYOR")
    elif resultado == "menor":
        print("El numero secreto es MENOR")

print(f"¡Correcto! Lo adivino en {intentos} intentos")
