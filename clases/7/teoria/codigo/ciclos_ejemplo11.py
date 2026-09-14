"""
Resumen: Este ejemplo permite ingresar una serie de números y calcular su suma. Emplea un ciclo while con una 
condición siempre verdadera (True) y una instrucción de ruptura (break) para salir del ciclo cuando se ingresa el 
valor -1, que indica que no se desean ingresar más números. Al final se despliega la suma total de los números 
ingresados.
"""

suma = 0
while True:
    numero = int(input('Ingrese un numero (-1 para terminar): '))
    if numero == -1:
        break  # Instrucción de ruptura
    suma = suma + numero

print(f"Suma total: {suma}")
