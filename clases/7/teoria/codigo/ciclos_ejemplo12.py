"""
Resumen: Ejemplo que que permite ingresar una serie de datos y validar que sean positivos. Emplea un ciclo while con 
una condición controlada por un contador y una instrucción de ruptura (break) para salir del ciclo cuando se ingresa 
un dato negativo, indicando que hubo un error en la entrada de datos.
"""

N = int(input('Cantidad de datos: '))
i = 0
huboError = False

while i < N:
    dato = int(input(f'Ingrese el dato {i}: '))
    if dato < 0:
        print(f"Dato invalido en la posicion {i}")
        huboError = True
        break  # Instrucción de ruptura
    i += 1

if not huboError:
    print("Todos los datos se procesaron correctamente.")
