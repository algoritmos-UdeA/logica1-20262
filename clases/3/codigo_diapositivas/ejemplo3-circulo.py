"""
Programa: Cálculo del área de un círculo
Autor: [Nombre del estudiante]
Fecha: [Fecha]
Descripción: Solicita al usuario el radio de un círculo, 
             calcula su área y muestra el resultado en pantalla.
"""

# Inicialización de variables
PI = 3.14

# Entrada de datos
radio = float(input("Ingrese el radio del círculo: "))

# Calculo del area
area = PI * radio ** 2

# Despligue del area
print(f"El area del círculo de radio {radio} es: {area}")
