num_divisores = 0

num = int(input("Ingrese un número entero positivo: "))

for i in range(1, num//2 + 1):
    if num % i == 0:
        num_divisores += 1
        print(f"{i} es divisor de {num}")

print(f"El número de divisores de {num} es: {num_divisores}")