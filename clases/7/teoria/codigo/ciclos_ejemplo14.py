"""
Resumen: Program que emplea ciclos anidados para determinar los números primos hasta un límite dado por el usuario. 
"""

n = int(input('Ingrese un limite: '))

for numero in range(2, n + 1):
    esPrimo = True
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            esPrimo = False
            break  # Instrucción de ruptura (solo corta el ciclo interno)
        divisor += 1

    if esPrimo:
        print(f"{numero} es primo")
