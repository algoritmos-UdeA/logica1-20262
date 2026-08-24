# Constantes
SALARIO_MIN = 2_000_000
flag_sal_valido = True

# --- Inputs ---
ID = input("Digite la cedula: ")
sal_base = int(input("Digite el salario base: "))

# --- Process ---
if sal_base < SALARIO_MIN:
    subsidio = 0.3 * sal_base
else:
    if sal_base >= SALARIO_MIN:
        subsidio = 0
    else:
        flag_sal_valido = False

sal_neto = sal_base + subsidio

# --- Outputs ---
if flag_sal_valido:
    print(f'{ID} le corresponde como pago ${sal_neto}')
else:
    print('Salario no valido')