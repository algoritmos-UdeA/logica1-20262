"""
Resumen: Programa que permite ingresar y validar una clave maximo 3 veces.
"""

intentos = 0
correcta = False
clave_real = "1234"

while intentos < 3:
    clave = input('Ingrese su clave: ')
    if clave == clave_real:
        correcta = True
        break  # Instrucción de ruptura
    intentos += 1
    print(f"Clave incorrecta, intento {intentos} de 3")

if correcta:
    print("Acceso concedido.")
else:
    print("Acceso bloqueado.")
