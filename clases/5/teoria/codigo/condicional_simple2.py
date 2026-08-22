# Constantes
SALARIO_MIN = 2_000_000

# Inicialización de variables
subsidio = 0

# --- Inputs ---
ID = input("Digite la cedula: ")
sal_base = int(input("Digite el salario base: "))

# --- Process ---
if sal_base < SALARIO_MIN:
    subsidio = 0.3 * sal_base

sal_neto = sal_base + subsidio

# --- Outputs ---
print(f'{ID} le corresponde como pago ${sal_neto}')