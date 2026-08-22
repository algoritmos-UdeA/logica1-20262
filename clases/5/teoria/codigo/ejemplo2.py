# --- Inputs ---
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

# --- Process / Outputs ---
if num1 % num2 == 0:
    print(f"{num2} es divisor de {num1}")
else:
    print(f"{num2} no es divisor de {num1}")