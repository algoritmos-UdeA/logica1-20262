"""
Resumen: Mediante el siguiente ejemplo se implementa un menu interactivo que permite al usuario elegir entre tres opciones: 
agregar, consultar y salir. Se emplea un ciclo while con una condición siempre verdadera (True) y una instrucció de ruptura 
(break) para salir del ciclo cuando el usuario elige la opción de salir.
"""

while True:
    print("1. Agregar")
    print("2. Consultar")
    print("3. Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 3:
        break  # Instrucción de ruptura
    elif opcion == 1:
        print("Agregando...")
    elif opcion == 2:
        print("Consultando...")
    else:
        print("Opcion invalida")

print("Programa finalizado.")
