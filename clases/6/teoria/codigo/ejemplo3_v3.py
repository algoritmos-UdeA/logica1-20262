"""
Ejemplo 3 - Solucion (forma 3: seguidilla de ifs independientes)

En el bachillerato de Springfield las calificaciones se suelen calcular
de acuerdo al siguiente cuadro:

    Grado numerico                              Grado en letra
    Grado mayor o igual a 90                    A
    Grado menor que 90 pero mayor o igual a 80   B
    Grado menor que 80 pero mayor o igual a 70   C
    Grado menor que 70 pero mayor o igual a 60   D
    Grado menor que 60                          E

Escribir un algoritmo que acepte una calificacion numerica del
estudiante [0,100], la convierta a su equivalente en letra y
visualice la calificacion correspondiente en letra.

Si el valor ingresado esta fuera del rango [0,100], se debe informar
un error en vez de asignar una nota en letra.

Datos de entrada:
    - Nota numerica

Datos de salida:
    - Nota en letra (A, B, C, D, E)

Definicion de variables:
    nota_num    : Nota numerica del estudiante        (entrada)
    nota_letra  : Nota equivalente en letra            (salida)
"""

# Constantes
NOTA_MINIMA = 0
NOTA_MAXIMA = 100

# --- Inputs ---
nota_num = int(input(f"Digite la nota [{NOTA_MINIMA},{NOTA_MAXIMA}]: "))

# --- Process ---
if (nota_num > NOTA_MAXIMA) or (nota_num < NOTA_MINIMA):
    # --- Outputs ---
    print('ERROR: Nota invalida, fuera de rango [0,100]')
else:
    if (nota_num >= 90):
        nota_letra = 'A'
    else:
        if (nota_num >= 90):
            nota_letra = 'A'
        if (80 <= nota_num < 90):
            nota_letra = 'B'
        if (70 <= nota_num < 80):
            nota_letra = 'C'
        if (60 <= nota_num < 70):
            nota_letra = 'D'
        if (nota_num < 60):
            nota_letra = 'E'
    # --- Outputs ---
    print(f'{nota_num} = {nota_letra}')
