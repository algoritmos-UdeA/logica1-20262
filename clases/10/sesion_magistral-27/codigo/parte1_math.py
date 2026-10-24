# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 1: el modulo math y la especificacion de math.sin.

La especificacion de math.sin dice que el angulo se mide en radianes.
Si se le entregan grados, no hay error, pero el resultado no tiene sentido.
"""
import math

# Sin leer la especificacion: 90 se interpreta como 90 radianes
print(f"math.sin(90) = {math.sin(90)}")

# Leyendo la especificacion: primero se convierte de grados a radianes
x = 90
x_rad = math.radians(x)
y = math.sin(x_rad)
print(f"math.sin(math.radians(90)) = {y}")

# Lo mismo en una sola linea: una funcion invocada dentro de otra
y = math.sin(math.radians(x))
print(f"y = {y}")

# La constante pi del modulo math: pi/2 radianes son 90 grados
print(f"math.pi = {math.pi}")
z = math.sin(math.pi / 2)
print(f"z = {z}")
