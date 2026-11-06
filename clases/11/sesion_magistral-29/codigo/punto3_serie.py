########## Inicializacion de variables ##########
# Contadores
term_1 = 1   # Termino menor del denominador
term_2 = 2   # Termino mayor del denominador
expo = 3     # Exponente del numerador
# Bandera
signo = False  # True: positivo, False: negativo
# Acumulador
suma = 1

########## Entrada de datos ##########
X = float(input("Ingrese el valor de X: "))
N = int(input("Ingrese el número de términos N: "))

########## Ciclo para el calculo de la suma #########
for i in range(0, N - 1):
    # Calculo del termino
    term = (X**expo)/(term_1*term_2)
    # Alternancia de signos
    if signo:
        suma += term
    else:
        suma -= term
    # Actualizacion de variables
    term_1 += 2
    term_2 += 2
    expo += 2
    signo = not signo # Cambio de signo

####### Impresion del resultado #######
print(f"La suma de los primeros {N} términos es: {suma}")


