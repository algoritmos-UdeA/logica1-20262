# Inicializacion de variables

s = 0
coef = 1

# Entradas
N = int(input("Digite el numero de entradas: "))
x = float(input("Digite el valor de la variable: "))

# Proceso
for i in range(N):    
    term = coef*(x**i)
    print(f"i = {i}; x**i = {x**i}, coef = {coef}, term = {term}")
    s += term 
    coef += 1
        
# Salidas
print(f"s = {s}")