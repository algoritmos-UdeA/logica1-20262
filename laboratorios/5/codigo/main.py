"""
Laboratorio 5 - Parqueadero: el programa principal.

ESTE ARCHIVO YA ESTÁ COMPLETO. No hay que modificarlo.

Presenta un menú y usa la clase Parqueadero para atender cada opción.
Funciona cuando las cuatro clases (Vehiculo, Puesto, Recibo y
Parqueadero) están completas y todas las pruebas pasan.

Se ejecuta con: python main.py
"""
from vehiculo import Vehiculo
from parqueadero import Parqueadero
from pantalla import mostrar_mapa, mostrar_vehiculos, mostrar_recibo

PISOS = 2
PUESTOS_POR_PISO = 5


def mostrar_menu():
    """Garantiza: imprime las opciones del menú. No retorna nada."""
    print()
    print("===== Parqueadero =====")
    print("1. Ingresar vehículo")
    print("2. Retirar vehículo")
    print("3. Buscar vehículo")
    print("4. Ver mapa")
    print("5. Ver vehículos")
    print("6. Ver recaudo")
    print("0. Salir")


def leer_tipo():
    """
    Garantiza: pide el tipo de vehículo hasta que sea 1 o 2, y retorna
    Vehiculo.CARRO o Vehiculo.MOTO.
    """
    opcion = input("Tipo (1 carro, 2 moto): ")
    while opcion != "1" and opcion != "2":
        print("Tipo no válido.")
        opcion = input("Tipo (1 carro, 2 moto): ")
    tipo = Vehiculo.MOTO
    if opcion == "1":
        tipo = Vehiculo.CARRO
    return tipo


def cargar_vehiculos_iniciales(parqueadero):
    """Garantiza: ingresa tres vehículos, para no empezar con el parqueadero vacío."""
    parqueadero.ingresar_vehiculo(Vehiculo("ABC123", Vehiculo.CARRO))
    parqueadero.ingresar_vehiculo(Vehiculo("XYZ78A", Vehiculo.MOTO))
    parqueadero.ingresar_vehiculo(Vehiculo("DEF456", Vehiculo.CARRO))


def ingresar(parqueadero):
    placa = input("Placa: ")
    tipo = leer_tipo()
    vehiculo = Vehiculo(placa, tipo)
    puesto = parqueadero.ingresar_vehiculo(vehiculo)
    if puesto == None:
        print("No se pudo ingresar: el parqueadero está lleno")
        print("o ya hay un vehículo con esa placa.")
    else:
        print("Vehículo ingresado.", puesto)


def retirar(parqueadero):
    placa = input("Placa: ")
    minutos = int(input("Minutos que estuvo: "))
    recibo = parqueadero.retirar_vehiculo(placa, minutos)
    if recibo == None:
        print("No hay un vehículo con esa placa.")
    else:
        mostrar_recibo(recibo)


def buscar(parqueadero):
    placa = input("Placa: ")
    puesto = parqueadero.buscar_vehiculo(placa)
    if puesto == None:
        print("No hay un vehículo con esa placa.")
    else:
        print(puesto)


def main():
    parqueadero = Parqueadero(PISOS, PUESTOS_POR_PISO)
    cargar_vehiculos_iniciales(parqueadero)

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            ingresar(parqueadero)
        elif opcion == "2":
            retirar(parqueadero)
        elif opcion == "3":
            buscar(parqueadero)
        elif opcion == "4":
            mostrar_mapa(parqueadero)
        elif opcion == "5":
            mostrar_vehiculos(parqueadero)
        elif opcion == "6":
            print("Recaudo: $" + str(parqueadero.get_recaudo()))
        elif opcion == "0":
            print("Hasta luego.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
