# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 4: modulo funciones del juego piedra, papel o tijera.

Lo importan main_juego.py y test_funciones.py.
definir_ganador todavia es un stub: completarla es la actividad de la sesion.
"""
import random

############ Constantes ############
PIEDRA = 1
PAPEL = 2
TIJERA = 3


############ Funciones ############
def mostrar_menu():
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")


def obtener_nombre_jugada(eleccion):
    """
    Traduce el numero de una jugada a su nombre.

    Supone:
        eleccion es un entero.
    Garantiza:
        Retorna "piedra", "papel" o "tijera" si eleccion es 1, 2 o 3,
        y "Incorrecto" para cualquier otro valor.
    """
    if eleccion == PIEDRA:
        return "piedra"
    elif eleccion == PAPEL:
        return "papel"
    elif eleccion == TIJERA:
        return "tijera"
    else:
        return "Incorrecto"


def jugar_maquina():
    """
    Elige al azar la jugada de la maquina.

    Supone:
        Nada: no recibe datos.
    Garantiza:
        Retorna un entero al azar entre 1 y 3 (PIEDRA, PAPEL o TIJERA).
    """
    return random.randint(PIEDRA, TIJERA)


def lanzar_dado():
    """
    Simula el lanzamiento de un dado de seis caras.

    Supone:
        Nada: no recibe datos.
    Garantiza:
        Retorna un entero al azar entre 1 y 6.
    """
    return random.randint(1, 6)


def definir_ganador(jugada_usuario, jugada_maquina):
    """
    Decide quien gana una ronda de piedra, papel o tijera.

    Supone:
        jugada_usuario y jugada_maquina son 1 (PIEDRA), 2 (PAPEL) o 3 (TIJERA).
    Garantiza:
        Retorna 0 si gana el usuario, 1 si gana la maquina y 2 si hay empate.
    """
    # PENDIENTE: implementar (actividad)
    return 0
