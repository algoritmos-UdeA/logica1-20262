# Inicializacion

num = 1     # Contador
suma = 0    # Acumulador

# Entrada de datos
N = int(input('Ingrese la candidad de números a sumar: '))

# Proceso
for i in range(1, N + 1):
  suma += i # suma = suma + i

# Salida de datos
print(f"La suma de los {N} primeros números da {suma}")
