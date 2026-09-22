# Inicializacion

fact = 1    # Acumulador (producto)

n = int(input('Digite el numero (mayor o igual a 0): '))

for i in range(1, n + 1):
  fact *= i # fact = fact * i

print(f"{n}! = {fact}")
