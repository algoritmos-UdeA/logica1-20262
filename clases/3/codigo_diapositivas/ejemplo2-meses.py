"""
Programa: Calculo del número de meses entre dos años
Autor: [Nombre del estudiante]
Fecha: [Fecha]
Descripción: Solicita al usuario el año inicial y el año final, calcula el número de meses entre ellos 
             mostrando el resultado en pantalla.
"""

# Entrada de datos
init_year = int(input("Ingrese el año inicial: "))
final_year = int(input("Ingrese el año final: "))

# Calculo del area
years = final_year - init_year
months = years * 12

# Despligue de los meses
print(f"El número de meses entre los años {init_year} y {final_year} es: {months}")