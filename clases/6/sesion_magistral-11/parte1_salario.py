# Constantes
HORA_BASE = 35
EXTRA = 1.5

# Inicializacion de variables
sal_base = 0
hr_extra = 0
imp = 0
sal_neto = 0

# Entrada de datos
nom = input("Nombre: ")
hr = int(input("Horas: "))
valor_hr = int(input("Valor hora: "))

# Calculo del salario base
if hr <= HORA_BASE:
    sal_base = valor_hr*hr
else:
    hr_extra = hr - HORA_BASE
    sal_base = valor_hr*HORA_BASE + EXTRA*valor_hr*hr_extra

print(sal_base)  # Se imprime para verificar el calculo del salario base

# Calculo de los impuestos
# To Do...



    