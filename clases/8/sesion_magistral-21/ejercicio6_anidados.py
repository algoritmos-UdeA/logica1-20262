# Inicializacion
suma = 0 # Aproximacion de e^x

# Entradas
N = int(input("Indique el valor de N (exponente del ultimo termino): "))
x = float(input("Indique el valor de x: "))

# Proceso
for n in range(0, N + 1):
    # Calculo del factorial de n
    fact = 1
    for j in range(1, n + 1):
        fact *= j

    # Calculo del termino n-esimo
    term = (x**n)/fact

    # Actualizacion de la suma
    suma += term

# Salidas
print(f"e^{x} aproximado con N = {N} es: {suma:.6f}")
