# -*- coding: utf-8 -*-
"""
Pruebas del modulo cai, nivel 1.

Autor(es): Nombre Apellido, Nombre Apellido
Fecha: dd/mm/aaaa
Version: 1
"""
# PISTA: este archivo necesita dos import:
#   - el modulo cai, para llamar sus funciones;
#   - random, porque la prueba de generar_operando usa random.seed().


############ Pruebas ##############
# PISTA: es_correcta. Escriba un assert por cada fila de la tabla
# "Casos de prueba de es_correcta" del enunciado. Cada llamada lleva el
# prefijo cai.
#     assert cai.es_correcta(42, 42) == True
#
# PISTA: generar_operando. Fije la semilla con random.seed() y un numero
# cualquiera, y verifique en un ciclo que 1000 valores generados esten
# entre 1 y 9. La estructura es:
#     random.seed(...)
#     for i in range(1000):
#         numero = cai.generar_operando()
#         assert ...      # complete: numero debe estar entre 1 y 9
# Si algun valor queda fuera del rango, el assert falla en esa vuelta.
#
# PISTA: mostrar_pregunta imprime y no retorna nada: no se prueba con assert.
#
# PISTA: este archivo no lleva guarda: nadie lo importa, solo se ejecuta
# directamente con python test_cai.py. Al final agregue:
#     print("Pruebas de cai: todas pasaron")
