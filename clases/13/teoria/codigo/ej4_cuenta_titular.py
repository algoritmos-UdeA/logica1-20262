"""Ejemplo 4: Titular y CuentaBancaria, asociación (diapositivas 42-48)."""


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


if __name__ == "__main__":
    # Diapositiva 47
    homero = Titular("Homero Simpson", "1001")
    marge = Titular("Marge Simpson", "1002")
    cuenta_h = CuentaBancaria(homero, 30000.0)
    cuenta_m = CuentaBancaria(marge)
    print(cuenta_h)
    print(cuenta_m)
    print(cuenta_h.transferir(cuenta_m, 15000.0))
    print(cuenta_m.transferir(cuenta_h, 99000.0))
    print(cuenta_h)
    print(cuenta_m)

    # Diapositiva 48
    cuenta_h = CuentaBancaria(homero, 30000.0)
    cuenta_m = CuentaBancaria(marge)
    assert cuenta_m.get_saldo() == 0.0
    assert cuenta_h.transferir(cuenta_m, 15000.0) == True
    assert cuenta_h.get_saldo() == 15000.0
    assert cuenta_m.get_saldo() == 15000.0
    assert cuenta_m.transferir(cuenta_h, 99000.0) == False
    assert cuenta_m.get_saldo() == 15000.0
    assert cuenta_h.get_saldo() == 15000.0
    print("CuentaBancaria: todas las pruebas pasaron")
