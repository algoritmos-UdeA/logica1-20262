es_primo = True

num = int(input("Ingrese un número entero positivo: "))

for i in range(2, num//2 + 1):
    if num % i == 0:
        es_primo = False
        break

if es_primo:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")