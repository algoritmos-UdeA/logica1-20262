num_divisores = 0

num = int(input("Ingrese un número entero positivo: "))

for i in range(1, num//2 + 1):
    if num % i == 0:
        num_divisores += 1
        

if num_divisores > 2:
    print(f"{num} no es primo")
else:
    print(f"{num} es primo")