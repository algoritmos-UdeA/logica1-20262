# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 4: pruebas del modulo funciones.

Mientras definir_ganador sea un stub, sus pruebas fallan:
las pruebas dicen que falta por hacer.
"""
import funciones

############ Test ################

# obtener_nombre_jugada
assert funciones.obtener_nombre_jugada(1) == "piedra"           # tipico
assert funciones.obtener_nombre_jugada(2) == "papel"            # tipico
assert funciones.obtener_nombre_jugada(3) == "tijera"           # tipico
assert funciones.obtener_nombre_jugada(4) == "Incorrecto"       # especial (fuera del rango)

# jugar_maquina y lanzar_dado: resultados al azar, se prueba el rango
for i in range(1000):
    assert 1 <= funciones.jugar_maquina() <= 3
    assert 1 <= funciones.lanzar_dado() <= 6

# definir_ganador
assert funciones.definir_ganador(1, 3) == 0, "ERROR: piedra le gana a tijera, gana el usuario"
assert funciones.definir_ganador(1, 1) == 2, "ERROR: piedra contra piedra es empate"
# ACTIVIDAD: escriba aqui los demas casos de prueba de definir_ganador

print("Pruebas de funciones: todas pasaron")
