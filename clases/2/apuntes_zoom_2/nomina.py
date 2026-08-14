# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:17:37 2026

- author: Usuario
- Resumen: Este programa calcula la nomina e imprime de un empleado
"""


# Inicializacion
TASA_SALUD = 0.10
TASA_PENSION = 0.05

# Entrada de datos
nombre = input("Ingrese el nombre del trabajador: ")
id = input("Ingrese el documento del empleado: ")
num_horas = float(input("Ingrese el numero de horas que trabajo el empleado: "))
val_hora = float(input("Ingrese valor de cada hora: "))

# Proceso
salario_base = num_horas * val_hora
imp_salud = salario_base * TASA_SALUD
imp_pesion = salario_base * TASA_PENSION
salario_neto = salario_base - imp_salud - imp_pesion

# Salida de datos
print("*******************************************************************************")
print("***** RECIBO DE PAGO *****")
print("- Salario base: ",salario_base)
print("- Impuesto de transporte: ",imp_pesion)
print("- Impuesto de salud: ",imp_salud)
print("-------------------------------------")
print("Salario neto: ",salario_neto)
print("=======================================================")
print("Paguese a ",nombre, "identificado con CC: ", id, "la suma de $", salario_neto)
print("Identificado con id: ",id)
print("*******************************************************************************")