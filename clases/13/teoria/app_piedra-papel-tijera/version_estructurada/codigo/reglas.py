"""
Piedra, papel o tijera: las reglas del juego.

Este archivo es igual en la versión estructurada y en la versión POO.
Las reglas no guardan datos: reciben jugadas y retornan resultados, así
que se escriben como funciones en los dos paradigmas.
"""
import random

# Jugadas
PIEDRA = 1
PAPEL = 2
TIJERA = 3

# Resultados de una ronda
EMPATE = 0
GANA_USUARIO = 1
GANA_MAQUINA = 2


def es_jugada_valida(jugada):
    """
    Supone: jugada es un entero.
    Garantiza: retorna True si jugada es PIEDRA, PAPEL o TIJERA, y False
    si no.
    """
    return PIEDRA <= jugada <= TIJERA


def nombre_jugada(jugada):
    """
    Supone: jugada es PIEDRA, PAPEL o TIJERA.
    Garantiza: retorna "piedra", "papel" o "tijera".
    """
    if jugada == PIEDRA:
        nombre = "piedra"
    elif jugada == PAPEL:
        nombre = "papel"
    else:
        nombre = "tijera"
    return nombre


def definir_ganador(jugada_usuario, jugada_maquina):
    """
    Decide quién gana una ronda: piedra le gana a tijera, tijera le gana
    a papel y papel le gana a piedra.

    Supone: las dos jugadas son PIEDRA, PAPEL o TIJERA.
    Garantiza: retorna EMPATE, GANA_USUARIO o GANA_MAQUINA.
    """
    if jugada_usuario == jugada_maquina:
        resultado = EMPATE
    elif ((jugada_usuario == PIEDRA and jugada_maquina == TIJERA)
          or (jugada_usuario == TIJERA and jugada_maquina == PAPEL)
          or (jugada_usuario == PAPEL and jugada_maquina == PIEDRA)):
        resultado = GANA_USUARIO
    else:
        resultado = GANA_MAQUINA
    return resultado


def jugar_maquina():
    """Garantiza: retorna una jugada al azar: PIEDRA, PAPEL o TIJERA."""
    return random.randint(PIEDRA, TIJERA)
