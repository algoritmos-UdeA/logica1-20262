"""
Aplicación de transporte: el programa principal.

Presenta un menú y usa la clase Plataforma para atender cada opción.
Crea los clientes y los conductores (por eso importa cliente.py y
conductor.py), pero nunca crea un Punto ni un Viaje: de eso se encargan
las otras clases.

Se ejecuta con: python main.py
"""
from cliente import Cliente
from conductor import Conductor
from plataforma import Plataforma


def mostrar_menu():
    """Garantiza: imprime las opciones del menú."""
    print()
    print("===== Plataforma de transporte =====")
    print("1. Registrar cliente")
    print("2. Registrar conductor")
    print("3. Ubicar cliente")
    print("4. Ubicar conductor")
    print("5. Solicitar viaje")
    print("6. Finalizar viaje")
    print("7. Ver clientes")
    print("8. Ver conductores")
    print("9. Ver viajes")
    print("0. Salir")


def cargar_datos_iniciales(plataforma):
    """
    Garantiza: registra cuatro clientes y cuatro conductores en la
    plataforma, cada uno en una posición distinta.
    """
    lucia = Cliente("1001", "Lucia")
    michael = Cliente("1002", "Michael")
    michael.set_posicion(2.0, 3.0)
    kendl = Cliente("1003", "Kendl")
    kendl.set_posicion(10.0, 10.0)
    trevor = Cliente("1004", "Trevor")
    trevor.set_posicion(-4.0, -3.0)
    plataforma.registrar_cliente(lucia)
    plataforma.registrar_cliente(michael)
    plataforma.registrar_cliente(kendl)
    plataforma.registrar_cliente(trevor)

    tommy = Conductor("2001", "Tommy", "VCT986")
    tommy.set_posicion(3.0, 4.0)
    cj = Conductor("2002", "CJ", "GRV992")
    cj.set_posicion(1.0, 1.0)
    catalina = Conductor("2003", "Catalina", "LBC008")
    catalina.set_posicion(9.0, 12.0)
    franklin = Conductor("2004", "Franklin", "LSA013")
    franklin.set_posicion(-6.0, -8.0)
    plataforma.registrar_conductor(tommy)
    plataforma.registrar_conductor(cj)
    plataforma.registrar_conductor(catalina)
    plataforma.registrar_conductor(franklin)


def registrar_cliente(plataforma):
    cedula = input("Cédula del cliente: ")
    nombre = input("Nombre: ")
    cliente = Cliente(cedula, nombre)
    plataforma.registrar_cliente(cliente)
    print("Cliente registrado:", cliente)


def registrar_conductor(plataforma):
    cedula = input("Cédula del conductor: ")
    nombre = input("Nombre: ")
    placa = input("Placa: ")
    conductor = Conductor(cedula, nombre, placa)
    plataforma.registrar_conductor(conductor)
    print("Conductor registrado:", conductor)


def ubicar_cliente(plataforma):
    cedula = input("Cédula del cliente: ")
    cliente = plataforma.buscar_cliente(cedula)
    if cliente == None:
        print("No hay un cliente con esa cédula.")
    else:
        x = float(input("Coordenada x (km): "))
        y = float(input("Coordenada y (km): "))
        cliente.set_posicion(x, y)
        print("Nueva ubicación:", cliente)


def ubicar_conductor(plataforma):
    cedula = input("Cédula del conductor: ")
    conductor = plataforma.buscar_conductor(cedula)
    if conductor == None:
        print("No hay un conductor con esa cédula.")
    else:
        x = float(input("Coordenada x (km): "))
        y = float(input("Coordenada y (km): "))
        conductor.set_posicion(x, y)
        print("Nueva ubicación:", conductor)


def solicitar_viaje(plataforma):
    cedula = input("Cédula del cliente: ")
    x = float(input("Coordenada x del destino (km): "))
    y = float(input("Coordenada y del destino (km): "))
    viaje = plataforma.solicitar_viaje(cedula, x, y)
    if viaje == None:
        print("No se pudo crear el viaje: el cliente no está registrado,")
        print("ya tiene un viaje en curso o no hay conductores disponibles.")
    else:
        print("Viaje creado:", viaje)
        print("Conductor asignado:", viaje.get_conductor())


def finalizar_viaje(plataforma):
    cedula = input("Cédula del cliente: ")
    if plataforma.finalizar_viaje(cedula):
        print("Viaje finalizado.")
    else:
        print("Ese cliente no tiene un viaje en curso.")


def main():
    plataforma = Plataforma()
    cargar_datos_iniciales(plataforma)

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            registrar_cliente(plataforma)
        elif opcion == "2":
            registrar_conductor(plataforma)
        elif opcion == "3":
            ubicar_cliente(plataforma)
        elif opcion == "4":
            ubicar_conductor(plataforma)
        elif opcion == "5":
            solicitar_viaje(plataforma)
        elif opcion == "6":
            finalizar_viaje(plataforma)
        elif opcion == "7":
            plataforma.mostrar_clientes()
        elif opcion == "8":
            plataforma.mostrar_conductores()
        elif opcion == "9":
            plataforma.mostrar_viajes()
        elif opcion == "0":
            print("Hasta luego.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
