# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
# Constantes
HORA_BASE = 35
EXTRA = 1.5

nom = input("Nombre: ")
hr = int(input("Horas: "))
valor_hr = int(input("Valor hora: "))
# Calculo del salario base
if hr <= HORA_BASE:
    sal_base = valor_hr*hr
else:
    hr_extra = hr - HORA_BASE
    sal_base = valor_hr*HORA_BASE + EXTRA*valor_hr*hr_extra
# print(sal_base)
# Calculo de los impuestos



    