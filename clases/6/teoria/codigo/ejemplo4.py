"""
Ejemplo 4 - Solucion

Se desea obtener la nomina semanal (salario neto) de los empleados de
una empresa cuyo trabajo se paga por horas, del siguiente modo:

- Las horas inferiores o iguales a 35 (normales) se pagan a una tarifa
  que se introduce por teclado, junto con el numero de horas y el
  nombre del trabajador.
- Las horas superiores a 35 se pagan como extra, a 1.5 veces la
  tarifa normal.
- Los impuestos a deducir varian en funcion del salario bruto:
    - Si sal_base <= 300000, libre de impuestos.
    - Los siguientes 150000 al 20%.
    - El resto al 30%.

Datos de entrada:
    - Nombre
    - Horas trabajadas
    - Tarifa hora

Datos de salida:
    - Nombre
    - Salario base (bruto)
    - Impuesto
    - Salario neto

Definicion de variables:
    nom            : Nombre del trabajador     (entrada/salida)
    hr_trabajadas  : Horas trabajadas          (entrada)
    hr_precio      : Tarifa por hora           (entrada)
    hr_extra       : Horas extra (> 35)        (auxiliar)
    sal_base       : Salario bruto             (salida)
    impuesto       : Impuesto a descontar      (auxiliar)
    sal_neto       : Salario neto              (salida)
"""

# Constantes
HORAS_NORMALES = 35
TARIFA_EXTRA = 1.5

# Inicialización de variables
impuesto = 0

# --- Inputs ---
nom = input("Digite el nombre del trabajador: ")
hr_trabajadas = float(input("Digite las horas trabajadas: "))
hr_precio = float(input("Digite la tarifa por hora: "))

# --- Process ---
if (hr_trabajadas <= HORAS_NORMALES):
    sal_base = hr_trabajadas*hr_precio
else:
    hr_extra = hr_trabajadas - HORAS_NORMALES
    sal_base = HORAS_NORMALES*hr_precio + TARIFA_EXTRA*hr_precio*hr_extra

if (sal_base >= 300000):
    if (sal_base <= 450000):
        impuesto = 0.2 * (sal_base - 300000)
    else:
        impuesto = 0.2*150000 + 0.3*(sal_base - 450000)

sal_neto = sal_base - impuesto

# --- Outputs ---
print('=' * 40)
print('COLILLA DE PAGO'.center(40))
print('=' * 40)
print(f'{"Empleado:":<20}{nom}')
print(f'{"Horas trabajadas:":<20}{hr_trabajadas}')
print(f'{"Tarifa por hora:":<20}${hr_precio:.0f}')
print('-' * 40)
print(f'{"Salario base:":<20}${sal_base:.0f}')
print(f'{"Impuesto:":<20}-${impuesto:.0f}')
print('-' * 40)
print(f'{"Salario neto:":<20}${sal_neto:.0f}')
print('=' * 40)