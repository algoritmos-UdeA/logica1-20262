"""
Resumen: Este ejemplo permite ingresar una edad válida. Emplea un ciclo while con una condición siempre verdadera (True) 
y una instrucción de ruptura (break) para salir del ciclo cuando se ingresa una edad válida, para que prosiga el procedimiento.
"""

while True:
    edad = int(input('Ingrese su edad: '))
    if 0 <= edad <= 120:
        break  # Instrucción de ruptura
    else:
        print("Edad invalida, intente de nuevo.")

print(f"Edad registrada: {edad}")
