# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:31:18 2026

@author: Soportedrai
"""

# Constantes
HORA_BASE = 35
EXTRA = 1.5

# Inicializacion
sal_base = 0
hr_extra = 0
resto = 0
imp = 0

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
if sal_base <= 300000:
    imp = 0
else:
    if sal_base <= 450000:
        resto = sal_base - 300000
        imp = 0.2*resto
    else:
        resto = sal_base - 450000
        imp = 0.2*150000 + 0.3*resto

# Calculo del salario neto
sal_neto = sal_base - imp
# print(sal_base,imp,sal_neto)
print("----------------------------------")
print("        RECIBO DE PAGO ")
print(f"Empleado: {nom}")
print(f"- Salario base: $ {sal_base}")
print(f"- impuestos: $ {imp}")
print(f"- Salario neto: $ {sal_neto}")
print("----------------------------------")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    


    