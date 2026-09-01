# Inicializacion

num = 1     # Contador
suma = 0    # Acumulador

# Entrada de datos
N = int(input('Ingrese la candidad de números a sumar: '))

# Proceso
while num <= N:
  suma = suma + num
  num = num + 1

# Salida de datos
print(f"La suma de los {N} primeros números da {suma}")
