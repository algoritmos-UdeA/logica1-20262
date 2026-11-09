"""Ejemplo 6: la clase Banco, composición (diapositivas 52-59). Mismas pruebas del Ejemplo 5 + ordenar y cupo.

El Banco guarda el arreglo de cuentas como atributo y es quien crea cada cuenta
(abrir_cuenta). Por eso la relación es de composición: Banco ◆── CuentaBancaria.
"""


def intercambiar(lista, i, j):
    """Intercambia los elementos de las posiciones i y j (la misma función de ordenamientos.py)."""
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp


class Titular:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula

    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula


class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.__titular = titular
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

    def retirar(self, valor):
        retirado = False
        if valor <= self.__saldo:
            self.__saldo = self.__saldo - valor
            retirado = True
        return retirado

    def transferir(self, destino, valor):
        transferido = False
        if self.retirar(valor):
            destino.depositar(valor)
            transferido = True
        return transferido

    def __str__(self):
        return (self.__titular.get_nombre()
                + ": $" + str(self.__saldo))


class Banco:
    def __init__(self, nombre, cupo):
        self.__nombre = nombre
        self.__cuentas = [None] * cupo
        self.__cantidad = 0

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_cuenta(self, posicion):
        return self.__cuentas[posicion]

    def abrir_cuenta(self, titular, saldo=0.0):
        abierta = False
        if self.__cantidad < len(self.__cuentas):
            self.__cuentas[self.__cantidad] = CuentaBancaria(titular, saldo)
            self.__cantidad = self.__cantidad + 1
            abierta = True
        return abierta

    def posicion_mayor_saldo(self, inicio=0):
        pos_mayor = inicio
        for j in range(inicio + 1, self.__cantidad):
            if self.__cuentas[j].get_saldo() > self.__cuentas[pos_mayor].get_saldo():
                pos_mayor = j
        return pos_mayor

    def ordenar_por_saldo(self):
        for i in range(self.__cantidad - 1):
            pos_mayor = self.posicion_mayor_saldo(i)
            intercambiar(self.__cuentas, i, pos_mayor)

    def dar_bono(self, valor):
        for i in range(self.__cantidad):
            self.__cuentas[i].depositar(valor)


# Uso: el mismo Ejemplo 5, ahora con el Banco
banco = Banco("Banco de Springfield", 5)
banco.abrir_cuenta(Titular("Homero Simpson", "1001"), 15000.0)
banco.abrir_cuenta(Titular("Marge Simpson", "1002"), 15000.0)
banco.abrir_cuenta(Titular("Señor Burns", "1003"), 1000000.0)

pos_mayor = banco.posicion_mayor_saldo()
print(pos_mayor)
print(banco.get_cuenta(pos_mayor))

banco.dar_bono(10000.0)
for i in range(banco.get_cantidad()):
    print(banco.get_cuenta(i))

banco.ordenar_por_saldo()
for i in range(banco.get_cantidad()):
    print(banco.get_cuenta(i))

# Pruebas
assert banco.get_cantidad() == 3
assert banco.get_cuenta(0).get_titular().get_nombre() == "Señor Burns"
assert banco.get_cuenta(1).get_saldo() == 25000.0
assert banco.posicion_mayor_saldo() == 0
assert banco.abrir_cuenta(Titular("Lisa Simpson", "1004")) == True
assert banco.abrir_cuenta(Titular("Bart Simpson", "1005")) == True
assert banco.abrir_cuenta(Titular("Maggie Simpson", "1006")) == False   # no hay cupo
assert banco.get_cantidad() == 5
print("Banco: todas las pruebas pasaron")
