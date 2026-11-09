"""Ejemplo 5: un arreglo de cuentas (diapositivas 49-51)."""
from ej4_cuenta_titular import Titular, CuentaBancaria

cuentas = [None] * 3
cuentas[0] = CuentaBancaria(Titular("Homero Simpson", "1001"), 15000.0)
cuentas[1] = CuentaBancaria(Titular("Marge Simpson", "1002"), 15000.0)
cuentas[2] = CuentaBancaria(Titular("Señor Burns", "1003"), 1000000.0)

# Diapositiva 50: el mayor saldo
pos_mayor = 0
for i in range(1, len(cuentas)):
    if cuentas[i].get_saldo() > cuentas[pos_mayor].get_saldo():
        pos_mayor = i
print(pos_mayor)
print(cuentas[pos_mayor])

# Diapositiva 51: un bono para cada cuenta
for i in range(len(cuentas)):
    cuentas[i].depositar(10000.0)

for i in range(len(cuentas)):
    print(cuentas[i])
