# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:44:41 2026

@author: Soportedrai
"""

""" Forma 1
# Inicializacion
e = 0

# num = int(input("Ingrese el numero: "))
num = 7
for i in range(num,0,-1):
    # print(f"{i} -- {e}")
    print(((-1)**e)*i)
    e += 1
    
"""
signo_pos = True

# num = 7
num = int(input("Ingrese el numero: "))
for i in range(num,0,-1):
    # print(f"{i} -- {signo_pos}")
    if signo_pos:
        print(i)
    else:
        print(-i)
    signo_pos = not(signo_pos)
        


