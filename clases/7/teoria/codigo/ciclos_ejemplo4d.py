# Inicializacion

i = 0 # Contador (empleado como exponente)

# Entrada de datos
n = int(input('Ingrese un número entero positivo: '))
num = n   # Iniciacion de la variable de control num (contador)

# Proceso y salida (Impresion de la secuencia de números enteros positivos y negativos)
while num > 0:
    print((-1)**i*num, end = ' ')   # Se imprime el numero
    i = i + 1                       # Actualizacion del contador (exponente)  
    num = num - 1                   # Actualizacion de la variable de control

