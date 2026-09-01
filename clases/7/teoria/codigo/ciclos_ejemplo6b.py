"""
Resumen:
Este ejemplo usando un centinela para el control del ciclo. La centinela es un valor especial que indica 
el fin de la entrada de datos. En este caso, la centinela es -1, que indica que no hay más estudiantes 
a los que se les ingresará la nota.
"""

# Constantes
NOTA_MINIMA = 3.0

# Inicializacion
notas_reprobadas = 0
notas_aprobadas = 0
suma_reprobadas = 0
suma_aprobadas = 0

# Solicitud de la nota del estudiante
nota = float(input('Ingrese la nota del estudiante (-1 para terminar): '))
while nota != -1:    
    # Validadación si gano o perdio
    if nota >= NOTA_MINIMA:
        # Gano
        notas_aprobadas += 1    
        suma_aprobadas += nota  
    else:
        # Perdio
        notas_reprobadas += 1
        suma_reprobadas += nota

    # Solicitud de la nota del estudiante
    nota = float(input('Ingrese la nota del estudiante (-1 para terminar): '))

# Calculo de los totales 
num_notas = notas_reprobadas + notas_aprobadas
suma_notas = suma_reprobadas + suma_aprobadas
if num_notas == 0:
    # Caso en el que no hay estudiantes
    print("No hay estudiantes")
else:
    # Calculo de los porcentajes y promedios
    p_aprobaron = (notas_aprobadas/num_notas)*100
    p_reprobaron = (notas_reprobadas/num_notas)*100
    prom_nota_reprobada = suma_reprobadas/notas_reprobadas
    prom_nota_aprobada = suma_aprobadas/notas_aprobadas
    prom = suma_notas/num_notas

    # Salida de datos
    print(f"Porcentaje de estudiantes que aprobaron: {p_aprobaron}%")
    print(f"Porcentaje de estudiantes que reprobaron: {p_reprobaron}%")
    print(f"Promedio de notas reprobadas: {prom_nota_reprobada}")
    print(f"Promedio de notas aprobadas: {prom_nota_aprobada}")
    print(f"Promedio general de notas: {prom}")

