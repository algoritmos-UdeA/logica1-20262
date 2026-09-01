# Inicializacion

i = 1       # Contador
fact = 1    # Acumulador (producto)

n = int(input('Digite el numero (mayor o igual a 0): '))
while i <= n:
  fact = fact * i
  i = i + 1
print(f"{n}! = {fact}")
