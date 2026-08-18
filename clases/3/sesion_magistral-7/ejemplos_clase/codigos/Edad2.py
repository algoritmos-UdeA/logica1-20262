# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 03:29:04 2026

@author: ANGELIE
"""

#Declarar variables
DIAS_ANNO=365
edad_annos=float
edad_dias=float

#Pedir datos
nombre=input("Ingrese su nombre: ")
edad_annos=float(input("Ingrese du edad (en años): "))

#Proceso
edad_dias=edad_annos*DIAS_ANNO

#Salida de datos
print (f"{nombre} tiene {edad_dias} días de edad")

