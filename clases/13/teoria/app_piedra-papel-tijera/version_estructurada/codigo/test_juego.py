"""Pruebas de juego.py. Se ejecutan con: python test_juego.py"""
from reglas import PIEDRA, PAPEL, TIJERA, EMPATE, GANA_USUARIO, GANA_MAQUINA
from juego import (sumar_si_gana, partida_terminada, nombre_ganador,
                   texto_ronda, texto_marcador)

# sumar_si_gana
assert sumar_si_gana(2, GANA_USUARIO, GANA_USUARIO) == 3     # gana: suma
assert sumar_si_gana(2, GANA_MAQUINA, GANA_USUARIO) == 2     # pierde: no suma
assert sumar_si_gana(2, EMPATE, GANA_USUARIO) == 2           # empate: no suma
assert sumar_si_gana(0, GANA_MAQUINA, GANA_MAQUINA) == 1     # límite: desde 0

# partida_terminada (a 3 rondas)
assert partida_terminada(0, 0, 3) == False      # recién empieza
assert partida_terminada(2, 2, 3) == False      # a una ronda de terminar
assert partida_terminada(3, 1, 3) == True       # ganó el usuario
assert partida_terminada(0, 3, 3) == True       # ganó la máquina

# nombre_ganador
assert nombre_ganador("Ana", 3, "Máquina", 1) == "Ana"
assert nombre_ganador("Ana", 2, "Máquina", 3) == "Máquina"

# texto_ronda
assert (texto_ronda("Ana", PIEDRA, "Máquina", TIJERA, GANA_USUARIO)
        == "Ana: piedra | Máquina: tijera | gana Ana")
assert (texto_ronda("Ana", PIEDRA, "Máquina", PAPEL, GANA_MAQUINA)
        == "Ana: piedra | Máquina: papel | gana Máquina")
assert (texto_ronda("Ana", TIJERA, "Máquina", TIJERA, EMPATE)
        == "Ana: tijera | Máquina: tijera | empate")

# texto_marcador
assert texto_marcador("Ana", 2, "Máquina", 1) == "Ana 2 - 1 Máquina"
assert texto_marcador("Ana", 0, "Máquina", 0) == "Ana 0 - 0 Máquina"

print("Pruebas de juego: todas pasaron")
