"""Pruebas de reglas.py. Se ejecutan con: python test_reglas.py"""
from reglas import (PIEDRA, PAPEL, TIJERA, EMPATE, GANA_USUARIO, GANA_MAQUINA,
                    es_jugada_valida, nombre_jugada, definir_ganador,
                    jugar_maquina)

# es_jugada_valida
assert es_jugada_valida(PIEDRA) == True         # límite inferior
assert es_jugada_valida(TIJERA) == True         # límite superior
assert es_jugada_valida(0) == False             # fuera del rango
assert es_jugada_valida(4) == False             # fuera del rango

# nombre_jugada
assert nombre_jugada(PIEDRA) == "piedra"
assert nombre_jugada(PAPEL) == "papel"
assert nombre_jugada(TIJERA) == "tijera"

# definir_ganador: los 9 casos posibles
assert definir_ganador(PIEDRA, PIEDRA) == EMPATE
assert definir_ganador(PAPEL, PAPEL) == EMPATE
assert definir_ganador(TIJERA, TIJERA) == EMPATE
assert definir_ganador(PIEDRA, TIJERA) == GANA_USUARIO
assert definir_ganador(TIJERA, PAPEL) == GANA_USUARIO
assert definir_ganador(PAPEL, PIEDRA) == GANA_USUARIO
assert definir_ganador(TIJERA, PIEDRA) == GANA_MAQUINA
assert definir_ganador(PAPEL, TIJERA) == GANA_MAQUINA
assert definir_ganador(PIEDRA, PAPEL) == GANA_MAQUINA

# jugar_maquina: el resultado es al azar, se prueba el rango
for i in range(1000):
    assert es_jugada_valida(jugar_maquina())

print("Pruebas de reglas: todas pasaron")
